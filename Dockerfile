# Use the official Python image as a base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Expose the port that Flask will run on
EXPOSE 5000

# Define the command to run your application
CMD ["python", "app.py"]

# For Jenkins
USER root
RUN apt-get update && apt-get install -y sudo

# Jenkins-specific settings
ARG user=jenkins
ARG group=jenkins
ARG uid=1000
ARG gid=1000

RUN groupadd -g ${gid} ${group} \
    && useradd -d "/var/jenkins_home" -u ${uid} -g ${gid} -m -s /bin/bash ${user} \
    && usermod -aG sudo ${user} \
    && echo "${user} ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# Switch back to non-root user
USER ${user}

# Jenkins runs on port 8080
EXPOSE 8080
