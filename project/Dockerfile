FROM python:3.7

WORKDIR /apps

COPY bboard /apps

COPY project /apps

COPY db.sqlite3 /apps

RUN pip install django==2.2.2

COPY . .

ENV PORT 8000

EXPOSE $PORT

VOLUME ["/app/db.sqlite3"]

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
