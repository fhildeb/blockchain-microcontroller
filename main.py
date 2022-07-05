# IoT
# Created at 2020-12-20 12:36:31.142305

# config.py
import config

# Micro Controller Unit for Reset Functionality
import mcu

# WiFi Drivers
from espressif.esp32net import esp32wifi as net_driver

from wireless import wifi

# SSL for HTTPS
import ssl

# Serial Interface for Terminal
import streams

# Mosquitto Library for Status Updates within the Terminal
from mqtt import mqtt

# Ethereum Connection
from blockchain.ethereum import ethereum
from blockchain.ethereum import rpc

# Global Variables
# Status of Actor Module
currentStatus = 0
previousStatus = 0
init = 1


# SSL Context for HTTPS Certificate
SSL_CTX = ssl.create_ssl_context(
    cacert=config.CA_CERT,
    options=ssl.CERT_REQUIRED|ssl.SERVER_AUTH
)

# Status Monitoring on Console
streams.serial()

# Initiate WiFi
def init_wifi():
    # Connect to WiFi Network
    print(config.WIFI_CONNECTING)
    net_driver.auto_init()
    wifi.link(config.WIFI_SSID, wifi.WIFI_WPA2, config.WIFI_PASSWORD)
    print(config.WIFI_CONNECTED)

# Read Actor Module Status from Smart Contract
def get_actor_status():
    global led_contract
    previousStatus = currentStatus
    status = led_contract.call(config.CONTRACT_READ)
    sleep(1000)
    
    if (status == config.CONTRACT_LED_VALUE):
        currentStatus = 1
    else:
        currentStatus = 0
    
    if init == 1:
        if currentStatus == 0:
            print(config.MQTT_ACTOR_PUBLISH_OFF)
            if config.ENABLE_MOSQUITTO == 1:
                client.publish(config.MQTT_ACTOR_CHANNEL, config.DEVICE_NAME + ': ' + config.MQTT_ACTOR_PUBLISH_OFF)
        init = 0

    if (currentStatus != previousStatus):
        if (currentStatus == 1):
            digitalWrite(D13, HIGH)
            print(config.MQTT_ACTOR_PUBLISH_ON)
            if config.ENABLE_MOSQUITTO == 1:
                client.publish(config.MQTT_ACTOR_CHANNEL, config.DEVICE_NAME + ': ' + config.MQTT_ACTOR_PUBLISH_ON)
        else:
            digitalWrite(D13, LOW)
            print(config.MQTT_ACTOR_PUBLISH_OFF)
            if config.ENABLE_MOSQUITTO == 1:
                client.publish(config.MQTT_ACTOR_CHANNEL, config.DEVICE_NAME + ': ' + config.MQTT_ACTOR_PUBLISH_OFF)

# Mosquitto
# Callback Function to Receive Mosquitto Message

# Regular Message
def regular_message(client, data):
    message = data['message']
    message_payload = message.payload.strip()
    print(config.MQTT_RAW_MESSAGE + message_payload)

# Actor Module Reset
# Filtering the Mosquitto Messages from Master Module
def is_master_reset_command(data):
    if('message' in data):
        print('is_master_reset_command(): ' + data['message'].topic)
        print(data['message'].topic == config.MQTT_MASTER_CHANNEL)
        return (data['message'].topic == config.MQTT_MASTER_CHANNEL)
    return False

# Reaction
def get_master_reset_command(client, data):
    message = data['message']
    command = message.payload.strip()
    print(config.MQTT_MASTER_RECEIVED + command)
    reset_command = config.MQTT_ACTOR_PUBLISH_RESET
    print(config.MQTT_MASTER_EXPECTED + reset_command)
    if command == reset_command:
        print(config.MQTT_MASTER_RESET_INIT)
        client.publish(config.MQTT_ACTOR_CHANNEL, config.MQTT_ACTOR_PUBLISH_RESET)
        # Reset Actor Module
        mcu.reset()

# Mosquitto
def talk_to_mosquitto():
    # Connect to Mosquitto Broker and Request Access
    print(config.MQTT_CONNECTING)
    for entry in range(2):
        try:
            # Client Setup
            client.connect(config.MQTT_BROKER_IP_ADDRESS, 60)
            break
        except Exception as e:
            print( config.MQTT_ERROR + e)
    print(config.MQTT_CONNECTED + config.MQTT_BROKER_IP_ADDRESS)


    # Subscribe to Mosquitto Channels

    # Mosquitto-Rx-Channels
    # Master Module
    qos = 1
    client.subscribe([[config.MQTT_MASTER_CHANNEL, qos]])

    # Mosquitto-Rx-Callback
    # Master Module
    client.on(mqtt.PUBLISH, get_master_reset_command, is_master_reset_command)

    # Regular Mosquitto Messages
    client.on(mqtt.PUBLISH, regular_message)

    # Start Mosquitto-Rx-Loop
    client.loop()

    # Tell Mosquitto Broker that Actor Module is ready
    client.publish(config.MQTT_ACTOR_CHANNEL, config.MQTT_ACTOR_PUBLISH_READY)

# Main Programm Procedure
try:
    # WiFi
    init_wifi()
    
    # Initiate Pins on Module
    pinMode(D13, OUTPUT)

    # Ethereum
    # Create Instance on Infura RPC-Node
    eth = rpc.RPC(config.RPC_URL, ssl_ctx = SSL_CTX)
    print(config.RPC_CREATED)

    # Create Instance of Smart Contract
    led_contract = ethereum.Contract(
        eth,
        config.CONTRACT_ADDRESS,
        config.PRIVATE_KEY,
        config.ADDRESS,
        chain=ethereum.ROPSTEN
    )
    print(config.CONTRACT_CREATED)

    # Handing over all Functions from the Smart Contract
    # to the led_contract Instance
    for name in config.CONTRACT_METHODS:
        method = config.CONTRACT_METHODS[name]
        led_contract.register_function(
            name,
            config.GAS_PRICE,
            method['gas_limit'],
            args_type=method['args']
        )
        print( config.CONTRACT_METHOD_PRE + name + config.CONTRACT_METHOD_POST)
    
    # Not used when started without Mosquitto
    client = None
    
    # Mosquitto is Enabled
    if config.ENABLE_MOSQUITTO == 1:
        client = mqtt.Client(config.MQTT_USER_NAME, True)
        talk_to_mosquitto()

except Exception as e:
    print(e)

# Main Loop

while True:

    # Read and Publish Status of Actor Module from Smart Contract
    get_actor_status();
    sleep(3000)