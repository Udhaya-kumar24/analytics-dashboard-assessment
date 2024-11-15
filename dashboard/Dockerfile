# Use the official Python image from Docker Hub
FROM python:3.11-slim

# Set environment variables to avoid Python writing .pyc files and buffering logs
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Expose port 8000 (Django's default port)
EXPOSE 8000

# Run the application using Gunicorn
CMD ["gunicorn", "dashboard.wsgi:application", "--bind", "0.0.0.0:8000"]
