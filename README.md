

# **Configure your backend for Email Sending**

Command Reference
***

## **Install celery**
```bash
    $ pip install celery
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
    $ celery -A core worker -l info --pool=solo
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
    #Show message on completion of task
        logger.info("Sent review email")