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


class User(Base):

    __tablename__ = 'user'

    username = db.Column(db.String(256), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_country_code = db.Column(db.Integer(), nullable=True)
    phone_number = db.Column(db.Integer(), nullable=True)

    def __init__(self, username, email):

        self.username = username
        self.email = email
