from django.template import RequestContext
from django.shortcuts import render_to_response
from companion.models import Catagories, Topics, Fabrics
from webstore.bing_search import run_query
import simplejson as json
from haystack.query import SearchQuerySet
from django.views.decorators.csrf import csrf_exempt
from jsonview.decorators import json_view
from django.http import HttpResponse
from django.forms.models import model_to_dict
from django.core import serializers
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')

def companion(request, id):
    context = RequestContext(request)
    fab_categories = Catagories.objects.all()
    return render_to_response('companion/companion-homepage.html', { 'fab_categories': fab_categories},context)

def app(request, id):
    context = RequestContext(request)
    fab_categories = Catagories.objects.all()
    return render_to_response('companion/companionSub.html', { 'fab_categories': fab_categories},context)

def getImage(request, id, directory, image_name):
    imagelocation = directory + "/" + image_name
    image_data = open(imagelocation, "rb").read()
    return HttpResponse(image_data, content_type="image/png")  

def topic(request, id):
    id = id.replace("amp; "," ") #This line is needed to remove generated '&' character encoding, "amp;"
    ids = Catagories.objects.get(catagory=id)
    topics = [model_to_dict(topic) for topic in Topics.objects.filter(fabCatagory_id=ids.id)]
    topic_list = json.dumps({'topics':topics})
    return HttpResponse(topic_list, content_type='application/json')

def fabric(request, id):
    test = Topics.objects.get(topicId= id)
    ids = Topics.objects.get(topic= test)
    fabrics = [model_to_dict(fabric) for fabric in Fabrics.objects.filter(fabTopic_id=ids.id)]
    fabric_list = serializers.serialize('json', Fabrics.objects.filter(fabTopic_id=ids.id), fields=('topic', 'fabName','fabDescription','fabContent','fabWeave','fabDye','fabFinish','fabDescription','fabImage','fabImage_secondary','fabVideoURL','isPremium'))
    return HttpResponse(fabric_list, content_type='application/json')


# old code...can probably be deleted
# def companion(request, id):
#     ids = Categories.objects.get(category=id);
#     items = Fabrics.objects.filter(category_id=ids.id).all()
#     return render_to_response('companion/companion-homepage.html', {'items': items, 'fab_categories': item_categories, 'regform': RegistrationForm(),'loginform': LoginForm()},context)
