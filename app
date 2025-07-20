from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated ML model (just for testing)
def predict_hazard(size):
    if size > 50:
        return 1  # Hazardous
    else:
        return 0  # Non-hazardous

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    sizes = data.get('sizes', [])
    results = [predict_hazard(float(size)) for size in sizes]
    return jsonify({'predictions': results})

if __name__ == '__main__':
    app.run(debug=True)
