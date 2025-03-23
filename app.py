import os
from flask import Flask, render_template,request
from flask_mail import Mail, Message 
from dotenv import load_dotenv
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__) 
mail = Mail(app) # instantiate the mail class 
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["2000 per day", "100 per hour"],
    storage_uri="memory://",
)


load_dotenv() 
# configuration of mail 
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.environ.get("MY_EMAIL_ID")
app.config['MAIL_PASSWORD'] = os.environ.get("MY_EMAIL_PW")
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

# message object mapped to a particular URL ‘/’ 
@app.route("/demo-request", methods=['POST']) 
def index():
   if request.method == 'POST':
    print(request.json)
    params = request.json
    msg = Message( 
                'New Demo Request', 
                sender ='demoupmovechess@gmail.com', 
                recipients = ['upmovechess@gmail.com'] 
               ) 
    msg.html = render_template('emailBody.html',params=params)
    mail.send(msg) 
    return 'Sent'
   
if __name__ == '__main__': 
   app.run(host='0.0.0.0', port = 8080, debug = True)