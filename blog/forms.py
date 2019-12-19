from django import forms

from .models import Blog


class PostForm(forms.ModelForm):
	post = forms.CharField(label = "Make a post below~!",widget = forms.Textarea(attrs = {"rows":5,
															"cols":136,
															"placeholder":"State your opinions here!",
														   }
												  )

						  )
	class Meta:
		model = Blog
		exclude = ('name',)
		fields =[
			"post"
		]




# #raw form
# class RawPostForm(forms.Form):
# 	title = forms.something
