from flask import *
from app import models, db

teams = Blueprint('teams', __name__, template_folder='templates')


@teams.route('/teams/create', methods=['GET', 'POST'])
def create_route():
    """
        Create a team
    """
    if request.method == 'GET':
        return render_template('create_team.html')
    else:
        team = models.Team(name=request.form['name'],
                           grade=request.form['grade'],
                           member1=request.form['member1'],
                           member2=request.form['member2'],
                           member3=request.form['member3'],
                           member4=request.form['member4'])
        db.session.add(team)
        db.session.commit()
        print(team)
        return redirect(url_for('index.home'))

@teams.route('/teams/finish', methods=['GET'])
def select_finish_route():
    teams = models.Team.query.all()
    options = {
        'teams': teams,
    }
    return render_template('select_team.html', **options)

@teams.route('/teams/finish/<int:team_id>', methods=['GET', 'POST'])
def finish_route(team_id):

    if request.method == 'GET':
        tasks = models.Task.query.all()
        team = models.Team.query.get(team_id)
        options = {
            'tasks': tasks,
            'team': team,
        }
        return render_template('finish_task.html', **options)

    else:
        task = models.Task.query.get(request.form.get('task_id'))
        team = models.Team.query.get(team_id)
        if task in team.tasks:
            return redirect(url_for('teams.display_route'))
        team.tasks.append(task)
        db.session.commit()
        return redirect(url_for('teams.display_route'))



@teams.route('/teams/display', methods=['GET'])
def display_route():
    """
        Displays all the teams and their tasks
    """
    teams = models.Team.query.all()
    options = {
        'teams': teams,
    }

    return render_template('team_display.html', **options)
