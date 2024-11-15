# Use a minimal Python image
FROM python:3.11-slim

# Install only essential packages
RUN apt-get update && apt-get install -y \
    openjdk-11-jre-headless \
    && apt-get clean

# Set environment variables for Java
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

# Install PySpark and Django dependencies
RUN pip install --no-cache-dir pyspark django

# Set the working directory
WORKDIR /app

# Copy project files into the container
COPY . /app

# Expose port 8000 for Django
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]