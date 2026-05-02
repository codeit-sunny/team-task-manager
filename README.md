TEAM TASK MANAGER (Django Full-Stack Project)

📌 Project Description
A full-stack web application where users can create projects, assign tasks, and track progress with role-based access control (Admin / Member).

------------------------------------------------------------
🚀 FEATURES
------------------------------------------------------------
- User Authentication (Signup / Login / Logout)
- Role-based access (Admin & Member)
- Create / Update / Delete Projects
- Create / Assign Tasks to users
- Task status tracking (Pending / In Progress / Completed)
- Dashboard for tasks overview
- Overdue task tracking

------------------------------------------------------------
⚙️ TECHNOLOGY STACK
------------------------------------------------------------
Backend:
- Django 6.x
- Django REST Framework

Database:
- PostgreSQL (Production - Railway)
- SQLite (Local development)

Frontend:
- HTML
- CSS
- Bootstrap

Deployment:
- Railway Cloud Platform

------------------------------------------------------------
📦 INSTALLATION (LOCAL SETUP)
------------------------------------------------------------
1. Clone repository:
   git clone <your-repo-url>

2. Create virtual environment:
   python -m venv env
   env\Scripts\activate   (Windows)

3. Install dependencies:
   pip install -r requirements.txt

4. Run migrations:
   python manage.py migrate

5. Create superuser:
   python manage.py createsuperuser

6. Start server:
   python manage.py runserver

------------------------------------------------------------
🌐 LIVE DEPLOYMENT
------------------------------------------------------------
Deployed on Railway:
team-task-manager-production-a3cc.up.railway.app

------------------------------------------------------------
👨‍💻 DEVELOPER
------------------------------------------------------------
Developed by: Sunny

------------------------------------------------------------
📌 NOTES
------------------------------------------------------------
- Make sure DEBUG = False in production
- Use PostgreSQL on Railway
- Static files handled using Whitenoise
- Do not use SQLite in production
