#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docutils import nodes
from docutils.parsers.rst import Directive

import os
import json

class bonjourlemonde(nodes.Element):
    pass


class bonjourlemondeDirective(Directive):
    has_content = True

    def run(self):
        env = self.state.document.settings.env

        jdl_data = {}
        # TODO find 'source' path to have the right path to the file
        hydra_filepath = '{0}/{1}'.format(os.getcwd(), self.content[0])
        with open(hydra_filepath) as f:
            jld_data = json.load(f)

            supportedClass = []
            for sc in jld_data['supportedClass']:
                supportedClass.append(sc['@id'])

            data = u'Liste des classes declarees {0} : \
                     avec les options {1}'.format(supportedClass,
                                                  self.content)

        #data = 'env : {0}'.format(dir(env))

        node = nodes.Text(data, data)
        return [node]


def setup(app):
    app.add_node(bonjourlemonde)
    app.add_directive('bonjourlemonde', bonjourlemondeDirective)
