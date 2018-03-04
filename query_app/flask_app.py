#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Initialise Flask app."""

from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.config.from_object('config')
