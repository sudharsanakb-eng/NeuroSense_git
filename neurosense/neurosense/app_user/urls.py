from django.urls import path

from neurosense.app_user import views


app_name="user"



urlpatterns = [
path('vcon/',views.vcon,name='vcon'),
path('vdetail/<int:id>',views.vdetail,name='vdetail'),
path('app/<int:id>',views.app,name='app'),
]