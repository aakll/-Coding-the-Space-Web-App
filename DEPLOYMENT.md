# Space Hazard Predictor - Deployment Guide

This guide covers multiple deployment options for your Space Hazard Predictor application.

## Project Structure
- `index.html` - Frontend React application (single page)
- `backend.py` - Flask API server with machine learning model
- `final_rf_model.joblib` - Trained ML model file
- `validation.py` - Data validation utilities
- `requirements.txt` - Python dependencies
- `runtime.txt` - Python version specification

## Deployment Options

### 1. Heroku (Recommended for Full-Stack Apps)

#### Prerequisites
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) installed
- Git repository

#### Steps
```bash
# 1. Login to Heroku
heroku login

# 2. Create a new Heroku app
heroku create your-space-hazard-app

# 3. Deploy
git add .
git commit -m "Deploy Space Hazard Predictor"
git push heroku main

# 4. Open your app
heroku open
```

Your app will be available at: `https://your-space-hazard-app.herokuapp.com`

### 2. Railway

#### Steps
1. Go to [Railway.app](https://railway.app)
2. Connect your GitHub repository
3. Railway will automatically detect the Python app
4. Deploy with one click

### 3. Render

#### Steps
1. Go to [Render.com](https://render.com)
2. Create a new Web Service
3. Connect your GitHub repository
4. Use these settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn backend:app`
   - Environment: Python 3

### 4. Google Cloud Platform (Cloud Run)

#### Prerequisites
- [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) installed
- Google Cloud project with billing enabled

#### Steps
```bash
# 1. Build and deploy
gcloud run deploy space-hazard-predictor \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

### 5. AWS (Elastic Beanstalk)

#### Prerequisites
- [AWS CLI](https://aws.amazon.com/cli/) installed
- [EB CLI](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install.html) installed

#### Steps
```bash
# 1. Initialize EB application
eb init -p python-3.10 space-hazard-predictor

# 2. Create environment and deploy
eb create space-hazard-env

# 3. Open app
eb open
```

### 6. Vercel (Frontend + Serverless Backend)

#### Prerequisites
- [Vercel CLI](https://vercel.com/cli) installed

#### Steps
```bash
# 1. Login to Vercel
vercel login

# 2. Deploy
vercel

# 3. Follow prompts and deploy
vercel --prod
```

### 7. Docker Deployment

#### Build and run locally:
```bash
# Build image
docker build -t space-hazard-predictor .

# Run container
docker run -p 8080:8080 space-hazard-predictor
```

#### Deploy to any Docker-compatible platform:
- AWS ECS
- Google Cloud Run
- Azure Container Instances
- DigitalOcean App Platform

## Environment Configuration

### Production Environment Variables
Some platforms may require these environment variables:

```bash
FLASK_ENV=production
PORT=8080  # Or the port your platform uses
```

### Local Development
To run locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Run backend
python backend.py

# Open index.html in browser or serve with a static server
python -m http.server 3000
```

## Important Notes

1. **Model File**: The `final_rf_model.joblib` file (1MB) is included and will be deployed with your app.

2. **CORS**: The backend is configured to accept requests from any origin in development. For production, consider restricting CORS origins.

3. **API Endpoints**: The frontend automatically detects the environment and uses:
   - `http://localhost:5000/predict` for development
   - `/api/predict` for production

4. **File Size Limits**: Most platforms have file upload limits. Current setup should work for typical CSV files.

## Troubleshooting

### Common Issues

1. **Build fails**: Ensure all files are committed to git
2. **Model not found**: Verify `final_rf_model.joblib` is in the repository
3. **CORS errors**: Check that CORS is properly configured in `backend.py`
4. **Memory issues**: The ML model requires sufficient memory (512MB+ recommended)

### Platform-Specific Notes

- **Heroku**: Free tier has limitations; consider upgrading for production use
- **Vercel**: Great for frontend, serverless functions have cold start times
- **Railway**: Simple deployment with good free tier
- **Render**: Good balance of features and pricing

## Security Considerations

1. Add rate limiting for the prediction endpoint
2. Validate file uploads more strictly
3. Consider authentication for sensitive deployments
4. Use HTTPS (most platforms enable this by default)

## Monitoring

Add these endpoints to monitor your deployment:
- `/api/health` - Health check endpoint
- `/api` - API status and information

## Next Steps

After deployment, consider:
1. Setting up monitoring and logging
2. Adding analytics
3. Implementing user feedback
4. Adding more robust error handling
5. Creating automated tests