import io
from time import sleep
import requests
import json
from functools import reduce
from celery import Celery
from datetime import timedelta
import random
from sqlalchemy.orm import declarative_base

app = Celery('tasks')

# app.conf.beat_schedule = {
#     'fetchschema': {
#         'task': 'tasks.fetchschema',
#         'schedule': timedelta(seconds=10),
#     },
# }


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, fetchschema.s(), name='add every 10')

    # # Calls test('world') every 30 seconds
    # sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # # Executes every Monday morning at 7:30 a.m.
    # sender.add_periodic_task(
    #     crontab(hour=7, minute=30, day_of_week=1),
    #     test.s('Happy Mondays!'),
    # )

@app.task
def fetchschema():
    def reducer(acc,curr):
        curr = {
            "Scheme_Name": curr['fields']['schemeName'],
            "Scheme_Short Title": curr['fields']['schemeShortTitle'],
            "Scheme_Category": curr['fields']['schemeCategory'],
            "Brief_Description": curr['fields']['briefDescription']
        }
        return acc + [curr]
    
    req = requests.get("https://api.myscheme.in/search/v2/schemes?lang=en&q=%5B%7B%22identifier%22%3A%22schemeCategory%22%2C%22value%22%3A%22Agriculture%2CRural%20%26%20Environment%22%7D%5D&keyword=&sort=&from=0&size=10",headers={
        'x-api-key':"tYTy5eEhlu9rFjyxuCr7ra7ACp4dv1RH8gWuHTDc"
    })
        
    data = reduce(reducer,req.json()['data']['hits']['items'],[])
    # print(data)
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)





