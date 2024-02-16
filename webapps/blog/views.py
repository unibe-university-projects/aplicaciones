from django.shortcuts import render

# Create your views here.
def list(request):
    blog = Blog.objects.all()
    return render(request, list.html', {'blog': blog})