class Plugin(object):
    def __init__(self, *args, **kwargs):
        """Initializes the plugin."""
        self.args = args
        self.kwargs = kwargs

    def get_header(self, jinja_env):
        tmp = jinja_env.get_template('plugin_{}_header.js'.format(self.name))
        return tmp.render()

    def get_body(self, jinja_env):
        body = jinja_env.get_template('plugin_{}_body.js'.format(self.name))
        return body.render()


class Terminator(Plugin):
    name = "terminator"

class FileLayer(Plugin):
    name = "filelayer"

