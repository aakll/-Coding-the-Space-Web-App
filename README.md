# Space Hazard Predictor 🚀

A machine learning web application that predicts space hazards from astronomical data. Built with React frontend and Flask backend.

## Features

- 🛰️ Upload CSV files with asteroid/object data
- 🤖 Machine learning predictions using Random Forest model
- 🌌 Beautiful space-themed UI with animations
- 📊 Real-time data validation and processing
- 🚀 Multiple deployment options

## Quick Start

### Local Development

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the backend:**
   ```bash
   python backend.py
   ```

3. **Open the frontend:**
   - Open `index.html` in your browser, or
   - Serve with Python: `python -m http.server 3000`

4. **Test the application:**
   - Upload a CSV file with the required columns
   - View predictions and processed data

### Required CSV Columns

Your CSV file should contain these columns:
- `Minimum Orbit Intersection`
- `Absolute Magnitude` 
- `Avg_Diameter_KM`
- `Perihelion Distance`
- `Orbit Uncertainity`
- `Inclination`

## Deployment 🚀

### Quick Deploy (Recommended)

Run the interactive deployment script:
```bash
./deploy.sh
```

### Platform Options

| Platform | Complexity | Free Tier | Best For |
|----------|------------|-----------|----------|
| **Railway** | ⭐ Easy | Yes | Beginners |
| **Render** | ⭐⭐ Easy | Yes | Full-stack apps |
| **Heroku** | ⭐⭐ Medium | Limited | Traditional deployment |
| **Vercel** | ⭐⭐ Medium | Yes | Serverless |
| **Docker** | ⭐⭐⭐ Advanced | N/A | Any platform |

### 1-Click Deployments

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template)

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

### Manual Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions for all platforms.

## Project Structure

```
├── index.html              # Frontend (React SPA)
├── backend.py              # Flask API server
├── validation.py           # Data validation utilities
├── final_rf_model.joblib   # Trained ML model
├── requirements.txt        # Python dependencies
├── runtime.txt            # Python version
├── Procfile               # Heroku configuration
├── Dockerfile             # Docker configuration
├── vercel.json            # Vercel configuration
├── netlify.toml           # Netlify configuration
└── deploy.sh              # Deployment script
```

## API Endpoints

- `GET /` - Health check
- `GET /api/health` - API health status
- `POST /predict` - Make predictions (development)
- `POST /api/predict` - Make predictions (production)

## Technologies Used

### Frontend
- React 18 (via CDN)
- Tailwind CSS
- Custom animations and space theme

### Backend
- Flask (Python web framework)
- scikit-learn (Machine learning)
- pandas (Data processing)
- joblib (Model serialization)
- Flask-CORS (Cross-origin requests)

### Deployment
- Gunicorn (WSGI server)
- Docker support
- Multiple platform configurations

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `PORT` | Server port | `5000` |
| `FLASK_ENV` | Environment | `development` |

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally
5. Submit a pull request

## Troubleshooting

### Common Issues

1. **Model file missing**: Ensure `final_rf_model.joblib` is included
2. **CSV upload fails**: Check required columns are present
3. **CORS errors**: Verify backend is running on correct port
4. **Memory issues**: Ensure deployment platform has sufficient memory (512MB+)

### Getting Help

- Check [DEPLOYMENT.md](DEPLOYMENT.md) for platform-specific issues
- Review the deployment script output for errors
- Ensure all dependencies are properly installed

## License

This project is open source and available under the [MIT License](LICENSE).

---

Made with ❤️ for space safety and asteroid detection 🌌