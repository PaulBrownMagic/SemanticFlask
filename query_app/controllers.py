#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Routes for app."""
from bs4 import BeautifulSoup
from flask import render_template, request, flash
from requests import post, codes

from .forms import SPARQLform
from .flask_app import app
from .models import Graph, NAMESPACES


graph = Graph()


@app.template_filter('namespace')
def abbreviate(url):
    for abbr, ns in NAMESPACES.items():
        if str(ns) in url:
            return url.replace(str(ns), f"{abbr}:")
    return url


@app.route("/", methods=["GET"])
def home_page():
    """Render the home page."""
    return render_template("home.html",
                           namespaces=NAMESPACES,
                           form=SPARQLform())


@app.route("/", methods=["POST"])
def result_page():
    """Render the query result."""
    if not SPARQLform().validate_on_submit():
        flash("Invalid Query")
        return home_page()
    query = request.form.get('query')
    try:
        results = graph.query(query)
    except Exception as e:
        flash("Could not run that query.")
        flash(f"RDFLIB Error: {e}")
        sparql_validate(query)
        return home_page()
    return render_template("result.html",
                           namespaces=NAMESPACES,
                           form=SPARQLform(),
                           results=results)


def sparql_validate(query):
    prefixes = "\n".join((f"PREFIX {ns}: <{uri}>" for ns, uri in NAMESPACES.items()))
    query = prefixes + "\n\n" + query
    data = {"query": query}
    resp = post("http://sparql.org/validate/query", data=data)
    if resp.status_code == codes.ok:
        soup = BeautifulSoup(resp.content.decode('utf-8'), "html.parser")
        pres = soup.find_all('pre')
        for p in pres:
            flash(p)
