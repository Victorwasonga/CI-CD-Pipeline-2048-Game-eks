# Use a lightweight official Python base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the entire app into the container
COPY . .

# Install Flask (no need for requirements.txt)
RUN pip install --no-cache-dir flask

# Expose port 5000 for the Flask app
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]