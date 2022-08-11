from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        if len(name) == 0:
            return render(request, "feedback/index.html", context={'got_error': True}) 
        print(name)
        return HttpResponseRedirect('/done')
    return render(request, "feedback/index.html") 

def done(request):
    return render(request, "feedback/done.html", context={'got_error': False}) 