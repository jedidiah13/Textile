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

def companion(request, id):
    context = RequestContext(request)
    	
    fab_categories = Catagories.objects.all()
    
    return render_to_response('companion/companion-homepage.html', { 'fab_categories': fab_categories},context)
    

def getImage(request, id, directory, image_name):
    imagelocation = directory + "/" + image_name
    print imagelocation
    image_data = open(imagelocation, "rb").read()
    return HttpResponse(image_data, mimetype="image/png")  


def topic(request, id):   
        print id
        ids = Catagories.objects.get(catagory=id)
        topics = [model_to_dict(topic) for topic in Topics.objects.filter(fabCatagory_id=ids.id)]
        print topics
        topic_list = json.dumps({'topics':topics})
        return HttpResponse(topic_list, content_type='application/json')



