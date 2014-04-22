from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from login.forms import RegistrationForm
from login.forms import LoginForm
from webstore.models import StoreItem

def index(request):
    context = RequestContext(request)
    items = StoreItem.objects.all()
    return render_to_response('index.html', {'items': items,'regform': RegistrationForm(),'loginform': LoginForm()},context )

def getImage(request, directory, image_name):
    imagelocation = directory + "/" + image_name
    print imagelocation
    image_data = open(imagelocation, "rb").read()
    return HttpResponse(image_data, mimetype="image/png")

def about(request):
	context = RequestContext(request)
	return render_to_response('about.html', {'regform': RegistrationForm(),'loginform': LoginForm()},context)

def contact(request):
	context = RequestContext(request)
	return render_to_response('contact.html', {'regform': RegistrationForm(),'loginform': LoginForm()},context)


