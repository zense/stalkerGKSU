# stalkerGKSU
It is a portal for finding github profiles of people related on the basis of organisations.

## Requirements
1. Install requirements ```pip install -r requirements.txt```
2. Create DB Stalker in mysql, change the password accordingly in `config.py`
3. Migrate the DB tables:<br>
```python
python task.py db init
python task.py db migrate
python task.py db upgrade
```

## To run

Run the server
<br>
`python routes.py`
