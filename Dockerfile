# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script into the container
COPY calculator.py .

# Command to run the Python script
CMD ["python", "calculator.py"]
