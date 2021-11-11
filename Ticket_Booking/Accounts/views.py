from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse, request
from django.shortcuts import render
from tickets.models import Ticket
from django.contrib.auth.models import User
from tickets.models import Ticket


class SignUpView(generic.CreateView):
    #return render(request,'registration/signup.html')
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def homepage(request):
    return render(request,'base.html') 
    
#def user_info(request):
    #user_info=User.objects.all()
    #user_info=request.user.ticket.all()
    #return render(request,'ticket.html',{'user_info':user_info}) 