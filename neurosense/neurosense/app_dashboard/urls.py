from django.urls import path

from neurosense.app_dashboard import views


app_name="dashboard"



urlpatterns = [
    path("admin/", views.appdash),
    path("guest/",views.guest),
    path("login/",views.login_view,name='login'),
    path("counsellor/",views.counsellor,name='counsellor'),
    path("cust/",views.cust,name='cust'),
    path("userdash/",views.userdash,name='userdash'),
    path("qview/",views.qview,name='qview'),
    path('con/',views.con,name='con'),
]