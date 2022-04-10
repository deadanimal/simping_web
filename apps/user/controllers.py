# Import flask dependencies
from flask import Blueprint, redirect, request, render_template, jsonify, flash, abort, session
from web3.auto import w3
from eth_account.messages import encode_defunct
from web3 import Web3
from web3.middleware import geth_poa_middleware
import sqlalchemy
import time
from decouple import config

from apps.user.models import User
from apps import db

user_bp = Blueprint('user', __name__, url_prefix='/user')


@user_bp.route('/', methods=['GET'])
def user_list():
    user_list = db.session.query(User).order_by(User.date_created.desc())
    return render_template('user/list.html', users=user_list)



@user_bp.route('/<int:user_id>', methods=['GET'])
def user_detail(user_id):
    user = db.session.query(u).filter_by(id=user_id).first()
    if user:
        return render_template('user/detail.html', user=user)    
    else:
        return render_template('404.html')   

