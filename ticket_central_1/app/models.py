"""
Definition of models.
"""

from django.db import models
from datetime import datetime

# Create your models here.
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    
    cust_name = models.CharField(max_length = 25)
    cust_address = models.CharField(max_length = 100, help_text = 'Enter street number and name only')
    cust_city = models.CharField(max_length = 100)
    cust_state = models.CharField(max_length = 2, help_text = 'Please type the abbreviation for your state')
    cust_zip = models.CharField(max_length = 5)
    cust_tech = models.ForeignKey(User)
    def __str__(self):
        return "%s" % (self.cust_name)


class Ticket_type(models.Model):
    type = models.CharField(max_length = 25)

    def __str__(self):
        return(self.type)

class Ticket_code(models.Model):
    description = models.TextField(max_length = 500)
    t_type = models.ForeignKey(Ticket_type)

    def __str__(self):
        return(self.description)

class Ticket(models.Model):
    status_choice = (
        ('Active','Active'),
        ('Done','Done'),
        ('In-progress','In-progress'),
        )
    level = (
        ('Low','Low'),
        ('Med','Med'),
        ('High','High'),
        )
    contact_method = (('Email','Email'),('Text','Text'),('Phone','Phone'),)
    affected_num = (('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),)

    custID = models.ForeignKey(Customer)
    userID = models.ForeignKey(User)
    ticketID = models.ForeignKey(Ticket_code)
    ticket_created = models.DateField(default=datetime.now)
    ticket_completed = models.DateField(null=True)
    ticket_fix = models.TextField(max_length = 500, null=True)
    description = models.TextField(max_length = 500)
    severity = models.CharField(max_length = 20, choices=level, default="Low")
    room_num = models.CharField(max_length = 20, null=True)
    contact = models.CharField(max_length = 25, null=True)
    contact_method = models.CharField(max_length = 14, null=True,default='Email',choices = contact_method)
    aff_work = models.CharField(max_length = 20, default="Low",choices=level)
    aff_num = models.CharField(max_length = 20, default="1",choices=affected_num)
    status = models.CharField(max_length = 25, default="Not begun",choices = status_choice ,help_text = 'Please enter Active, Resolved or In-progress')
    document = models.FileField(upload_to='documents/',null=True,blank=True)
    def __str__(self):
        return(self.custID.cust_name)

class Tech_update(models.Model):
    status_choice = (
        ('Active','Active'),
        ('Done','Done'),
        ('In-progress','In-progress'),
        )
    tech_ticket = models.ForeignKey(Ticket)
    tech_date = models.DateField()
    tech_notes = models.TextField(max_length = 500, null=True)
    tech_status = models.CharField(max_length = 25, default="Active",choices = status_choice ,help_text = 'Please enter Active, Resolved or In-progress')