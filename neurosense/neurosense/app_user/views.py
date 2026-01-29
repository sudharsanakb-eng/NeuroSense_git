from django.shortcuts import render

from app_core.models import councellor

# Create your views here.
def vcon(request):
    c=councellor.objects.filter(status='Accept')
    return render(request ,'conview.html',{'vdi':c})
def vdetail(request,id):
    c=councellor.objects.get(id=id)
    return render(request ,'details.html',{'vdi':c})
def vapp(request):
   
    return render(request ,'appoinment.html')
