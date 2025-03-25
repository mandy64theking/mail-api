import os
from flask import Flask, jsonify, request
from dotenv import load_dotenv
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from smtp_client.email import email
from flask_cors import CORS

app = Flask(__name__) 
CORS(app)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["2000 per day", "100 per hour"],
    storage_uri="memory://",
)
load_dotenv() 
# configuration of mail 
app.config['MAIL_SERVER']='smtp.hostinger.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.environ.get("MY_EMAIL_ID")
app.config['MAIL_PASSWORD'] = os.environ.get("MY_EMAIL_PW")
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

# message object mapped to a particular URL ‘/’ 
@app.route("/demo-request", methods=['POST']) 
def index():
    api_key = request.headers.get("x-api-key")
    if api_key != os.environ.get("API_KEY"):
        return jsonify({"error": "Unauthorized"}), 401
    if request.method == "OPTIONS":
        return '', 204
    if request.method == 'POST':
        params = request.json
        email.send_email(params=params)
        return 'Sent'
   
if __name__ == '__main__': 
    app.run(port=os.environ.get("PORT"))