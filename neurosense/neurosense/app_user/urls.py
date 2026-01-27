from django.urls import path

from neurosense.app_user import views


app_name="user"



urlpatterns = [
path('vcon/',views.vcon,name='vcon'),
path('vdetail/',views.vdetail,name='vdetail'),
]