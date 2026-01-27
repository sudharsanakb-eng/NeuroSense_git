from django.shortcuts import render

from app_core.models import councellor

# Create your views here.
def vcon(request):
    c=councellor.objects.filter(status='Accept')
    return render(request ,'conview.html',{'vdi':c})
def vdetail(request):
    c=councellor.objects.all()
    return render(request ,'details.html',{'vdi':c})