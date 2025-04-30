### Task manager

### Hexlet tests and linter status:
[![Actions Status](https://github.com/Marvv1ne/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Marvv1ne/python-project-52/actions)

### PythonCI tests and linter status:
[![PythonCI](https://github.com/Marvv1ne/python-project-52/actions/workflows/pythonCI.yml/badge.svg?branch=main)](https://github.com/Marvv1ne/python-project-52/actions/workflows/pythonCI.yml)

### SonarQube quality gate status:
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Marvv1ne_python-project-52&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=Marvv1ne_python-project-52)


#### --> [Project demonstration](https://python-project-52-1-5wvv.onrender.com) <--

### Description
A task management web application built with Python and Django framework. It allows you to set tasks, assign performers and change their statuses. Registration and authentication are required to work with the system.

## Technologies Used
- Python 3.12
- Django 4.2
- PostgreSQL
- HTML/Bootstrap for frontend

## Local Setup
**After cloning the repository**

1. **Install dependencies:**
```
make sync
```
2. **Build tables in DB (default database is sqlite):**
```
make migrate
```
3. **Run server in developer mode:**
```
make runserver
```