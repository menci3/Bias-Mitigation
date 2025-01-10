# Use the official Python image as a base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir --progress-bar=on --verbose -r requirements.txt

# Copy only the generate.py script into the container
COPY generate.py .

# Set the default command to run the generate.py script
CMD ["python", "generate.py"]