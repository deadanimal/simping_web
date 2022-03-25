import requests
import json
import time
import os

from flask import Flask, render_template, flash, request, redirect, session
from flask_recaptcha import ReCaptcha
from flask_sqlalchemy import SQLAlchemy
from decouple import config
from web3.auto import w3
from eth_account.messages import encode_defunct
from authy.api import AuthyApiClient
from flask_migrate import Migrate
from flask_cors import CORS


app = Flask(__name__)


app.config['DEBUG'] = config('DEBUG')
app.config['BASE_DIR'] = os.path.abspath(os.path.dirname(__file__))  
app.config['DATABASE_CONNECT_OPTIONS'] = {}
app.config['CSRF_SESSION_KEY'] = config('SECRET_KEY')
app.config['SECRET_KEY'] = config('SECRET_KEY')
app.config['CSRF_SESSION_KEY'] = config('SECRET_KEY')
app.config['CSRF_ENABLED'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = config('DB_URL')
# app.config['RECAPTCHA_SITE_KEY'] = config('RECAPTCHA_SITE_KEY')
# app.config['RECAPTCHA_SECRET_KEY'] = config('RECAPTCHA_SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CSRF_ENABLED'] = True
app.config['THREADS_PER_PAGE'] = 2

recaptcha = ReCaptcha(app) 
db = SQLAlchemy(app)
#authy_api = AuthyApiClient(config('AUTHY_KEY'))
migrate = Migrate(app, db)
CORS(app)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/profile')
def profile():
    if session.get("wallet"):
        wallet = session['wallet']
        context = {
            wallet: wallet
        }
        return render_template('profile.html', context=context)    
    else:
        flash("Your login cannot be verified")
        return redirect('/')

@app.route('/login-via-web3', methods=['GET', 'POST'])
def login_via_web3():
    
    if request.method == "POST":
        wallet = request.values['wallet']
        timestamp = request.values['timestamp']
        signature = request.values['signature']
        signer = request.values['signer']
        message_text = config('BASE_URL') + "," + timestamp
        verified = verify_message(message_text, wallet, signature)
        if verified:
            session['wallet'] = wallet
            session['timestamp'] = timestamp
            session['signature'] = signature
            if signer:
                session['signer'] = signer
            flash("Your login is successful")
            print("Your login is successful")
            return redirect('/')
        else:
            flash("Your login cannot be verified")
            print("Your login cannot be verified")
    wallet = request.args.get('address')
    timestamp = request.args.get('ts')
    signature = request.args.get('sig')
    signer = request.args.get('signer')
    return render_template('login_via_web3.html', wallet=wallet, timestamp=timestamp, signature=signature, signer=signer)    

@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    flash("You have been logged out")
    return redirect('/')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
  


from apps.lotto.controllers import lotto_bp as lotto_module
app.register_blueprint(lotto_module)

db.create_all()

def verify_message(message_text, address, signature):
    message = encode_defunct(text=message_text)
    got_address = w3.eth.account.recover_message(message, signature=signature)

    if got_address == address:
        return True
    else:
        return False