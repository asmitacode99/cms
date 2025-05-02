import random
from django.utils.text import slugify



def generate_slug(name):
    return slugify(name)+str(random.randrange(0,100000,1))+str(random.randrange(0,100000,1))


