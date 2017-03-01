from django.shortcuts import render
from django.http import Http404
from blog.models import Post

# Create your views here.
def index(request):
	posts = Post.objects.all()
	return render(request,'blog/index.html',
		{ 'posts':posts  }) 

def post_details(request,id):
	try:
		post = Post.objects.get(id=id)
	except Post.DoesNotExist:
		raise Http404('This item does not exist')
