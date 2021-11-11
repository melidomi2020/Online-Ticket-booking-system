from django.shortcuts import render,redirect
from django.http import HttpResponse
from tickets import forms
from .forms import ticketForm
from .models import Ticket

def ticket_detail(request):
     if request.method=='POST':
         form=ticketForm(request.POST)
         if form.is_valid():
             
            form.save()
            print("information receive")

     form=ticketForm()   
     return render(request,'ticketdetail.html',{'form':form})

def ticket_no(request):
    ticket_info=Ticket.objects.filter(user=request.user)
    return render(request,'ticket.html',{'ticket_info':ticket_info})
