from django.template import RequestContext
from django.shortcuts import render_to_response
from login.forms import RegistrationForm
from login.forms import LoginForm


def index(request):
    context = RequestContext(request)
    return render_to_response('index.html', {'regform': RegistrationForm(),'loginform': LoginForm()},context )

def about(request):
	context = RequestContext(request)
	return render_to_response('about.html', {'regform': RegistrationForm(),'loginform': LoginForm()},context)

def contact(request):
	context = RequestContext(request)
	return render_to_response('contact.html', {'regform': RegistrationForm(),'loginform': LoginForm()},context)


