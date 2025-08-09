# ACTIVITYPURI

## Features
- Create tweets with text and optional image
- Bad word filter: "shit", "fuck", "bobo"
- Admin view for tweets

## Installation
```bash
git clone https://github.com/YOURUSERNAME/ACTIVITYPURI.git
cd ACTIVITYPURI
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

# ACTIVITYPURIFORM
