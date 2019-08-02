from django import forms

from .models import Account

class LoginForm(forms.ModelForm):
	class Meta:
		model = Account
		fields = [
			"username",
			"password",
		]

class  SignupForm(forms.Form):
	New_Username = forms.CharField()
	Password = forms.CharField()
	Confirm_Password = forms.CharField()


