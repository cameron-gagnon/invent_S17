from flask import *

from app import models

index = Blueprint('index', __name__, template_folder='templates')

@index.route('/')
@index.route('/index')
def home():
    tasks = models.Task.query.all()

    options = {
        'tasks': tasks,
    }
    return render_template('index.html', **options)
