#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives
from docutils.statemachine import ViewList
from sphinx.util.nodes import nested_parse_with_titles

import os
import json

class hydradoc(nodes.Element):
    pass


class hydradocDirective(Directive):
    has_content = True
    option_spec = {
            'file': directives.unchanged,
            'uri': directives.unchanged,
            'type': directives.unchanged,
            }

    # dirty
    def supportedProperty2rst(self, json_segment):
        yield 'Property'
        yield '~~~~~~~~'
        for prop in json_segment:
            yield '* {0}'.format(prop)
        yield ""

    # dirty
    def json2rst(self, json_data):
        yield 'Service'
        yield '======='
        supportedClass = []
        for sc in json_data['supportedClass']:
            if 'hydra:title' in sc.keys():
                title = sc['hydra:title']
                yield "{0}".format(title)
                yield "_"*len(title)
            if 'hydra:description' in sc.keys():
                yield "Description : {0}".format(sc['hydra:description'])
            yield ""
            supportedClass.append(sc['@id'])
            yield "* `{0} : <{1}>`_".format(supportedClass[0], supportedClass[0])
            yield ""
            if 'supportedProperty' in sc.keys():
                for properties in self.supportedProperty2rst(sc['supportedProperty']):
                    yield properties


    def run(self):
        env = self.state.document.settings.env
        nodeRoot = nodes.section()
        nodeRoot.document = self.state.document

        jdl_data = {}
        result = ViewList()

        if 'file' in self.options.keys():
            hydra_filepath = os.path.join(env.srcdir, self.options['file'])
            with open(hydra_filepath) as f:
                jld_data = json.load(f)
            for ligne in self.json2rst(jld_data):
                result.append(ligne, '<hydradoc>')

        nested_parse_with_titles(self.state, result, nodeRoot)
        return nodeRoot.children


def setup(app):
    app.add_node(hydradoc)
    app.add_directive('hydradoc', hydradocDirective)
