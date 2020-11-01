from django.shortcuts import render

# Create your views here.
def home(request):
    title = 'welcome home'
    return render(request, "index.html", {"title":title})