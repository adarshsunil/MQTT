import logging
import os
import paho.mqtt.client as mqtt

# Ensure the log files are created
message_log_path = "received_messages.log"
error_log_path = "errors.log"
if not os.path.exists(message_log_path):
    open(message_log_path, 'w').close()
if not os.path.exists(error_log_path):
    open(error_log_path, 'w').close()

# Set up message logging
message_logger = logging.getLogger("messageLogger")
message_logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(message_log_path)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
message_logger.addHandler(file_handler)

# Set up error logging
error_logger = logging.getLogger("errorLogger")
error_logger.setLevel(logging.ERROR)
error_file_handler = logging.FileHandler(error_log_path)
error_file_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
error_logger.addHandler(error_file_handler)

# Log a startup message for messages
message_logger.info("Message logging setup complete. Ready to log messages.")
error_logger.error("Error logging setup complete. Ready to log errors.")  # Just to confirm errors log setup

# Callback function when a message is received
def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode()
    print(f"DEBUG: Received message on {topic}: {payload}")
    message_logger.info(f"Received message on {topic}: {payload}")
    file_handler.flush()  # Ensure log is written to file

# Callback function when connected to the broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully")
        client.subscribe("devices/+/status")
        print("Subscribed to devices/+/status")
    else:
        error_logger.error(f"Failed to connect to broker, return code {rc}")
        print(f"Failed to connect, return code {rc}")

# Callback function for disconnections
def on_disconnect(client, userdata, rc):
    if rc != 0:
        error_logger.error(f"Unexpected disconnection, return code {rc}")
        print(f"Unexpected disconnection, return code {rc}")

# Create MQTT client instance
client = mqtt.Client(protocol=mqtt.MQTTv311)

# Attach callback functions
client.on_message = on_message
client.on_connect = on_connect
client.on_disconnect = on_disconnect

# Connect to the broker
try:
    client.connect("mosquitto", 1883)
    print(f"Connected to broker at mosquitto:1883")
except Exception as e:
    error_logger.error(f"Error connecting to broker: {e}")

# Start the loop
try:
    client.loop_forever()
except Exception as e:
    error_logger.error(f"Unexpected error in MQTT loop: {e}")

