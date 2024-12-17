from flask import Flask, request
import requests
import os

app = Flask(__name__)

# Ngrok에서 제공한 공용 URL
#LOCAL_PC_URL = "https://939e-112-217-166-10.ngrok-free.app"

@app.route('/')
def home():
    #data = {"message": "Hello from Azure WebApp!"}
    #response = requests.post(LOCAL_PC_URL, json=data)
    #return f"Response from local PC: {response.text}"
    return "Hello, this is the Azure WebApp!"

@app.route('/forward', methods=['GET'])
def forward():
    return "Hello, this is the Azure WebApp!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)