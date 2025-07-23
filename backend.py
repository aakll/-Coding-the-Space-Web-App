from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

# Load model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "best_rf_model.pkl")

try:
    model = joblib.load(MODEL_PATH)
    print(f"✅ Model loaded successfully from {MODEL_PATH}")
    print(f"Model type: {type(model)}")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    raise

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json['processedData']
        df = pd.DataFrame(data)
        
        features = [
            "Minimum Orbit Intersection",
            "Absolute Magnitude",
            "Avg_Diameter_KM",
            "Perihelion Distance",
            "Orbit Uncertainity",
            "Inclination"
        ]
        
        predictions = model.predict(df[features]).tolist()
        return jsonify({'predictions': predictions})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Render requires dynamic port binding
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
