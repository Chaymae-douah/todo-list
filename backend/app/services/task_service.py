from app.config.db import db
from app.models.task import Task


def get_all_tasks():
    tasks = Task.query.order_by(Task.id.asc()).all()
    return [task.to_dict() for task in tasks]


def add_task(title):
    new_task = Task(title=title, completed=False)
    db.session.add(new_task)
    db.session.commit()
    return new_task.to_dict()


def update_task(task_id, completed):
    task = db.session.get(Task, task_id)
    if not task:
        return None

    task.completed = completed
    db.session.commit()
    return task.to_dict()


def delete_task(task_id):
    task = db.session.get(Task, task_id)
    if not task:
        return None

    db.session.delete(task)
    db.session.commit()
    return task.to_dict()
