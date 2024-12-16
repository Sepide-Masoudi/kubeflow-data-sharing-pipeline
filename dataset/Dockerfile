# Use a Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and the application files
COPY requirements.txt ./
COPY dataset-service.py ./
COPY sample-new.csv ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Define the command to run the app
CMD ["python", "dataset-service.py"]
