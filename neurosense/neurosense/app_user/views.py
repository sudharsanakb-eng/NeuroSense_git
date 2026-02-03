from django.http import HttpResponse
from django.shortcuts import render

from app_core.models import councellor
from app_dashboard.models import customer
from app_user.models import appointment
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from app_dashboard.models import customer

# Create your views here.
def vcon(request):
    c=councellor.objects.filter(status='Accept')
    return render(request ,'conview.html',{'vdi':c})
def vdetail(request,id):
    c=councellor.objects.get(id=id)
    return render(request ,'details.html',{'vdi':c})

def app(request, id):
    
    # 1. Fetch the specific counsellor
    counc = get_object_or_404(councellor, id=id)

    # 2. Fetch the customer profile of logged-in user
    try:
        profile = customer.objects.get(user=request.user)
    except customer.DoesNotExist:

        profile = None

    if request.method == "POST":
        selected_date = request.POST.get("date")  # from <input type="date" name="date">

        # 3. Create appointment
        appoint = appointment.objects.create(
            councellor=counc.user,          # counsellor is a User
            customer=request.user,          # logged-in User
            appointmentdate=selected_date   # DateField accepts YYYY-MM-DD
        )

        return HttpResponse(
            "<script>alert('Booked');window.location='/dashboard/userdash';</script>"
        )

    # 4. Pass data to template
    return render(
        request,
        "appoinment.html",
        {
            "councellor": counc,   # {{ councellor.user.username }}
            "customer": profile ,  # {{ customer.age }}
            "id":id
        }
    )

