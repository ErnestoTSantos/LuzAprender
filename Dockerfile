FROM python:3.10-slim

WORKDIR /app

# Installs poetry and pip
RUN pip install --upgrade pip 

# Copy dependency definition to cache
COPY requirements.txt ./

# Installs projects dependencies
RUN pip install -r requirements.txt

COPY . ./

EXPOSE 8080