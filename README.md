# mycloud
Simple repo to learn how to use my old Mac as server


# How to

## To run the app
python app.py

## To find the IP address of the device serving
```
ifconfig
en0 
inet
```

## To find public IP address
curl ipinfo.io/ip

 # CURL command to test the server

 ` curl -X POST <IP ADRESS>:8088/capitalize -H "Content-Type: application/json" -d '{"text": "hello world"}' `

 # IP Addresses
 
 ## Localhost
 curl -X POST http://127.0.0.1:8088/capitalize -H "Content-Type: application/json" -d '{"text": "hello world"}'

## IP MacBook Air
curl -X POST http://192.168.219.6:8088/capitalize -H "Content-Type: application/json" -d '{"text": "hello world"}'
## IP MacBook Pro
curl -X POST http://192.168.219.7:8088/capitalize -H "Content-Type: application/json" -d '{"text": "hello world"}'

## Public IP Chalet
curl -X POST http://172.226.162.83:8088/capitalize -H "Content-Type: application/json" -d '{"text": "hello worldz"}'