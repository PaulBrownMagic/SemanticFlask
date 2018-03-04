import os

from rdflib.namespace import Namespace, RDF, RDFS, OWL, XSD
# Other optional namespaces predefined
# from rdflib.namespace import SKOS, DOAP, FOAF, DC, DCTERMS

DEBUG = True

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SECRET_KEY = os.urandom(64)

# Prefixes and namespaces to use.
NAMESPACES = dict(swivt=Namespace("http://semantic-mediawiki.org/swivt/1.0#"),
                  wiki=Namespace('http://www.skybrary.aero/index.php/Special:URIResolver/'),
                  property=Namespace('http://www.skybrary.aero/index.php/Special:URIResolver/Property-3A'),
                  wikiurl=Namespace('https://www.skybrary.aero/index.php/'),
                  rdf=RDF,
                  rdfs=RDFS,
                  owl=OWL,
                  xsd=XSD)

# Path to Directory containing RDF data.
RDF_DIR = os.path.join(BASE_DIR, "rdf")

# URLs from which to download RDF data.
RDF_URLS = ["http://www.paulbrownmagic.com/foaf.rdf",
            ]
