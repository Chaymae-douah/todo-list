import React from "react";

function TaskItem({ task, onToggleTask, onDeleteTask }) {
  return (
    <li>
      <span>
        {task.title} - {task.completed ? "Done" : "Pending"}
      </span>

      <button onClick={() => onToggleTask(task.id, task.completed)}>
        {task.completed ? "Mark as Pending" : "Mark as Done"}
      </button>

      <button onClick={() => onDeleteTask(task.id)}>
        Delete
      </button>
    </li>
  );
}

export default TaskItem;
