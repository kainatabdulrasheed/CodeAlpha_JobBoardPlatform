# Job Board Platform

A backend API for a job board platform built with Django REST Framework, where employers can post jobs and candidates can search, apply, and track their applications.

## Features

- Employer and Candidate profiles linked to Django's built-in User model
- Employers can post, update, and delete job listings
- Candidates can search jobs by location, job type, and keyword
- Resume upload (file upload support)
- Candidates can apply to jobs and track their application status
- Employers can view applicants per job and update application status
- Employers receive notifications when a candidate applies
- Django admin panel for managing all data (jobs, applications, users)

## Tech Stack

- **Backend:** Django, Django REST Framework
- **Database:** PostgreSQL
- **Authentication:** Basic Authentication
- **File handling:** Django's FileField (resume uploads)

## Project Structure

- `jobs/` — Employer and Job models, views, serializers
- `applications/` — Candidate, Resume, Application, and Notification models, views, serializers

## Setup Instructions

1. Clone the repo and create a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root:
   ```
   SECRET_KEY=your-secret-key
   DEBUG=True
   DB_NAME=job_board_db
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=localhost
   DB_PORT=5432
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (for admin panel access):
   ```bash
   python manage.py createsuperuser
   ```

6. Run the server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

| Method | Endpoint | Description | Auth |
|--------|----------|--------------|------|
| GET | `/api/jobs/` | List active jobs (supports `?location=`, `?job_type=`, `?keyword=` filters) | Any logged-in user |
| GET | `/api/jobs/<id>/` | Job detail | Any logged-in user |
| POST | `/api/jobs/create/` | Post a new job | Employer |
| PATCH | `/api/jobs/<id>/manage/` | Update a job | Employer (own job) |
| DELETE | `/api/jobs/<id>/manage/` | Delete a job | Employer (own job) |
| POST | `/api/resumes/` | Upload a resume (form-data) | Candidate |
| POST | `/api/applications/` | Apply to a job | Candidate |
| GET | `/api/applications/my/` | View own applications | Candidate |
| GET | `/api/jobs/<id>/applications/` | View applicants for a job | Employer (own job) |
| PATCH | `/api/applications/<id>/status/` | Update application status | Employer (own job) |
| GET | `/api/notifications/` | View notifications | Employer |

## Authentication

This API uses **Basic Authentication**. Include your username and password with each request (Postman: Authorization tab → Basic Auth).

## Testing

All endpoints were tested manually using Postman, including:
- Core flow: job posting, searching, resume upload, applying, status updates
- Permission checks: candidates cannot post jobs, employers cannot manage other employers' jobs or applicants

## Admin Panel

All models are registered in Django admin (`/admin/`) with list display, filters, and search — used for managing test data and users.

## Author

Kainat Rasheed — CodeAlpha Backend Development Intern