# Job Board Platform

A backend system for managing job listings, employers, candidates, and applications, built with Django, Django REST Framework, and PostgreSQL. Employers can post jobs, candidates can search jobs, upload resumes, and apply, and both sides can track applications.

## Features

- View a list of all job postings
- Search/filter jobs (location, job type, keyword, salary)
- View details of a specific job
- Post a job (employer)
- Upload a resume (candidate)
- Apply for a job (candidate)
- View your own applications
- View applicants for your job (employer)
- Update application status (employer)
- View notifications (employer)

## Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL

## Setup

Clone the repository and move into the folder:
```
git clone <repo-url>
cd CodeAlpha_JobBoardPlatform
```

Create and activate a virtual environment:
```
python -m venv venv
venv\Scripts\Activate.ps1
```

Install dependencies:
```
pip install -r requirements.txt
```

Create a `.env` file in the project root (see `.env.example`) with your PostgreSQL credentials:
```
SECRET_KEY=your-secret-key
DEBUG=True
DB_NAME=job_board_db
DB_USER=your_db_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

Run migrations:
```
python manage.py migrate
```

Run the app:
```
python manage.py runserver
```

The app will start on `http://localhost:8000`

## API Usage (In Progress)

All endpoints require authentication (Basic Auth — logged-in user), unless noted otherwise.

| Method | Endpoint | Description | Status |
|--------|----------|-------------|--------|
| GET | /api/jobs/ | Get a list of all jobs (supports filters: location, job_type, keyword, min_salary) | Not done |
| GET | /api/jobs/<id>/ | Get details of a single job | Not done |
| POST | /api/jobs/ | Post a new job (employer only) | Not done |
| PUT/PATCH | /api/jobs/<id>/ | Update your own job (employer only) | Not done |
| DELETE | /api/jobs/<id>/ | Delete your own job (employer only) | Not done |
| POST | /api/resumes/ | Upload a resume (candidate only) | Not done |
| POST | /api/applications/ | Apply for a job (send job ID and resume ID; candidate linked automatically) | Not done |
| GET | /api/applications/my/ | View your own applications (candidate) | Not done |
| GET | /api/jobs/<id>/applications/ | View applicants for your job (employer only) | Not done |
| PATCH | /api/applications/<id>/status/ | Update an application's status (employer only) | Not done |
| GET | /api/notifications/ | View your notifications (employer only) | Not done |

_This table will be updated to "Done" as each endpoint is built and tested in Postman._

## Author

Kainat Rasheed — CodeAlpha Backend Development Intern