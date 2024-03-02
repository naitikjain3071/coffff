# # Use an official Python runtime as a base image
# FROM python:3.9-slim

# # Set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# # Set the working direxctory in the container
# WORKDIR /app

# # Install Python dependencies
# COPY requirements.txt /app/
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the current directory contents into the container at /app
# COPY . /app/
# COPY uwsgi.ini /app/

# # Run the command to start uWSGI
# # CMD ["uwsgi", "app.ini"]
# CMD ["uwsgi", "--ini", "uwsgi.ini"]
# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies required for uWSGI
RUN apt-get update && apt-get install -y \
    gcc \
    libc6-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install uwsgi
# Copy the current directory contents into the container at /app
COPY . /app/
COPY uwsgi.ini /app/
COPY requirements.txt /app/
# Create a user and group
RUN addgroup --system django && adduser --system --ingroup django django

# Copy the application and set ownership to the created user
COPY --chown=django:django . /app/

# Switch to the non-root user
USER django


# Run the command to start uWSGI
CMD ["uwsgi", "--ini", "uwsgi.ini", "--enable-threads"]

