# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Copy the current directory contents into the container at /app
COPY . /app

# Set the working directory in the container
WORKDIR /app

RUN pip install --upgrade pip

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Define environment variable to tell Flask to run the app
ENV FLASK_APP=app.py

# Command to run the application
CMD ["flask", "run",  "--host=0.0.0.0"]