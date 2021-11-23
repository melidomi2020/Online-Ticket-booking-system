from django.shortcuts import render,redirect
from django.http import HttpResponse
from tickets import forms
from .forms import ticketForm
from .models import Ticket
from math import *
from datetime import datetime
from datetime import timedelta

def ticket_detail(request):
     if request.method=='POST':
         form=ticketForm(request.POST)
         if form.is_valid():
             
            form.save()
            return redirect('/ticket/information/')
        

     form=ticketForm()   
     return render(request,'ticketdetail.html',{'form':form})

def ticket_no(request):
    ticket_info=Ticket.objects.filter(user=request.user)
    #print(ticket_info.user)
    waitors_no=Ticket.objects.all().count()
    #waitors_no=Ticket.objects.filter(user=request.user).values_list('reg_no',flat=True)
    print(waitors_no)
    now=datetime.now()
    #print(now)
    for u in ticket_info:
        time_str=str(u.time)
        tim_str=time_str.split("+")
        ti=tim_str[0]
        c="".join(ti)
        #f=tim_str
        
        date_format_str='%Y-%m-%d %H:%M:%S.%f'
        given_time=datetime.strptime(c,date_format_str)
        #print('given time is:',given_time)
        n=waitors_no*2
        final_time=given_time+timedelta(minutes=n)
        expected_time=final_time.strftime('%Y-%m-%d %H:%M:%S.%f')
        #print("final time after some minutes:",final_time_str)
        #u=x.Time
    

    return render(request,'ticket.html',{'ticket_info':ticket_info,'expected_time':expected_time,'waitors_no':waitors_no})
 