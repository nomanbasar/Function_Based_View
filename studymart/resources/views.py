from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Free_course(request):
    return render(request, 'freecourse.html')

def blog(request):
    return render(request, 'blog.html')
