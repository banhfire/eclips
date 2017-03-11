from django import forms

class SignupForm(forms.Form):
    # choices used for the radio button
    CHOICES = [
        ('selectBarber', 'I am a Barber'),
        ('selectClient', 'I am a Client')]

    userType = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    firstName = forms.CharField()
    lastName = forms.CharField()
    email = forms.EmailField()
    address = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    phone = forms.CharField()
    
    
class BarberCreationForm(forms.Form):
    # what else should be included here? PRICES, SCHEDULE, WALKIN, DRIVE TO
    description = forms.CharField()
    price = forms.CharField()
    walkin = forms.CharField()
    schedule = forms.CharField()
    
<<<<<<< HEAD
    
=======
class EditClientProfileForm(forms.Form):
    description = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    address = forms.CharField()
    phone = forms.CharField()
>>>>>>> 43150f7c2dc9df929fc9d72c5dd13233a9eaa948
