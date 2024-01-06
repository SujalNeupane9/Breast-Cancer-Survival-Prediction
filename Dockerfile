# Use a base image with Python installed
FROM python:3.9

# WORKDIR - sets the working directory for any RUN, CMD, ENTRYPOINT, COPY and ADD instructions that follow it in the Dockerfile.
WORKDIR /service

# Copy the requirements file to the container
COPY requirements.txt .

#COPY - copies files or directories and adds them to the filesystem of the container.
COPY . ./

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Set the command to run when the container starts
CMD ["python", "run_pipeline.py"]
