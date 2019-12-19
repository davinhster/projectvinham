from django.shortcuts import render
from .forms import LoginForm, SignupForm


# Create your views here.

def create_user(request, *args, **kwargs):
	form = SignupForm(request.POST or None)
	context = {
		"form": form
	}

	return render(request,"user/create_user.html",context)

def login_user(request, *args, **kwargs):
	template_name = "user/login_user.html"
	form = LoginForm(request.POST or None)
	context = {
		"form":form
	}
	return render(request,"user/login_user.html",context)

def user_option(request, *args, **kwargs):
	context = {

	}

	return render(request, "user/user_option.html", context)

def success_view(request, *args, **kwargs):
	context = {

	}

	return render(request,"user/success.html",context)