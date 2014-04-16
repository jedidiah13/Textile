from django.template import RequestContext
from django.shortcuts import render_to_response
from companion.models import Catagories, Topics, Fabrics
from webstore.bing_search import run_query
import simplejson as json
from haystack.query import SearchQuerySet

def companion(request, id):

    context = RequestContext(request)
    ids = Catagories.objects.get(catagory=id);
    fabrics = Fabrics.objects.filter(fabCatagory_id=ids.id).all()
    fab_categories = Catagories.objects.all();
    return render_to_response('companion/companion-homepage.html', {'fabrics': fabrics, 'fab_categories': fab_categories},context)

def getImage(request, id, directory, image_name):
    imagelocation = directory + "/" + image_name
    print imagelocation
    image_data = open(imagelocation, "rb").read()
    return HttpResponse(image_data, mimetype="image/png")


    
