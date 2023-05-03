from django.shortcuts import render

# Create your views here.

def filters(request):
    d={'data':'Hai HoW ArE yOu'}
    return render(request,'filters.html',d)