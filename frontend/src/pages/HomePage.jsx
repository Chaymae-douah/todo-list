import React, { useEffect, useState } from "react";
import {
  fetchTasks,
  createTask,
  updateTask,
  deleteTask
} from "../services/api";
import TaskForm from "../components/TaskForm";
import TaskList from "../components/TaskList";

function HomePage() {
  const [tasks, setTasks] = useState([]);
  const [title, setTitle] = useState("");
  const [error, setError] = useState("");

  useEffect(() => {
    loadTasks();
  }, []);

  async function loadTasks() {
    try {
      setError("");
      const data = await fetchTasks();
      setTasks(data.tasks);
    } catch (error) {
      console.error("Error loading tasks:", error);
      setError("Unable to load tasks.");
    }
  }

  async function handleSubmit(event) {
    event.preventDefault();

    if (!title.trim()) {
      return;
    }

    try {
      setError("");
      await createTask(title);
      setTitle("");
      await loadTasks();
    } catch (error) {
      console.error("Error creating task:", error);
      setError("Unable to create task.");
    }
  }

  async function handleToggleTask(taskId, currentStatus) {
    try {
      setError("");
      await updateTask(taskId, !currentStatus);
      await loadTasks();
    } catch (error) {
      console.error("Error updating task:", error);
      setError("Unable to update task.");
    }
  }

  async function handleDeleteTask(taskId) {
    try {
      setError("");
      await deleteTask(taskId);
      await loadTasks();
    } catch (error) {
      console.error("Error deleting task:", error);
      setError("Unable to delete task.");
    }
  }

  return (
    <div>
      <h1>Todo App</h1>

      <TaskForm
        title={title}
        setTitle={setTitle}
        onSubmit={handleSubmit}
      />

      {error && <p>{error}</p>}

      <TaskList
        tasks={tasks}
        onToggleTask={handleToggleTask}
        onDeleteTask={handleDeleteTask}
      />
    </div>
  );
}

export default HomePage;
