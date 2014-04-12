from django.contrib.auth.models import User
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder
from crispy_forms.bootstrap import PrependedText, PrependedAppendedText, FormActions
from login.models import User, UserProfile



class RegistrationForm(forms.ModelForm):
        password = forms.CharField(widget=forms.PasswordInput())
        class Meta:
             model = User
     	     fields = ('username', 'email', 'first_name','last_name','password')
	def __init__(self, *args, **kwargs):
       		 super(RegistrationForm, self).__init__(*args, **kwargs)
       		 self.helper = FormHelper()
        	 self.helper.form_id = 'id-registration'
        	 self.helper.form_class = 'blueForms'
        	 self.helper.form_method = 'post'
        	 self.helper.form_action = '/login/register/'
		 self.helper.add_input(Submit('submit', 'Submit'))      	 	
	
             
class LoginForm(forms.ModelForm):
     password = forms.CharField(widget=forms.PasswordInput())

     class Meta:
	model = User
	fields = ('username', 'password')
     def __init__(self, *args, **kwargs):
                super(LoginForm, self).__init__(*args, **kwargs)        	
        	self.helper = FormHelper()
		self.helper.form_id = 'id-loginform'
		self.helper.form_class = 'blueForms'
        	self.helper.form_method = 'post'
		self.helper.form_action = '/login/authenticate/'
        	self.helper.add_input(Submit('submit', 'Submit'))
	    
class ContactForm(forms.ModelForm):

     class Meta:
        model = User
        fields = ('first_name','last_name', 'email')
     def __init__(self, *args, **kwargs):
                super(LoginForm, self).__init__(*args, **kwargs)
                self.helper.form_tag = False
		self.helper = FormHelper()
                self.helper.form_id = 'id-contact-form'
                self.helper.form_class = 'blueForms'
                self.helper.form_method = 'post'
                self.helper.form_action = '/contact/'
                self.helper.add_input(Submit('submit', 'Submit'))



class updateFirstName(forms.ModelForm):
    
    
    class Meta:
        model = User
        fields = ('first_name',)
        def __init__(self, *args, **kwargs):
            super(updateInfoForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_id = 'id-updateFirst'
            self.helper.form_class = 'blueForms'
            self.helper.form_method = 'post'
            self.helper.form_action = '/login/userInfoChange/'
            self.helper.add_input(Submit('submit', 'Submit'))
            
class updateLastName(forms.ModelForm):
    model = User
    
    class Meta:
        model = User
        fields = ('last_name',)
        def __init__(self, *args, **kwargs):
            super(updateInfoForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()

class updateEmail(forms.ModelForm):
    model = User
    
    class Meta:
        model = User
        fields = ('email',)
        def __init__(self, *args, **kwargs):
            super(updateInfoForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()

class updateAddress(forms.ModelForm):
    address_lineOne = forms.CharField(required=False)
    address_lineTwo = forms.CharField(required=False)
    city = forms.CharField(required=False)
    zipCode = forms.CharField(required=False)
    State = forms.CharField(required=False)
    
    class Meta:
        model = UserProfile
        fields = ('address_lineOne','address_lineTwo','city','zipCode','State')
        def __init__(self, *args, **kwargs):
            super(updateInfoForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()


