# sigc
Sistema de gestao de cheques devolvidos

commands:
1.docker-compose run --rm app sh -c "celery -A app worker -l info"
2.docker-compose run --rm app sh -c "celery -A app beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler

