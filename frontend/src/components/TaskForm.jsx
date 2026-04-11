import React from "react";

function TaskForm({ title, setTitle, onSubmit }) {
  return (
    <form onSubmit={onSubmit}>
      <input
        type="text"
        placeholder="Enter a task"
        value={title}
        onChange={(event) => setTitle(event.target.value)}
      />
      <button type="submit">Add Task</button>
    </form>
  );
}

export default TaskForm;
