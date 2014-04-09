from django.template import RequestContext
from django.shortcuts import render_to_response
from companion.models import Catagories, Topics, Fabrics

def companion(request, id):

    context = RequestContext(request)
    ids = Catagories.objects.get(catagory=id);
    fabrics = Fabrics.objects.filter(fabCatagory_id=ids.id).all()
    fab_categories = Catagories.objects.all();
    return render_to_response('companion/companion-homepage.html', {'fabrics': fabrics, 'fab_categories': fab_categories},context)
    
