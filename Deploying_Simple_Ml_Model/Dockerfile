# Use a base image with Python
FROM python:3.11.4

# Set the working directory in the container
WORKDIR /app

# Copy the necessary files into the container
COPY . .

# Install the required Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# Run the Python script when the container starts
CMD ["python", "app.py"]
