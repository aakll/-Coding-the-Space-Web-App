#!/bin/bash

# Space Hazard Predictor Deployment Script

echo "🚀 Space Hazard Predictor Deployment Script"
echo "============================================="

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "📝 Initializing git repository..."
    git init
    git add .
    git commit -m "Initial commit: Space Hazard Predictor"
fi

echo ""
echo "Select deployment platform:"
echo "1) Heroku"
echo "2) Railway" 
echo "3) Render"
echo "4) Vercel"
echo "5) Docker (local)"
echo "6) Show deployment URLs"
echo ""

read -p "Enter your choice (1-6): " choice

case $choice in
    1)
        echo "🌐 Deploying to Heroku..."
        if ! command -v heroku &> /dev/null; then
            echo "❌ Heroku CLI not found. Please install it first:"
            echo "   https://devcenter.heroku.com/articles/heroku-cli"
            exit 1
        fi
        
        read -p "Enter your app name (or press enter for auto-generated): " app_name
        
        if [ -z "$app_name" ]; then
            heroku create
        else
            heroku create $app_name
        fi
        
        git add .
        git commit -m "Deploy to Heroku" --allow-empty
        git push heroku main
        heroku open
        ;;
        
    2)
        echo "🚂 Railway deployment:"
        echo "1. Go to https://railway.app"
        echo "2. Connect your GitHub repository"
        echo "3. Deploy with one click"
        echo "4. Railway will auto-detect Python and deploy"
        ;;
        
    3)
        echo "🎨 Render deployment:"
        echo "1. Go to https://render.com"
        echo "2. Create new Web Service"
        echo "3. Connect your GitHub repository"
        echo "4. Build Command: pip install -r requirements.txt"
        echo "5. Start Command: gunicorn backend:app"
        ;;
        
    4)
        echo "▲ Vercel deployment:"
        if ! command -v vercel &> /dev/null; then
            echo "Installing Vercel CLI..."
            npm i -g vercel
        fi
        vercel login
        vercel
        ;;
        
    5)
        echo "🐳 Building Docker container..."
        if ! command -v docker &> /dev/null; then
            echo "❌ Docker not found. Please install Docker first."
            exit 1
        fi
        
        docker build -t space-hazard-predictor .
        echo "✅ Docker image built successfully!"
        echo "Run with: docker run -p 8080:8080 space-hazard-predictor"
        ;;
        
    6)
        echo "📋 Deployment Platform URLs:"
        echo "• Heroku: https://heroku.com"
        echo "• Railway: https://railway.app" 
        echo "• Render: https://render.com"
        echo "• Vercel: https://vercel.com"
        echo "• Google Cloud: https://cloud.google.com"
        echo "• AWS: https://aws.amazon.com"
        echo ""
        echo "📖 See DEPLOYMENT.md for detailed instructions"
        ;;
        
    *)
        echo "❌ Invalid choice. Please run the script again."
        exit 1
        ;;
esac

echo ""
echo "✅ Deployment process initiated!"
echo "📖 Check DEPLOYMENT.md for detailed instructions and troubleshooting"