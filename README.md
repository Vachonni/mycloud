# mycloud
Simple repo to learn how to use my old Mac as server


# To run the app
python app.py


 # CURL command to test the server

 ## Localhost
 curl -X POST http://127.0.0.1:8088/capitalize -H "Content-Type: application/json" -d '{"text": "hello world"}'

## MacBook Air
curl -X POST http://192.168.219.6:8088/capitalize -H "Content-Type: application/json" -d '{"text": "hello world"}'
