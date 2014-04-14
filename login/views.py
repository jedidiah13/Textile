import json
import string 
import random
from jsonview.decorators import json_view
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from crispy_forms.utils import render_crispy_form
from crispy_forms.helper import FormHelper, FormHelpersException
from crispy_forms.layout import Submit, Reset, Hidden, Button
from login.forms import RegistrationForm, LoginForm, updateFirstName
from login.models import UserProfile

@csrf_exempt
@json_view
def registration(request):
    
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = RegistrationForm(request.POST)
        

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.is_active = False 
	    user.save()

	    #Create And Send User Activation Email.
            confirmation_code = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for x in range(33)) 
            p = UserProfile(user=user, confirmation_code=confirmation_code)      
            p.save()
	    title = "Textile Fabric Consultants, Inc. Account Activation"
	    content = "Someone has recently registered at Textilefabric.com. We hope it was you. If so, please follow the link below. If not please disregard this email.\n" +"theftp.dyndns.org:8000/login/activate/" + str(p.confirmation_code) + "/" + user.username
	    send_mail(title, content, 'no-reply@gsick.com', [user.email], fail_silently=False)
	    # Update our variable to tell the template registration was successful.
            registered = True
            
        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors
            
    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    
    form = RegistrationForm(request.POST)
    form_html = render_crispy_form(form)
    result = {'success': registered, 'form_html': form_html}
    return result
 
@csrf_exempt
@json_view
def authenticateLogin(request):
    context = RequestContext(request)
    
    username = request.POST['username']
    password = request.POST['password']
    
    user = authenticate(username=username, password=password)
    print user
    if user is not None:
       if user.is_active:
          login(request, user)
          
         
	  result  = { 'success':  True}
	 
	  

          return result
          
       else:
          
	return HttpResponse("Your account is disabled.")
    else:
	
        result = { 'success': False }
        return result


@csrf_exempt
@json_view   
def authenticateUser(request):
   if not request.user.is_authenticated():
	print 'logged Out'
        return {'success': False}
   else:
	print 'logged In'
	return {'success': True}

@csrf_exempt
def activate(request, confirmation_code, username):
		
		user = User.objects.get(username=username[:-1])
		profile = user.get_profile()
		if profile.confirmation_code == confirmation_code:
			user.is_active = True
			user.save()
			user.backend='django.contrib.auth.backends.ModelBackend' 
			login(request,user)
		return HttpResponseRedirect('/')
	

@login_required
@csrf_exempt
@json_view
def logoutUser(request):
    logout(request)
    return {'success': True}	

@csrf_exempt
def userInfo(request):
    context = RequestContext(request)

   
    user = request.user
    
    return render_to_response('base.html',{'user': user})


@json_view
@csrf_exempt
def changeFirstName(request):
     context = RequestContext(request)
     if request.method == 'POST':

            user = User.objects.get(username=request.user.username)
            first_name = request.POST.get('first_name')
            user.first_name = first_name
            user.save()
            
            return {'success': True}
     else: return {'success': False}

@json_view
@csrf_exempt
def changeLastName(request):
     context = RequestContext(request)
     if request.method == 'POST':

            user = User.objects.get(username=request.user.username)
            last_name = request.POST.get('last_name')
            user.last_name = last_name
            user.save()
            
            return {'success': True}
     else: return {'success': False}

@json_view
@csrf_exempt
def changeEmail(request):
     context = RequestContext(request)
     if request.method == 'POST':

            user = User.objects.get(username=request.user.username)
            email = request.POST.get('email')
            user.email = email
            user.save()
            
            return {'success': True}
     else: return {'success': False}

@json_view
@csrf_exempt
def changePassword(request):
     context = RequestContext(request)
     if request.method == 'POST':

            user = User.objects.get(username=request.user.username)
            user.set_password(request.POST.get('password'))
            user.save()
            return {'success': True}
     else: return {'success': False}

@json_view
@csrf_exempt
def changeAddress(request):
     context = RequestContext(request)
     if request.method == 'POST':

            user = User.objects.get(username=request.user.username)
            profile = user.get_profile()
            print user.username
            print profile.address_lineOne
            address_lineOne = request.POST.get('addOne')
            print address_lineOne
            profile.address_lineOne = address_lineOne
            print user.address_lineOne
            address_lineTwo = request.POST.get('addTwo')
            print address_lineTwo
            profile.address_lineTwo = address_lineTwo
            print user.address_lineTwo
            city = request.POST.get('addThree')
            print city
            profile.city = city
            print user.city
            State = request.POST.get('addFour')
            print State
            profile.State = State
            print user.State
            zipCode = request.POST.get('addFive')
            print zipCode
            profile.zipCode = zipCode
            print user.zipCode
            user.save()
            

            return {'success': True}
     else: return {'success': False}

def orderHistory(request):
    context = RequestContext(request)
    return render_to_response('store/orderHistory.html')	
