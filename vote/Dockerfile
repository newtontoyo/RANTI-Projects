# Use lightweight Python base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY vote.py .

# Expose port
EXPOSE 5000

# Run app
CMD ["python", "vote.py"]
