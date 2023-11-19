import gunicorn.app.base
from six import iteritems
from app import app  # Import your Flask app from app.py

# Define Gunicorn options here
options = {
    'bind': '0.0.0.0:7000',
    'workers': 1  # You can adjust the number of workers as needed
}

class StandaloneApplication(gunicorn.app.base.BaseApplication):
    def __init__(self, app, options=None):
        self.application = app
        self.options = options or {}
        super(StandaloneApplication, self).__init__()

    def load_config(self):
        config = {
            key: value for key, value in iteritems(self.options)
            if key in self.cfg.settings and value is not None
        }
        for key, value in iteritems(config):
            self.cfg.set(key, value)

    def load(self):
        return self.application

if __name__ == '__main__':
    StandaloneApplication(app, options).run()