

# 8x-link-sortener
Link Shortener based on a course from Udemy

python3.8 -m pip install geopandas 

pip install hashids

source 8x-link-sortener/entorno/bin/activate

python manage.py makemigrations core

python manage.py migrate

python manage.py createsuperuser

pipenv install gunicorn

pipenv run gunicorn EightX.wsgi:application --bind=0.0.0.0:8000

sudo apt install supervisor

sudo emacs /etc/supervisor/conf.d/8x.social.conf

``` [program:8x.social]
command = gunicorn EightX.wsgi:application --bind=0.0.0.0:8000
directory = /var/www/8x.social/8x-link-sortener/entorno/EightX
user = production

```

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