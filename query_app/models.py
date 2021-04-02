#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Automatic injesting of data to rdflib.Graph."""

from itertools import chain
import os
from pathlib import Path

import rdflib

from config import RDF_DIR, NAMESPACES, RDF_URLS, PARSERS


def get_files(rootdirfiles):
    """Turn the results of os.walk into usable paths."""
    return (os.path.join(rootdirfiles[0], f) for f in rootdirfiles[2])


def is_rdf_file(filename):
    """Only injests rdf files."""
    return filename.suffix in PARSERS.keys()


class Graph(rdflib.Graph):
    """Interface to rdflib graph."""

    def __init__(self, *args, **kwargs):
        """Injest Data on initialisation."""
        super().__init__(*args, **kwargs)
        for ns, uri in NAMESPACES.items():
            self.bind(ns, uri)
        files_in_dir = map(
            Path, chain.from_iterable(map(get_files, os.walk(RDF_DIR)))
        )
        for rdf_file in filter(is_rdf_file, files_in_dir):
            print("Parsing: ", rdf_file)
            self.parse(str(rdf_file), format=PARSERS[rdf_file.suffix])
        for url in RDF_URLS:
            print("Parsing: ", url)
            self.parse(url)
        print("Parsing Complete")
