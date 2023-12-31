# Use an official Python runtime as a parent image
FROM harbor.mgmt-bld.oncp.dev/staging_base_images/python:3.10.6-alpine3.16

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
COPY . .
RUN pip config set global.cert /app/combined_certs.pem
# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

## Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]