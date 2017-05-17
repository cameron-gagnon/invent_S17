from flask import *

from app import models, db

tasks = Blueprint('tasks', __name__, template_folder='templates')

@tasks.route('/tasks/create', methods=['GET', 'POST'])
def create_route():
    """
        Create a task
    """
    if request.method == 'GET':
        return render_template('create_task.html')
    else:
        task = models.Task(name=request.form['name'],
                           type=request.form['type'],
                           value=request.form['value'],
                           description=request.form['description'])

        print(task)

        db.session.add(task)
        db.session.commit()

        return redirect(url_for('index.home'))

@tasks.route('/tasks/edit/<int:id>', methods=['GET', 'POST'])
def edit_task(id):
    """
        Update a task for a team
    """
    task = models.Task.query.get(id)
    if request.method == 'GET':
        options = {
            'task': task,
            'arduinoChecked': "Checked" if task.type == 'Arduino' else '',
            'pythonChecked': "Checked" if task.type == 'Python' else '',
            'modelChecked': "Checked" if task.type == '3D Modeling' else '',
        }
        return render_template('edit_task.html', **options)
    else:
        if not session.get('username'):
            return redirect(url_for('login_api.login'))

        task.name = request.form['name']
        task.type = request.form['type']
        task.description = request.form['description']
        task.value = request.form['value']
        db.session.commit()

        return redirect(url_for('index.home'))
