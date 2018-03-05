import os

from rdflib.namespace import Namespace, RDF, RDFS, OWL, XSD
from rdflib.namespace import SKOS, DOAP, FOAF, DC, DCTERMS

DEBUG = True

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SECRET_KEY = os.urandom(64)

# Prefixes and namespaces to use.
NAMESPACES = dict(rdf=RDF,
                  rdfs=RDFS,
                  owl=OWL,
                  xsd=XSD,
                  skos=SKOS,
                  doap=DOAP,
                  foaf=FOAF,
                  dc=DC,
                  dcterms=DCTERMS,
                  swivt=Namespace("http://semantic-mediawiki.org/swivt/1.0#"),
                  pbmfoaf=Namespace("http://www.paulbrownmagic.com/foaf.rdf"),
                  )

# Path to Directory containing RDF data.
RDF_DIR = os.path.join(BASE_DIR, "rdf")

# URLs from which to download RDF data.
RDF_URLS = ["http://www.paulbrownmagic.com/foaf.rdf",
            ]
