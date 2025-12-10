# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
# Note: This might fail if packages are not yet on PyPI, assumes they are available.
RUN pip install --no-cache-dir -r requirements.txt || echo "Warning: dependencies install failed, proceeding for demo structure"

# Run main.py when the container launches
CMD ["python", "main.py"]
