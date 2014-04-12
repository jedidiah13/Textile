from django.contrib.auth.models import User
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder
from crispy_forms.bootstrap import PrependedText, PrependedAppendedText, FormActions
from login.models import User



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



class updateInfoForm(forms.ModelForm):
    model = User
    password = forms.CharField(widget=forms.PasswordInput(), required=False)
    address_lineOne = forms.CharField(required=False)
    address_lineTwo = forms.CharField(required=False)
    city = forms.CharField(required=False)
    zipCode = forms.CharField(required=False)
    State = forms.CharField(required=False)
    class Meta:
        model = User
        fields = ('email','address_lineOne','address_lineTwo','city','State','zipCode')
        def __init__(self, *args, **kwargs):
            super(updateInfoForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()


