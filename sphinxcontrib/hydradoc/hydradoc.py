#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives

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

    def run(self):
        env = self.state.document.settings.env

        data = u'self.content : {0}'.format(self.content)

        jdl_data = {}

        if 'file' in self.options.keys():
            hydra_filepath = os.path.join(env.srcdir, self.options['file'])
            with open(hydra_filepath) as f:
                jld_data = json.load(f)

                supportedClass = []
                for sc in jld_data['supportedClass']:
                    supportedClass.append(sc['@id'])

                data += u'Liste des classes declarees : {0}'.format(supportedClass)

        data += '"uri" option : {0}'.format(self.options['uri'])
        data += '"type" option : {0}'.format(self.options['type'])

        node = nodes.Text(data, data)

        return [node]


def setup(app):
    app.add_node(hydradoc)
    app.add_directive('hydradoc', hydradocDirective)
