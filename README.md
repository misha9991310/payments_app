Запуск
git https://github.com/misha9991310/payments_app.git

cd paymentsapp

python -m venv env

.\venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

Запуск Docker

git https://github.com/misha9991310/payments_app.git

cd paymentsapp

docker-compose up -d

Остановка docker:

docker-compose stop

Главная страница: http://localhost:8000/


