pasos para despliegue

1 - python -m venv venv
2 - source venv/scripts/activate
3 - pip install -r requirements.txt
4 - crear .env
    DJANGO_SECRET=
    CLOUDINARY_CLOUD_NAME=
    CLOUDINARY_API_KEY=
    CLOUDINARY_API_SECRET=
5 - python manage.py runserver