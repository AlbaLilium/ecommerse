FROM python:3.11-slim

ENV PYTHONBUFFERED=1
WORKDIR /django-app
COPY ../requirements.txt /django-app
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt
COPY /backend /django-app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000 "]
# CMD  ["python -m uvicorn ecommerce.asgi:application --bind 0.0.0.0:8000"]
# EXPOSE ${PORT}