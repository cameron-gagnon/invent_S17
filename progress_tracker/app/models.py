from app import db

task_identifier = db.Table('task_identifier',
    db.Column('task_id', db.Integer, db.ForeignKey('task.id')),
    db.Column('team_id', db.Integer, db.ForeignKey('team.id'))
)

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    tasks = db.relationship('Task', secondary=task_identifier)
    grade = db.Column(db.String(5))
    member1 = db.Column(db.Text)
    member2 = db.Column(db.Text)
    member3 = db.Column(db.Text)
    member4 = db.Column(db.Text)

    def __repr__(self):
        return 'Team: {}.\n\tGrade: {}\n\tTasks: {}\n\tMembers: {}, {}, {}, {}'.format(
                self.name, self.grade, self.tasks, self.member1,
                self.member2, self.member3, self.member4)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    type = db.Column(db.String(80))
    value = db.Column(db.Integer)
    description = db.Column(db.Text)

    def __repr__(self):
        return 'Task name: {}.\n\tType: {}\n\tDescription: {}'.format(
                self.name, self.type, self.description)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __repr__(self):
        return 'Username: {}.\n\tPassword: {}'.format(
                self.username, self.password)
