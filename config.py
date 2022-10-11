# IoT
# Created at 2020-12-20 12:36:31.142305

# Device Name of Actor Module
DEVICE_NAME = 'Actor-1'

# PIN of LED from Actor Module
PIN_LED = 13

# WLAN-Access
WIFI_SSID = 'my_wifi_name'
WIFI_PASSWORD = 'my_wifi_password'
WIFI_CONNECTING = 'Trying to connect to WiFi...'
WIFI_CONNECTED = 'WiFi connected.'

# Mosquitto Functionality
ENABLE_MOSQUITTO = 1

# Mosquitto Broker
MQTT_BROKER_IP_ADDRESS = 'mqtt.fluux.io'
MQTT_USER_NAME = ''
MQTT_PASSWORD = ''

# Mosquitto Master Outputs
MQTT_MASTER_CHANNEL = 'iot/master'

# Mosquitto Actor Outputs
MQTT_ACTOR_CHANNEL = 'iot/Actor-1/status'
MQTT_ACTOR_PUBLISH_READY = 'Actor-1 is ready'
MQTT_ACTOR_PUBLISH_RESET = 'Master: Actor-1 reset.'
MQTT_ACTOR_PUBLISH_ON = 'Actor-1 is on'
MQTT_ACTOR_PUBLISH_OFF = 'Actor-1 is off'
MQTT_CONNECTED = 'Connected with Mosquitto Broker: '
MQTT_ERROR = 'Connection to Mosquitto Broker failed with Error: '
MQTT_CONNECTING = 'Trying to connect to Mosquitto Broker...'
MQTT_MASTER_RECEIVED = 'Received Command from Master Module: '
MQTT_MASTER_EXPECTED = 'Expected Command from Master Module: '
MQTT_MASTER_RESET_INIT = 'Reset of Actor Module initiated.'
MQTT_MASTER_RESET_COMMAND = 'is_master_reset_command(): '
MQTT_RAW_MESSAGE = 'raw mosquitto message: '

RPC_CREATED = 'RPC-Node Instance created'

# Users MetaMask
ADDRESS = '0x302BB128f6dc9f2b25646B6537353783B6408A14'
PRIVATE_KEY = '8cebc20e5ed9ff733fd7833605bbe1d66ca3b6efac483fc3026fc6d21a37f8c7'

# Smart Contract Address
CONTRACT_ADDRESS = '0xe485C39B96a17f8be840B4eaCEeDF7BCcF4427E9'
CONTRACT_LED_VALUE = '0x0000000000000000000000000000000000000000000000000000000000000001'
CONTRACT_READ = 'readLed'
CONTRACT_CREATED = 'Smart Contract Instance created'
CONTRACT_METHOD_PRE = 'Smart Contract Method '
CONTRACT_METHOD_POST = ' created'

# Ethereum Methods
CONTRACT_METHODS = {
    "readLed": {
        "args": (),
        "gas_limit": "0x6691b7",
    },
}

# Defined Transaction Price
GAS_PRICE = "0x174876e800"

# Infura-RPC-URL
RPC_URL = 'my_infura_rpc'

# SSL Certificate
CA_CERT = """-----BEGIN CERTIFICATE----- 
MIIDQTCCAimgAwIBAgITBmyfz5m/jAo54vB4ikPmljZbyjANBgkqhkiG9w0BAQsF 
ADA5MQswCQYDVQQGEwJVUzEPMA0GA1UEChMGQW1hem9uMRkwFwYDVQQDExBB
bWF6b24gUm9vdCBDQSAxMB4XDTE1MDUyNjAwMDAwMFoXDTM4MDExNzAwMDAwMF
owOTELMAkGA1UEBhMCVVMxDzANBgNVBAoTBkFtYXpvbjEZMBcGA1UEAxMQQW1he
m9uIFJvb3QgQ0EgMTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALJ4gH
HKeNXjca9HgFB0fW7Y14h29Jlo91ghYPl0hAEvrAIthtOgQ3pOsqTQNroBvo3bSMgHFzZM 
9O6II8c+6zf1tRn4SWiw3te5djgdYZ6k/oI2peVKVuRF4fn9tBb6dNqcmzU5L/qw 
IFAGbHrQgLKm+a/sRxmPUDgH3KKHOVj4utWp+UhnMJbulHheb4mjUcAwhmahRWa6 
VOujw5H5SNz/0egwLX0tdHA114gk957EWW67c4cX8jJGKLhD+rcdqsq08p8kDi1L 
93FcXmn/6pUCyziKrlA4b9v7LWIbxcceVOF34GfID5yHI9Y/QCB/IIDEgEw+OyQm 
jgSubJrIqg0CAwEAAaNCMEAwDwYDVR0TAQH/BAUwAwEB/zAOBgNVHQ8BAf8EBAMC 
AYYwHQYDVR0OBBYEFIQYzIU07LwMlJQuCFmcx7IQTgoIMA0GCSqGSIb3DQEBCwUA 
A4IBAQCY8jdaQZChGsV2USggNiMOruYou6r4lK5IpDB/G/wkjUu0yKGX9rbxenDI 
U5PMCCjjmCXPI6T53iHTfIUJrU6adTrCC2qJeHZERxhlbI1Bjjt/msv0tadQ1wUs 
N+gDS63pYaACbvXy8MWy7Vu33PqUXHeeE6V/Uq2V8viTO96LXFvKWlJbYK8U90vv 
o/ufQJVtMVT8QtPHRh8jrdkPSHCa2XV4cdFyQzR1bldZwgJcJmApzyMZFo6IQ6XU 
5MsI+yMRQ+hDKXJioaldXgjUkK642M4UwtBV8ob2xJNDd2ZhwLnoQdeXeGADbkpy 
rqXRfboQnoZsG4q5WTP468SQvvG5 
-----END CERTIFICATE----- 
\x00"""
