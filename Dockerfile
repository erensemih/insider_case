# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt /usr/src/app/

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Copy the rest of the application
COPY . /usr/src/app

RUN apt-get update && apt-get install -y \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*
# Make port 5000 available to the world outside this container
EXPOSE 5000

CMD ["python3", "./app.py"]