from django.shortcuts import render
from django.utils import timezone
from .models import Post 

# Create your views here.
def post_list(request):
	post = Post.objects.filte(published_date--lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'post': post})
