"""
Definition of views.
"""
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.utils import timezone
from django.contrib.auth.models import User

from app.models import *

from django.shortcuts import render,render_to_response, redirect
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from django import forms
from app.forms import Ticket_form,Ticket_update,TechUpdate
from django.shortcuts import get_object_or_404


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
            request,
            'app/index.html',
            {
                'title':'Home Page',
                'year':datetime.now().year,
            }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
def dashboard(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/dashboard.html',
        {
            'title':'Dashboard',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
def ticket(request):
    id = request.GET.get('id')
    u_id = request.user.id
    ##job = Job.objects.filter(person_id = 1)
    assert isinstance(request, HttpRequest)
    return render(request,'app/ticket_submit.html')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'app/change_password.html', {
        'form': form
    })

def add_model(request):
    id = request.GET.get('id')
    ticket_type = Ticket_type.objects.get(id=id)
    if request.method == "POST":
            form = Ticket_form(request.POST,request.FILES)
            
            if form.is_valid():
                model_instance = form.save(commit=False)
                model_instance.timestamp = timezone.now()
                model_instance.userID = request.user
                model_instance.save()
                last_id = Ticket.objects.latest('id')
                messages.add_message(request,messages.SUCCESS, "Ticket Number: " + str(last_id.id) + " has been successfully created; Enter another ticket for this type or go back to Dashboard")
                
                return redirect('/ticket?id=' + id)
    else:
        form = Ticket_form()
        form.fields["ticketID"].queryset = Ticket_code.objects.filter(t_type_id=id)
        return render(request, "app/ticket_submit.html", {'form': form,'ticket_type':ticket_type})

def mytickets(request):
    assert isinstance(request, HttpRequest)
    id = request.user
    my_tickets = Ticket.objects.filter(userID=id)
    return render(request,'app/mytickets.html',{'my_tickets':my_tickets})

def work_tickets(request):
    assert isinstance(request, HttpRequest)
    id = request.user
    my_tickets = Ticket.objects.filter(custID__cust_tech = id)
    ticket_count = Ticket.objects.filter(custID__cust_tech = id).filter(status = "Not begun").count()
    return render(request,'app/worktickets.html',{'my_tickets':my_tickets,'tick_cnt':ticket_count})

def work_detail(request,id):
    ##assert isinstance(request, HttpRequest)
    p=get_object_or_404(Ticket,pk = id)
    if request.method == "POST":

        form = Ticket_update(request.POST or None, instance = p)
        
        if form.is_valid():
            form.save()
            return redirect('/work_tickets')
    else:
        form = Ticket_update()
        detail = Ticket.objects.get(id = id)
    return render(request,'app/workdetail.html',{'detail':detail,'form':form})

def tech_detail(request,id):
    history = Tech_update.objects.filter(tech_ticket = id)
    if request.method == "POST":
        a = Ticket.objects.get(id=id)
        b = request.POST['tech_status']
        form = TechUpdate(request.POST)
        
        if form.is_valid():
            Ticket.objects.filter(pk=a.id).update(status= b)
            model_instance = form.save(commit=False)
            model_instance.tech_ticket = a
            model_instance.save()
            return redirect('/work_tickets')
    else:
        form = TechUpdate()
        detail = Ticket.objects.get(id = id)
    return render(request,'app/workdetail1.html',{'detail':detail,'form':form,'history':history})

