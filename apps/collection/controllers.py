# Import flask dependencies
from flask import Blueprint, redirect, request, render_template, jsonify, flash, abort, session
from web3.auto import w3
from eth_account.messages import encode_defunct
from web3 import Web3
from web3.middleware import geth_poa_middleware
import sqlalchemy
import time
from decouple import config

from apps.collection.models import Collection
from apps import db

collection_bp = Blueprint('collection', __name__, url_prefix='/collection')


@collection_bp.route('/', methods=['GET'])
def collection_list():
    collection = db.session.query(Collection).order_by(Collection.date_created.desc())
    return render_template('collection/list.html', collections=collection)



@collection_bp.route('/<int:collection_id>', methods=['GET'])
def collection_detail(collection_id):
    collection = db.session.query(Collection).filter_by(id=collection_id).first()
    if collection:
        return render_template('collection/detail.html', collection=collection)    
    else:
        return render_template('404.html')   

