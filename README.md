

# 8x-link-sortener
8x.social is a Link Shortener created to give a tool for different social, cultural, politic and educational institutions.

### Instala geopandas y hashids
python3.8 -m pip install geopandas hashids

### Crea y activa el entorno virtual
python -m venv .env
source .env/bin/activate

### Instala las dependencias
pip install -r requirements.txt

### Instala las dependencias

cd EightX

python manage.py makemigrations core

python manage.py migrate

python manage.py createsuperuser

python manage.py collectstatic

pip install gunicorn

pip run gunicorn EightX.wsgi:application --bind=0.0.0.0:8000

sudo apt install supervisor

sudo emacs /etc/supervisor/conf.d/8x.social.conf

#### configuración supervisor en local

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