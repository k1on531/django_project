run:
	docker run --rm -d --publish 8000:8000 -v db:/app/db.sqlite3 --name django_bb django_bb:env
run-dev:
	docker run --rm -d --publish 8000:8000 -v db:/app/db.sqlite3 -v /Users/rustamakbarov/django_project/project/bboard:/app -v /app/bboard --name django_bb django_bb:env
stop:
	docker stop django_bb