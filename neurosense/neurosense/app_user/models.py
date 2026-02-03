from django.db import models

from neurosense.users.models import User

# Create your models here.
class appointment(models.Model):
    customer=models.ForeignKey(User, on_delete=models.CASCADE,related_name='appointment_customer')
    councellor=models.ForeignKey(User, on_delete=models.CASCADE,related_name='appontment_councellor')
    currentdate= models.DateField(auto_now_add=True)
    appointmentdate= models.DateField()