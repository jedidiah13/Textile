from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from login.forms import RegistrationForm
from login.forms import LoginForm
from webstore.models import StoreItem

def index(request):
    context = RequestContext(request)
    items = StoreItem.objects.all()
    return render_to_response('index.html', {'items': items,'regform': RegistrationForm(),'loginform': LoginForm()},context )

def about(request):
	context = RequestContext(request)
	return render_to_response('about.html', {'regform': RegistrationForm(),'loginform': LoginForm()},context)


@csrf_exempt
def contact(request):
    context = RequestContext(request)
    if(request.method == 'POST'):
    	title = "Textile Fabric Consultants, Inc. Customer Contact"
       	last = request.POST.get('last')
        first = request.POST.get('first')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        comments = request.POST.get('comments')
        content = "Name: " + str(last) + "," + str(first)  + "Phone: " + str(phone)  + "Email: " + str(email)  + "Comments: " + str(comments)
        sendemail = [ "hwtechnicalsolutions@gmail.com" ] 
        send_mail(title, content, 'no-reply@gsick.com', sendemail, fail_silently=False)
        return render_to_response('contact.html',{'success':True},context)
    return render_to_response('contact.html',context)
