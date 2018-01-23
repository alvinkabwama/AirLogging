from django.db import models

class Owner(models.Model):
    
    name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add =True)
      
    def __str__(self):
        return self.name + ' - ' + self.email
    
    
class Device(models.Model): 
    deviceserial = models.CharField(max_length = 255)
    devicelocation = models.CharField(max_length = 255)
    added_at = models.DateTimeField(auto_now_add =True)
    owner = models.ForeignKey(Owner, blank= True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.deviceserial
    
    
     
class Data(models.Model):
    
    device = models.ForeignKey(Device, blank= True, on_delete=models.CASCADE)
    pm25 = models.CharField(max_length = 255)
    co2 = models.CharField(max_length = 255)
    received_at = models.DateTimeField(auto_now_add =True)
   
    def __str__(self):
        return str(self.device)
    
