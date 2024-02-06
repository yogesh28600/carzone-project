from django.shortcuts import render,redirect
from inquiry.models import Inquiry
from django.contrib import messages
import numbers
# Create your views here.
def inquiry(request):
    if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            topic = request.POST['topic']
            city = request.POST['city']
            state = request.POST['state']
            email = request.POST['email']
            phone = request.POST['phone'] 
            car_id = request.POST['car_id']
            car_title = request.POST['car_title']
            car_model = request.POST['car_model']
            car_price = request.POST['car_price']
            user_id = request.POST['user_id']
            comment = request.POST['message']
            has_contacted = Inquiry.objects.all().filter(user_id=user_id,car_id=car_id)
            if has_contacted:
                messages.error(request,'You have already inquired about this car. Please wait for response')
                return redirect('/cars/'+car_id)
            else:
                inquire = Inquiry(first_name=first_name,last_name=last_name,topic=topic,city=city,state=state,email=email,car_id=car_id,car_title=car_title,car_model=car_model,car_price=car_price,user_id=user_id,comment=comment)
                if  phone.isdigit() and len(phone) == 10 :
                    inquire.phone=int(phone)
                if inquire is not None:
                    inquire.save()
                    messages.success(request,'Inquiry successfull, we will get back to you soon.')
                else:
                    messages.error(request,"Something went wrong")
                return redirect('/cars/'+car_id)

    return redirect('home')