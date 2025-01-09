from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
# Create your views here.
from .models import Post


def testView(request):
    return HttpResponse("Hello World")
def post_list(request):
    posts = Post.published.all()
    return render(request,'blog/list.html',{'posts':posts})
def post_detail(request, id):
    # try:
    #     post = Post.published.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404("No Post found.")

    # instead of the above stuff we have a shortcut
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    return render(
 request,
 'blog/detail.html',
 {'post': post}
 )
