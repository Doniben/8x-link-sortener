# 8x-link-sortener

8x.social is a Link Shortener created to provide a tool for various social, cultural, political, and educational institutions.

## Getting Started

### Prerequisites

Make sure you have Python 3.8 or later installed.

### Installation

```bash
# Create and activate a virtual environment
python -m venv .env
source .env/bin/activate

# Navigate to the project directory
cd EightX

# Install dependencies
pip install -r requirements.txt
```

### Database Setup

```bash
# Apply database migrations
python manage.py makemigrations core
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic
```

### Run the Application

```bash 
# Install Gunicorn (if not installed)
pip install gunicorn

# Start the application
gunicorn EightX.wsgi:application --bind=0.0.0.0:8000
```

### configuración supervisor en local
sudo apt install supervisor

sudo emacs /etc/supervisor/conf.d/8x.social.conf


```
[program:8x-social]
command=/Users/doniben/Documents/PROGRAMMING-GIT/8x-link-sortener-1/entorno/.env/bin/gunicorn EightX.wsgi:application --bind=0.0.0.0:8000
directory=/Users/doniben/Documents/PROGRAMMING-GIT/8x-link-sortener-1/entorno/EightX
user=production
autostart=true
autorestart=true
stdout_logfile=/var/log/8x-social.log
stderr_logfile=/var/log/8x-social-error.log
```

``` [program:8x.social]
command = gunicorn EightX.wsgi:application --bind=0.0.0.0:8000
directory = /var/www/8x.social/8x-link-sortener/entorno/EightX
user = production

```

#### En mac local
brew install supervisor
brew services start supervisor
supervisorctl reread
supervisorctl update
supervisorctl restart 8x-social

#### En linux de producción

sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start dominio.com

### Colour Palette:

#FFFFFF - White

#FDBB34 - Mustard

#1E4132 - Green

### Resources used:

Illustrations - https://undraw.co

Colour Palette - https://dribbble.com/shots/7074188-Food-App-IOS