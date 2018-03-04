#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Forms for use in app."""

from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField
from wtforms.validators import DataRequired


class SPARQLform(FlaskForm):
    """Form to accept SPARQL query."""

    query = TextAreaField('Query', validators=[DataRequired()])
