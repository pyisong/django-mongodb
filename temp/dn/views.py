from django.shortcuts import render
from django.db import models
from django.db import connection, connections
from django.http import HttpResponse
from . import docs
from dn import models
# Create your views here.


def app_label(request):
    my_model = models.MyModel()
    print "+++++++++++++++"
    app = my_model._meta.app_label
    print app
    return HttpResponse(app)


# def index(request):
#     profile1 = docs.Profile(gender='male', location='Beijing')
#     user1 = docs.User(
#         username='Perchouli',
#         website='http://dmyz.org',
#         tags=['Web','Django','JS'],
#         profile=profile1
#     )
#     user1.save()
#     user1_json = str(user1.to_mongo())
#     return HttpResponse(user1_json)
