# Use a base image with Python installed
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code to the container
COPY source ./src
COPY model ./model
COPY data ./data
COPY run_pipeline.py

# Set the command to run when the container starts
CMD ["python", "run_pipeline.py"]