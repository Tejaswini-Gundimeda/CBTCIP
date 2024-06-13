import React, { useState } from 'react';
import './App.css';

const ToDoApp = () => {
    const [tasks, setTasks] = useState([]);
    const [completedTasks, setCompletedTasks] = useState([]);
    const [taskInput, setTaskInput] = useState('');

    const addTask = () => {
        if (taskInput.trim() === '') return;

        const newTask = {
            text: taskInput,
            addedAt: new Date().toLocaleString(),
        };

        setTasks([...tasks, newTask]);
        setTaskInput('');
    };

    const completeTask = (index) => {
        const task = tasks[index];
        task.completedAt = new Date().toLocaleString();

        setTasks(tasks.filter((_, i) => i !== index));
        setCompletedTasks([...completedTasks, task]);
    };

    const switchTheme = (theme) => {
        document.body.className = theme === 'light' ? 'light-theme' : 'dark-theme';
    };

    return (
        <div className="container">
            <button onClick={() => switchTheme('light')}>Light Theme</button>
            <button onClick={() => switchTheme('dark')}>Dark Theme</button>
            <h1>To-Do List</h1>
            <div className="input-group">
                <input
                    type="text"
                    value={taskInput}
                    onChange={(e) => setTaskInput(e.target.value)}
                    placeholder="Add a new task..."
                />
                <button onClick={addTask}>Add Task</button>
            </div>
            <h2>Tasks</h2>
            <ul>
                {tasks.map((task, index) => (
                    <li key={index}>
                        {task.text} <span className="timestamp">[Added: {task.addedAt}]</span>
                        <button onClick={() => completeTask(index)}>Complete</button>
                    </li>
                ))}
            </ul>
            <h2>Completed Tasks</h2>
            <ul>
                {completedTasks.map((task, index) => (
                    <li key={index} className="completed">
                        {task.text} <span className="timestamp">[Added: {task.addedAt}] [Completed: {task.completedAt}]</span>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default ToDoApp;
