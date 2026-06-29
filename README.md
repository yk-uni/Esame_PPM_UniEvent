# UniEvent

## Project Description

UniEvent is a web application developed with Django for managing university events.

The application allows organizers to create and manage events, while attendees can browse available events and register for them.

This project was developed for the **Progettazione e Produzione Multimediale (PPM)** course.

---

## Features

* User authentication (Login / Logout)
* Custom User model
* Two user roles:

  * Organizer
  * Attendee
* Create events
* Edit events
* Delete events
* Event registration
* Personal dashboard
* Bootstrap 5 responsive interface
* Django Admin panel

---

## Technologies

* Python 3
* Django
* SQLite
* Bootstrap 5
* HTML5
* CSS3

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yk.uni/Esame_PPM_UniEvent.git
```

Move into the project folder:

```bash
cd Esame_PPM_UniEvent
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment (Windows):

```bash
venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

---

## Demo Users

### Admin

Username:

```
admin_demo
```

Password:

```
Admin2026!
```

### Organizer

Username:

```
organizer_demo
```

Password:

```
Organizer2026!
```

### Attendee

Username:

```
attendee_demo
```

Password:

```
Attendee2026!
```

---

## Project Structure

```
accounts/
config/
events/
templates/
manage.py
requirements.txt
README.md
```

---

## Framework

Django

---

## Author

Yash Kumar
Università degli Studi di Firenze
