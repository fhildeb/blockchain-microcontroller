# How to Kill Mosquitto on TCP Port
sudo lsof -i TCP:1883
sudo kill [proccess-id]

# How to connect with Sub Mosquitto
mosquitto_sub -h [broker-address] -t [channel] -V [version] | ts
mosquitto_sub -h mqtt.fluux.io -t "iot/master" -V "mqttv311" | ts
mosquitto_sub -h mqtt.fluux.io -t "iot/Actor-1/status" -V "mqttv311" | ts

# Thingy-52
mosquitto_sub -h mqtt.fluux.io -t "iot/Thingy52-1/status" -V "mqttv311" | ts
mosquitto_sub -h mqtt.fluux.io -t "iot/Thingy52-1/temperature" -V "mqttv311" | ts
mosquitto_sub -h mqtt.fluux.io -t "iot/Thingy52-1/air_pressure" -V "mqttv311" | ts
mosquitto_sub -h mqtt.fluux.io -t "iot/Thingy52-1/humidity" -V "mqttv311" | ts
mosquitto_sub -h mqtt.fluux.io -t "iot/Thingy52-1/co2" -V "mqttv311" | ts
mosquitto_sub -h mqtt.fluux.io -t "iot/Thingy52-1/tvoc" -V "mqttv311" | ts
mosquitto_sub -h mqtt.fluux.io -t "iot/Thingy52-1/step_counter" -V "mqttv311" | ts

# Master-Module Nachrichten senden
mosquitto_pub -h mqtt.fluux.io -t "iot/master" -V "mqttv311" -m "Master: Actor-1 reset."
