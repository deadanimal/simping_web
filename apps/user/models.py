import requests
import json
import time
import os

from flask import Flask, render_template, flash, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from decouple import config

from apps import db

class Base(db.Model):

    __abstract__  = True

    id = db.Column(db.BigInteger, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


class Lottery(Base):

    __tablename__ = 'lottery'

    title = db.Column(db.String(256), nullable=False)
    description = db.Column(db.String(256), nullable=False)
    contract_address = db.Column(db.String(256), nullable=False)
    lottery_type = db.Column(db.String(16), nullable=False)
    ended = db.Column(db.Boolean, default=False)

    def __init__(self, title, description, contract_address, lottery_type):

        self.title = title
        self.description = description
        self.contract_address = contract_address
        self.lottery_type = lottery_type
