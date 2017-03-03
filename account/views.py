from django.shortcuts import render, render_to_response
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render_to_response('index.html')

def signup(request):
    return render_to_response('account/signup.html')

def login(request):
	return render_to_response("account/login.html")

def help(request):
    return render_to_response("account/help.html")
def bprofile(request):
    return render_to_response("account/bprofile.html")