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
