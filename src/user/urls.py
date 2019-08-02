from django.urls import path
#from .views import something here

from .views import create_user, user_option, login_user

from django.contrib.auth.views import LoginView



app_name = "user"

urlpatterns = [
	path('', user_option, name = "option"),
	path('create/', create_user, name = "create"),
	path('login/', LoginView.as_view(template_name = "user/login_user.html"), name = "login"),
	
]