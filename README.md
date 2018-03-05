# Semantic Web Flask

This application is for local querying of RDF data. You can drop your files into
the rdf directory, run the application, open up a browser and SPARQL query your
data.

## Requirements

Requirements are all
Python3.4+ and can be installed with pipenv. If you
don't have pipenv yet, install that first. The last command here activates your
virtual environment. The top-level dependencies are Flask, Flask-WTF,
Flask-Bootstrap, BeautifulSoup4, RDFLib and requests.

```
pip3 install pipenv
pipenv --three install
pipenv shell
```

## Running the app
The main entry point to the application is `run.py`. Before you run the app,
you should put some RDF files into the `rdf` directory. This path to this
directory can be configured in `config.py` if you wish to change it. The app
will search all sub-directories of the rdf directory for data and it will
injest them all.

```
python run.py
```

### Note
Be aware that currently all the data is loaded into memory with RDFLib, this
operation takes a second so keep an eye on your command line to know when
the application is ready to use. The advantage of this is the application is
pure Python, no need for an external data base and once the data is loaded it
is adequately fast. This is not a production solution, just a local app.

## Querying the data

In a browser go to <http://127.0.0.1:5000>, this is the home page and query page.
You can input SPARQL queries here, some prefixes have been predefined for you.
More namespaces can be defined in `config.py`, you should define all the prefixes
for your data here so that invalid SPARQL queries can be properly debugged.

### Note
There is a limit to how many triples a query can return, this is only a little,
local Python application, not a production system. Beware, it is possible to crash
the application with a query that'll return many, many triples.


### Example queries:
This will return all the instances (?subject) of all the classes (?object).

```sparql
SELECT ?subject ?object
WHERE {
    ?subject rdf:type ?object .
}
```

The default config file is set to injest my foaf.rdf file, which is
hosted online. You can run queries on the data using the foaf prefix.
In this query we also use `a`, which is equivalent to `rdf:type`.

```sparql
SELECT ?person ?title ?name ?blog
WHERE {
    ?person a foaf:Person.
    ?person foaf:title ?title.
    ?person foaf:name ?name.
    ?person foaf:weblog ?blog.
}
```
