# recipe-app-api


docker-compose run --rm app sh -c "django-admin startproject app ."

docker-compose run --rm app sh -c "python manage.py startapp core"

docker-compose run --rm app sh -c "python manage.py makemigrations"
docker volume ls
docker volume rm recipe-app-api_dev-db-data
docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py migrate"

docker-compose run --rm app sh -c "python manage.py createsuperuser"

docker-compose run --rm app sh -c "python manage.py startapp user"

docker-compose run --rm app sh -c "python manage.py test  --verbosity=2"

https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#reversing-admin-urls
https://docs.djangoproject.com/en/3.2/topics/testing/tools/#overview-and-a-quick-example

https://stackoverflow.com/questions/25981703/pip-install-fails-with-connection-error-ssl-certificate-verify-failed-certi
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

pip install -r /tmp/requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com