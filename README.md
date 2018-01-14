# stalkerGKSU
Portal for finding github profiles of people related on the basis of organisations.

## Requirements
1. Install redis-server and mysql
```
$ sudo apt-get install redis-server
$ sudo apt-get install mysql-server
```
2. Install requirements
```
$ pip install -r requirements.txt
```
3. Create DB Stalker in mysql, change the password accordingly in `config.py`
4. Set the environment variables for reCAPTCHA
```
$ export RECAPTCHA_SITE_KEY="public key"
$ export RECAPTCHA_SECRET_KEY="secret key"
```
5. Share the email server credentials in `config.py`
6. Migrate the DB tables
```
$ python task.py db init
$ python task.py db migrate
$ python task.py db upgrade

```
In case above commands gives error. Delete the migration folder and delete alembic_version table in the database. And run the above three commands again.
```sh
mysql> SELECT * FROM alembic_version;
mysql> DROP TABLE alembic_version;
$ python task.py db init
$ python task.py db migrate
$ python task.py db upgrade
```

## Run

Run each in a different terminal window...

```
# redis
$ redis-server

# worker process
$ python worker.py

# the app
$ python routes.py
```
