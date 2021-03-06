from django import forms
from django.forms import DateTimeField
from models import Client, Barber

class SignupForm(forms.Form):
    # choices used for the radio button
    CHOICES = [
        ('selectBarber', 'I am a Barber'),
        ('selectClient', 'I am a Client')]

    userType = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    firstName = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Joe', 'size': 40}))
    lastName = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Doe', 'size': 40}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'name@example.com', 'size': 40}))
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '123 Street, San Diego, CA 92122', 'size': 40}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'size': 40}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '(800) 123-4567', 'size': 40}))
    
class LoginForm(forms.Form):
    # coices used for the radio button
    CHOICES = [
        ('selectBarber', 'Barber'),
        ('selectClient', 'Client')]

    userType = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'name@example.com', 'size': 40}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'size': 40}))
    
class AppointmentForm(forms.Form):
    # choices for location of the barber
    CHOICES = [
        ('selectLocationBarber', "Barber's House"),
        ('selectLocationClient', "Client's House")]
    when = forms.CharField()
    addressChoice = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    
class EditClientForm(forms.Form):
    # firstName = forms.CharField()
    # lastName = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    phone = forms.CharField()
    address = forms.CharField()
    profilePic = forms.ImageField(required=False)

class EditBarberForm(forms.Form):
    description = forms.CharField(widget=forms.Textarea)
    address = forms.CharField()
    phone = forms.CharField()
    price = forms.CharField()
    walkin = forms.CharField()
    skills = forms.CharField(widget=forms.Textarea)
    schedule = forms.CharField(widget=forms.Textarea)
    profilePic = forms.ImageField(required=False)
    gallery = forms.ImageField(required=False)

class ReviewForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 12}))
