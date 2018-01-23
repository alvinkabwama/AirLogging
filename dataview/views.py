#from django.shortcuts import render
from django.http import HttpResponse
from .models import Data, Device


#def datashow(request):
    
    
def datarecieve(request):
    if(request.method == 'GET'):
        serialnumber = request.GET.get("serial") 
        
        in_c02 = request.GET.get("c02")
        in_pm25 = request.GET.get("pm25")
        
        #return HttpResponse("<h3> Co2 is {a}and serial is {b} and pm2.5 is {c} </h3>".format(a=c02, b=serialnumber, c=pm25))
    
        if(serialnumber and in_c02 and in_pm25):
            
            #incomingdevice = Device.objects.get(deviceserial = serialnumber)
            if(Device.objects.get(deviceserial = serialnumber)):
                incomingdevice = Device.objects.get(deviceserial = serialnumber)
                Data(device=incomingdevice, co2=in_c02,  pm25=in_pm25).save()
            
                return HttpResponse("<br><h3> Pass </h3>")
        
            else:
                return HttpResponse("<br><h3> Device Missing </h3>")
            
        else:
            return HttpResponse("<br><h3> Data Missing </h3>")
        
        
        
        
        
        

# Create your views here.
