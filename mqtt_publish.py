import paho.mqtt.publish as publish

hostname = "iot.eclipse.org" # Sandbox broker
port = 1883 # Default port for unencrypted MQTT

topic = "elec3542/test" # '/' as delimiter for sub-topics

# API reference can be found at https://eclipse.org/paho/clients/python/docs/#id17
publish.single(topic, payload="Hello, MQTT!", 
	qos=0,
	hostname=hostname,
	port=port)
