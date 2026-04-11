from flask import Blueprint, request
from app.services.task_service import (
    get_all_tasks,
    add_task,
    update_task,
    delete_task
)

task_bp = Blueprint("tasks", __name__)


@task_bp.route("/tasks", methods=["GET"])
def get_tasks():
    return {"tasks": get_all_tasks()}


@task_bp.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    if not data or "title" not in data:
        return {"error": "Title is required"}, 400

    title = data["title"].strip()

    if not title:
        return {"error": "Title cannot be empty"}, 400

    new_task = add_task(title)
    return {"task": new_task}, 201


@task_bp.route("/tasks/<int:task_id>", methods=["PUT"])
def edit_task(task_id):
    data = request.get_json()

    if not data or "completed" not in data:
        return {"error": "Completed field is required"}, 400

    if not isinstance(data["completed"], bool):
        return {"error": "Completed must be true or false"}, 400

    updated_task = update_task(task_id, data["completed"])

    if not updated_task:
        return {"error": "Task not found"}, 404

    return {"task": updated_task}


@task_bp.route("/tasks/<int:task_id>", methods=["DELETE"])
def remove_task(task_id):
    deleted_task = delete_task(task_id)

    if not deleted_task:
        return {"error": "Task not found"}, 404

    return {"message": "Task deleted successfully"}
