# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file and install the Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the entire project into the working directory
COPY . .

# Expose the port that the Flask app will run on
EXPOSE 5000

# Define the command to run the Flask app
CMD ["python", "inference.py"]
