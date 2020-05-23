import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

import random
from first_app.models import Topic, AccessTracker, Webpages
from faker import Faker

fakegen = Faker()
topics=['Chatting','News','Marketing','Education','Information and Broadcast']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):

    for entry in range(N):

        topic = add_topic() #getting topic

        fake_name=fakegen.company() #Creating various fake fields
        fake_url=fakegen.url()
        fake_date=fakegen.date()

        # creating and saving fake webpage data
        webpg = Webpages.objects.get_or_create(top_name=topic,name=fake_name,url=fake_url)[0]

        #creating and saving fake access tracking data

        acc_tr = AccessTracker.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__':
    print("Populating fake data for all tables :")
    populate(20)
    print("Population completed")
