# Import flask dependencies
from flask import Blueprint, redirect, request, render_template, jsonify, flash, abort, session
from web3.auto import w3
from eth_account.messages import encode_defunct
from web3 import Web3
from web3.middleware import geth_poa_middleware
import sqlalchemy
import time
from decouple import config

from apps.lotto.models import Lottery
from apps import db

lotto_bp = Blueprint('lotto', __name__, url_prefix='/lotto')


@lotto_bp.route('/', methods=['GET'])
def lotto_list():
    lotteries = db.session.query(Lottery).order_by(Lottery.date_created.desc())
    return render_template('lotto/list.html', lottos=lotteries)



@lotto_bp.route('/<int:lotto_id>', methods=['GET'])
def lotto_detail(lotto_id):
    lottery = db.session.query(Lottery).filter_by(id=lotto_id).first()
    if lottery:
        return render_template('lotto/detail.html', lotto=lottery)    
    else:
        return render_template('404.html')   



@lotto_bp.route('/result', methods=['GET'])
def lotto_result_list():
    lotteries = db.session.query(Lottery).filter_by(ended=True).order_by(Lottery.date_created.desc())
    return render_template('lotto/result_list.html', lottos=lotteries)

                


@lotto_bp.route('/admin/', methods=['GET', 'POST'])
def lotto_admin_create():

    if session['wallet'] != config("LOTTO_PUBLIC"):
        flash("Not Authorised")
        return redirect('/')

    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        contract_address = request.form['contract_address']
        lottery_type = request.form['lottery_type']
        lottery = Lottery(title, description, contract_address, lottery_type)
        db.session.add(lottery)
        db.session.commit()
        flash("New lottery created")

    return render_template('lotto/new.html')    


@lotto_bp.route('/admin/<int:lotto_id>', methods=['GET', 'PUT'])
def lotto_admin_edit(lotto_id):

    if session['wallet'] != config("LOTTO_PUBLIC"):
        flash("Not Authorised")
        return redirect('/')

    lottery = db.session.query(Lottery).filter_by(id=lotto_id).first()
    if request.method == 'PUT':
        lottery.title = request.form['title']
        lottery.description = request.form['description']
        lottery.contract_address = request.form['contract_address']
        lottery.lottery_type = request.form['lottery_type']
        db.session.commit()
    
    return render_template('lotto/edit.html', lotto=lottery)      
