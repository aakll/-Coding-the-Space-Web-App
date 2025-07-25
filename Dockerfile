# Use Python 3.10 as base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Expose port 8080 (common for cloud platforms)
EXPOSE 8080

# Run the Flask application
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "backend:app"]