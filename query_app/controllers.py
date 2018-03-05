#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Routes for app."""
from functools import partial
from itertools import chain

from bs4 import BeautifulSoup
from flask import render_template, request, flash
from requests import post, codes

from .forms import SPARQLform
from .flask_app import app
from .models import Graph, NAMESPACES


graph = Graph()


@app.template_filter('namespace')
def abbreviate(data):
    if data is None:
        return ""
    for abbr, ns in NAMESPACES.items():
        if str(ns) in data:
            n = data.replace(str(ns), "{}:".format(abbr))
            return '<a href="{url}" title="{n}">{n}</a>'.format(url=data, n=n)
    return data


@app.route("/", methods=["GET"])
def home_page():
    """Render the home page."""
    return render_template("home.html",
                           namespaces=NAMESPACES,
                           form=SPARQLform())


@app.route("/", methods=["POST"])
def result_page():
    """Render the query result."""
    form = SPARQLform()
    if not form.validate_on_submit():
        errors = chain.from_iterable(
            (
                map(partial("{}. {}".format, field.title()), errs) for
                field, errs in form.errors.items()
            )
        )
        flash("Invalid Query")
        for err in errors:
            flash(err)
        return home_page()
    query = request.form.get('query')
    try:
        results = graph.query(query)
    except Exception as e:
        flash("Could not run that query.")
        flash("RDFLIB Error: {}".format(e))
        sparql_validate(query)
        return home_page()
    return render_template("result.html",
                           namespaces=NAMESPACES,
                           form=SPARQLform(),
                           results=results)


def sparql_validate(query):
    prefix = "PREFIX {}: <{}>".format
    prefixes = "\n".join((prefix(ns, uri) for ns, uri in NAMESPACES.items()))
    query = prefixes + "\n\n" + query
    resp = post("http://sparql.org/validate/query", data=dict(query=query))
    if resp.status_code == codes.ok:
        soup = BeautifulSoup(resp.content.decode('utf-8'), "html.parser")
        pres = soup.find_all('pre')
        for p in pres:
            flash(p)
    else:
        flash("Unable to access query validation service.")
