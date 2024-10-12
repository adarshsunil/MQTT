FROM python:3.9-slim

WORKDIR /app

# Upgrade pip to the latest version and install the latest paho-mqtt version
RUN pip install --upgrade pip && pip install paho-mqtt==1.6.1

# Copy the subscriber script into the container
COPY . .

# Run the subscriber script
CMD ["python", "subscriber.py"]

