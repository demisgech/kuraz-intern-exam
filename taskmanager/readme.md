# Simple Task Manager API (Backend)

## Overview

This project is a simple Task Manager REST API built with Django and Django REST Framework.  
It allows users to:

- View a list of tasks
- Add new tasks
- Mark tasks as completed
- Delete tasks
- Filter tasks by completion status (completed vs. pending)
- Validate task title input (title must not be empty)

The project uses SQLite as the database engine by default.

---

## Features

- **CRUD API endpoints** for managing tasks
- **Filtering support** via query parameters: `?completed=true` or `?completed=false`
- **Validation** to ensure the task title is not empty
- Clear and descriptive JSON responses
- Basic API health check endpoint

---

## API Endpoints

| Method | Endpoint          | Description                             | Request Body                | Response                                        |
| ------ | ----------------- | --------------------------------------- | --------------------------- | ----------------------------------------------- |
| GET    | `/api/`           | API health check                        | None                        | `{ "message": "Task Manager API is running." }` |
| GET    | `/api/tasks/`     | Get all tasks (with optional filtering) | None                        | List of tasks (JSON array)                      |
| POST   | `/api/tasks/`     | Create a new task                       | `{ "title": "Task title" }` | Created task JSON                               |
| GET    | `/api/tasks/:id/` | Get task details by ID                  | None                        | Task JSON                                       |
| PUT    | `/api/tasks/:id/` | Mark a task as completed                | None                        | Confirmation message                            |
| DELETE | `/api/tasks/:id/` | Delete a task                           | None                        | Confirmation message                            |

---

## Filtering Tasks

You can filter tasks by their completion status by adding a query parameter to the GET `/api/tasks/` endpoint:

- `/api/tasks/?completed=true` — Returns only completed tasks
- `/api/tasks/?completed=false` — Returns only pending tasks

---

## Validation

When creating a new task (`POST /api/tasks/`), the `title` field:

- Must not be empty or contain only whitespace
- If validation fails, the API responds with status 400 and a descriptive error message.

---

## Setup Instructions

Follow these steps to get the project running locally:

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd <project-folder>
   ```
