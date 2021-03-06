'''This file is created to fill up database for debugging, delete before deploy'''
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page
from random import randint

def populate():
    python_pages = [
        {"title": "Official Python Tutorial",
         "url": "http://docs.python.org/2/tutorial/"},
        {"title": "How to Think like a Computer Scientist",
         "url": "http://www.greenteapress.com/thinkpython/"},
        {"title": "Learn Python in 10 Minutes",
         "url": "http://www.korokithakis.net/tutorials/python/"}
    ]

    django_pages = [
        {"title": "Official Django Tutorial",
         "url": "https://docs.djangoproject.com/en/1.9/intro/tutorial01/"},
        {"title": "Django Rocks",
         "url": "http://www.djangorocks.com/"},
        {"title": "How to Tango with Django",
         "url": "http://www.tangowithdjango.com/"}
    ]

    other_pages = [
        {"title": "Bottle",
         "url": "http://bottlepy.org/docs/dev/"},
        {"title": "Flask",
         "url": "http://flask.pocoo.org"}
    ]

    cats = {"Python": {"pages": python_pages, "views": 128, "likes": 64},
            "Django": {"pages": django_pages, "views": 64, "likes": 32},
            "Other Frameworks": {"pages": other_pages, "views": -1} }

    for lst in (python_pages, django_pages, other_pages):
        for dict in lst:
            dict['views'] = randint(0, 101)


    for cat, cat_data in cats.items():
        c = add_cat(cat, **cat_data)
        for p in cat_data["pages"]:
            add_page(c, **p)

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))


def add_page(cat, **kwargs):
    p = Page.objects.get_or_create(category=cat, title=kwargs.get("title"))[0]
    p.url = kwargs.get("url")
    p.views = kwargs.get("views", 0)
    p.save()
    return p


def add_cat(name: str, **kwargs):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = kwargs.get("views", 0)
    c.likes = kwargs.get("likes", 0)
    c.save()
    return c


if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()