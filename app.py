from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

from backend.projects import projects_blueprint
from backend.users import users_blueprint
from backend.posts import posts_blueprint
from backend.messages import messages_blueprint
from backend.roles import roles_blueprint
from backend.applications import applications_blueprint
from backend.authentication import auth_blueprint

from backend.middlewares.authenticator import Authenticator

load_dotenv()

app = Flask(__name__)
app.url_map.strict_slashes = False

app.wsgi_app = Authenticator(app.wsgi_app)
CORS(app)

app.register_blueprint(projects_blueprint, url_prefix='/projects')
app.register_blueprint(users_blueprint, url_prefix='/users')
app.register_blueprint(posts_blueprint, url_prefix='/posts')
app.register_blueprint(messages_blueprint, url_prefix='/messages')
app.register_blueprint(roles_blueprint, url_prefix='/roles')
app.register_blueprint(applications_blueprint, url_prefix='/applications')
app.register_blueprint(auth_blueprint)


@app.route('/')
def api():
    return 'Guild API'
