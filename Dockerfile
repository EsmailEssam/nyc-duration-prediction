# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Copy the current directory contents into the container at /app
COPY . /app

RUN pip install --upgrade pip

# Set the working directory in the container
WORKDIR /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run app.py when the container launches
CMD ["python","app.py"]