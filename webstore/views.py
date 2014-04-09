from django.template import RequestContext
from django.shortcuts import render_to_response
from login.forms import RegistrationForm
from login.forms import LoginForm
from webstore.models import StoreItem, StoreCategory
from django.http import HttpResponse
from webstore.bing_search import run_query
import simplejson as json
from haystack.query import SearchQuerySet

def webstore(request,id):
    context = RequestContext(request)    
    #if request.method == 'GET':
    ids = StoreCategory.objects.get(categoryName=id);
    items = StoreItem.objects.filter(category_id=ids.id).all()
    item_categories = StoreCategory.objects.all();
    return render_to_response('store/shop-homepage.html', {'items': items, 'item_categories': item_categories, 'regform': RegistrationForm(),'loginform': LoginForm()},context)

           
    #return render_to_response('store/shop-homepage.html', {'items': items, 'item_categories': item_categories, 'regform': RegistrationForm(),'loginform': LoginForm()},context)
def getImage(request, id, directory, image_name):
    imagelocation = directory + "/" + image_name
    print imagelocation
    image_data = open(imagelocation, "rb").read()
    return HttpResponse(image_data, mimetype="image/png")
    
def home(request):
    context = RequestContext(request)
    return render_to_response('store/shop-homepage.html', {'regform': RegistrationForm(),'loginform': LoginForm()},context )

def search(request):
	
	if request.method == 'POST':
		context = RequestContext(request)
        	query = request.POST['query'].strip()
        	print "searching"
        	

	        result_list = StoreItem.objects.filter(itemName_contains="Fiber").all()
        	    	
        	return render_to_response('store/shop-homepage.html', {'result_list': result_list}, context)


def autocomplete(request):
    sqs = SearchQuerySet().autocomplete(content_auto=request.GET.get('q', ''))[:5]
    suggestions = [result.itemName for result in sqs]
    # Make sure you return a JSON object, not a bare list.
    # Otherwise, you could be vulnerable to an XSS attack.
    the_data = json.dumps({
        'results': suggestions
    })
    print "called auto complete"
    return HttpResponse(the_data, content_type='application/json')

















