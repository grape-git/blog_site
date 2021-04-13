FROM python:3.9.0

WORKDIR /home/

RUN echo "testing1234"

RUN git clone https://github.com/grape-git/blog_site.git

WORKDIR /home/blog_site/

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=blog.settings.deploy && python manage.py migrate --settings=blog.settings.deploy && gunicorn blog.wsgi --env DJANGO_SETTINGS_MODULE=blog.settings.deploy --bind 0.0.0.0:8000"]