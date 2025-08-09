# ACTIVITYPURI

## Features
- Create tweets with text and optional image
- Bad word filter: "shit", "fuck", "bobo"
- Admin view for tweets

## Installation
```bash
git clone https://github.com/Japuri/ACTIVITYPURIFORM.git
cd ACTIVITYPURI
#create venv
python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

