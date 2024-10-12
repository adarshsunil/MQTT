# MQTT Subscriber and Logging System

This project implements an MQTT subscriber using the Mosquitto broker. The subscriber logs received messages to `received_messages.log` and logs errors (e.g., disconnections, broker timeouts) to `errors.log`. The project is containerized using Docker for easy setup and deployment.

## Features

- **Task 1**: Set up the Mosquitto broker using Docker Compose, accessible on the default MQTT port (`1883`).
- **Task 2**: Implement an MQTT subscriber that listens for messages on the topic pattern `devices/+/status` and logs received messages to `received_messages.log`.
- **Task 3**: Implement error handling for the MQTT subscriber, logging errors (e.g., disconnections) to `errors.log`.

## Prerequisites

To run this project, you need the following installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Git](https://git-scm.com/)

## Setup Instructions

### 1. Clone the Repository

Clone the project using SSH:

```bash
git clone git@github.com:adarshsunil/MQTT.git
cd MQTT
```
### 2. Build and Run the Docker Containers
Use Docker Compose to build and run the Mosquitto broker and the MQTT subscriber under the Subscriber folder:
```bash
sudo docker-compose up -d --build
```

This will spin up two containers:

Mosquitto Broker (mosquitto-broker): Provides the MQTT broker on port 1883.
MQTT Subscriber (mqtt-subscriber): Subscribes to devices/+/status and logs messages and errors.

### 3. Publish Messages to the Broker
You can use the mosquitto_pub tool to publish messages to the broker:
```bash
mosquitto_pub -h localhost -t devices/device1/status -m "Device 1 is online"
mosquitto_pub -h localhost -t devices/device2/status -m "Device 2 is online"
```

### 4. Check Logs
Message logs are saved in received_messages.log:

```bash
cat received_messages.log
```
Error logs (e.g., disconnections) are saved in errors.log:

```bash
cat errors.log
```
### 5. Stopping the Containers
To stop the Docker containers, run:
```bash
sudo docker-compose down
```
