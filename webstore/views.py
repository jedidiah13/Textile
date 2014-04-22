from django.template import RequestContext
from django.shortcuts import render_to_response
from login.forms import RegistrationForm
from login.forms import LoginForm
from webstore.models import StoreItem, StoreCategory
from django.http import HttpResponse
from webstore.bing_search import run_query
import simplejson as json
from haystack.query import SearchQuerySet
from django.forms.models import model_to_dict
from copy import deepcopy

def webstore(request,id):
    context = RequestContext(request)    
    #if request.method == 'GET':
    ids = StoreCategory.objects.get(categoryName=id)
    items = StoreItem.objects.filter(category_id=ids.id).all()
    item_categories = StoreCategory.objects.all();
    return render_to_response('store/shop-homepage.html', {'items': items, 'item_categories': item_categories, 'regform': RegistrationForm(),'loginform': LoginForm()},context)

def featured(request):
    
    context = RequestContext(request)
    items = StoreItem.objects.all()
    return render_to_response('index.html',{'success': True, 'items': items}, context)

def getImage(request, id, directory, image_name):
    imagelocation = directory + "/" + image_name
    print imagelocation
    image_data = open(imagelocation, "rb").read()
    return HttpResponse(image_data, mimetype="image/png")
    
def home(request):
    context = RequestContext(request)
    return render_to_response('store/shop-homepage.html', {'regform': RegistrationForm(),'loginform': LoginForm()},context )

def searchStore(request):
    context = RequestContext(request)
    
    sqs = SearchQuerySet().filter(content=request.POST.get('search_text'))
    #searchResults = StoreItem.objects.filter(itemName__icontains= sqs )
    result_list = StoreItem.objects.filter(itemName__icontains= sqs )
    #result_list = [result.itemName for result in sqs]
    
        

    #print json.dumps({'result_list': result_list})
    #return HttpResponse( json.dumps({'result_list': result_list}), content_type='application/json')
    return render_to_response('store/shop-homepage.html',{'result_list': result_list}, context)

def autocomplete(request):
    sqs = SearchQuerySet().autocomplete(content_auto=request.GET.get('q', ''))[:5]
    suggestions = [result.itemName for result in sqs]
    # Make sure you return a JSON object, not a bare list.
    # Otherwise, you could be vulnerable to an XSS attack.
    the_data = json.dumps({
        'results': suggestions
    })
    
    return HttpResponse(the_data, content_type='application/json')


def query(request):
    context = RequestContext(request)
    
            

    return render_to_response('store/shop-homepage.html',{'success': True},context)

# The car is stored in the session as a dictionary of a dictionary that has
# the primary key of an item and how many were added
def buttonTest(request):
    print "pressed button"
    context = RequestContext(request)
    return render_to_response('store/shop-homepage.html',{'success': True}, context)

def addToCart(request, itemKey, quantity):
    #print "FLUSHING THE SESSION"
    #request.session.flush()

    print itemKey
    context = RequestContext(request)
    print request.session.keys()

    if quantity <= 0:
        removeFromCart(request, itemKey)
    if not 'cartList' in request.session:
        #request.session['cartList'] = {itemKey : {"quantity" : quantity}}
        print "making a new cart"
        print [itemKey, quantity]
        request.session['cartList'] = []
        request.session['cartList'].append([itemKey, quantity])
        # make a new cart
    else:
        print "inserting to cart"
        print [itemKey, quantity]
        alreadydone = False
        for index in xrange(len(request.session['cartList'])):
            print "at index ", index 
            print "looking at ", request.session['cartList'][index]
            if itemKey == request.session['cartList'][index][0]: # already in list
                print "already in cart, updating quantity"
                request.session['cartList'][index][1] = quantity
                alreadydone = True
                break
        if not alreadydone: # append the new item to the cart
            print "appending to cart"
            request.session['cartList'].append([itemKey, quantity])
        # this works for modifying quantity as well as adding
    print "printing session cart before save"
    print request.session['cartList']
    request.session.save()
    cart = deepcopy(request.session['cartList']) # wondering if this is needed...
    print "printing cart list"
    print cart

    sendlist = json.dumps({'cart':cart})
    return HttpResponse(sendlist, content_type='application/json')
    #return render_to_response('store/shop-homepage.html',{'cart':cart,'success': True},context)

def removeFromCart(request, itemKey):
    context = RequestContext(request)
    if 'cartList' in request.session and itemKey in request.session['cartList']:
        pass
        #request.session['cartList'].pop(itemKey)
    request.session.save()
    return render_to_response('store/shop-homepage.html',{'success': True},context)

def deleteCart(request):
    context = RequestContext(request)
    if 'cartList' in request.session:
        request.session.pop('cartList')
    request.session.save()
    return render_to_response('store/shop-homepage.html',{'success': True},context)