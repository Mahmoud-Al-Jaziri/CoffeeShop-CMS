from django.forms import ModelForm ,TextInput,EmailInput,PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.validators import EmailValidator
from .models import Order , Customer

class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ['user']
          
class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        self.fields['password1'].widget.attrs.update({ 
            'style':"width: 100%; padding: 12px;padding-left: 30px;border: none;background: #eeeeee;",
            'placeholder':'Password'
            })
         
        self.fields['password2'].widget.attrs.update({ 
            'style':"width: 100%; padding: 12px;padding-left: 30px;border: none;background: #eeeeee;",
            'placeholder':'Re-enter password'
            })
         
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
        
        widgets = {
            'username' : TextInput(
                attrs={
                    'class':"input",
                    'style':"width: 100%; padding: 12px;padding-left: 30px;border: none;background: #eeeeee;",
                    'placeholder':"Name"
                }),

            'email' : EmailInput(
                attrs={
                    'class':"input",
                    'style':"width: 100%; padding: 12px;padding-left: 30px;border: none;background: #eeeeee;",
                    'placeholder':"Email"
                }),
        }

