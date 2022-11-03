from django.shortcuts import render,HttpResponse
from .models import post
# Create your views here.
def index(request):
    text = post.objects.all()
    # text = sorted(text,key = lambda x: x.date,reverse = True)
    return render(request,"index.html",{"text":text})

def page(request,name):
    page = post.objects.filter(name = name)
    # print("name is :",name)
    # print(post.objects.all())
    # print(page)
    return render(request,"page.html",{"page":page[0]})
    # return HttpResponse(request,"HI")