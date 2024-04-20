# Use the official Python image as a base image. This image is based on debian. 
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask and dependencies
RUN pip install --no-cache-dir Flask

# Expose the Flask application port
EXPOSE 5000

# Define the command to run the Flask application when the container starts
CMD ["python3", "webapp.py"]



# Create the image; 
# $ docker build -t python-app-testn .

# Run the container which runs on port 4000 on host machine
# docker run -d -p 4000:5000 python-app-testn

# Test your application
# hit http://localhost:4000 on web


# Tag and push the image 
# First create a repository in dockerhub. I have created with name python_fask_2024

# $ docker tag python-app-testn mannsaxenaxebia/python_fask_2024:v1-15-april
# $ docker push mannsaxenaxebia/python_fask_2024:v1-15-april

# Username      ; mannsaxenaxebia
# Repository    ; python_fask_2024
# image name    ; python-app-testn
# tag           ; v1-15-april