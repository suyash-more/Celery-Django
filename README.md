

# **Configure your backend for Email Sending**

Command Reference
***

## **Install celery**
```bash
    $ pip install celery
```
## **Install flower**
```bash
    $ pip install flower
```

## **Install beat**
```bash
    $ pip install django-celery-beat
```
## **Install RabbitMQ (Ubuntu Linux 20.04LTS)**
```bash
    $ sudo apt-get install rabbitmq-server
```
## **Run Celery**
```bash
    $ celery -A NAMEOFINSTANCE worker --loglevel=info
```
In our case it is : 
```bash
    $ celery -A celeryDjango worker --loglevel=info
```
####  **[Windows OS]**
```bash
    $ celery -A celeryDjango worker -l info --pool=solo
```
## **Run RabbitMQ (On Windows)**

Run:
```
C:\Program Files\RabbitMQ Server\rabbitmq_server-3.8.6\sbin\rabbitmq-server.bat
```
### **Run First Task**
```bash
    $ py manage.py shell
    $ from task1.tasks import add
    $ add.delay(2, 2)
```
or
```bash
    $ add.apply_async((2, 2), countdown=5)
```

### **Useful commands**
Show message on completion of task

```sh
    $ logger.info("Sent review email")
```
### **In case if your flower does not work**
Add the following lines to this file :
```sh
C:\django\yt-django-celery-series-intro-install-run-task\venv\lib\site-packages\tornado\platform\asyncio.py
```
Add these line at the start (in case flower does not start)

```sh
import sys

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

```

## **Start Flower**
```sh
$ flower -A celeryDjango --port=5555
```

## **Django-celery-beat**

This is normal startup for beat
```sh
$ celery -A celeryDjango beat -l INFO  # For deeper logs use DEBUG
```

Startup of beat with celery worker ( Embedded command )
```sh
$ celery -A celeryDjango worker -B -l INFO
```
You can also embed beat inside the worker by enabling the workers -B option

## **Database scheduler**
```sh
$ celery -A celeryDjango beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
```