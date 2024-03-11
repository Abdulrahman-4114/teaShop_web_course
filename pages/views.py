from django.shortcuts import render



def index(request):
   return render(request, 'pages/index.html')

def about(request):
    pass

    
# Create your views here.
