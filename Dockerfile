#Deriving the latest base image
FROM python:latest


# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY src/ /app/

# Define the command to run your script when the container starts
CMD ["python", "main.py"]