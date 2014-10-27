from docutils import nodes
from docutils.parsers.rst import Directive


class bonjourlemonde(nodes.Element):
    pass


class bonjourlemondeDirective(Directive):
    has_content = True

    def run(self):
        data = 'bonjour le monde %s  avec les options : %s ' \
            % (str(self.content[0]), self.content)
        node = nodes.Text(data, data)
        return [node]


def setup(app):
    app.add_node(bonjourlemonde)
    app.add_directive('bonjourlemonde', bonjourlemondeDirective)
