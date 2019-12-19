from django.shortcuts import render
from .forms import PostForm
from .models import Blog
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


from django.contrib.auth.models import User

# Create your views here.


@login_required
def post_view(request):
	form = PostForm(request.POST or None)

	if Blog.objects.count() > 5:
		everything = Blog.objects.all().delete()

		obj = form.save(commit=False)
		obj.name = request.user
		obj.save()
		form = PostForm()
	
	elif form.is_valid():
		obj = form.save(commit=False)
		obj.name = request.user
		obj.save()
		form = PostForm()	


	context = {
		'form':form
	}
	queryset = Blog.objects.all()
	context = {
		"object_list":queryset,
		"form":form
	}



	return render(request,"home_view.html",context)


@login_required
def edit_view(request):


	context = {

	}

	return render(request, "blog/update.html",context)














