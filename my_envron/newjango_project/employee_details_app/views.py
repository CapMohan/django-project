from django.shortcuts import render
from django.http import HttpResponse
from .models import Employees_details, Person_contact_details

# Create your views here.

def base(request):
    post = Employees_details.objects.all()
    return render(request, "base.html", {"post":post})

def first(request):
    return render(request, "first.html", {"name":"Murali"})

#Below funstion is used for to create or to store person details into database through web table.
def person_contact_infor(request):
    if request.method == 'POST':
        full_name = request.POST['name']
        company_name = request.POST['company_name']
        company_location = request.POST['company_location']
        contact_num = request.POST['contact_num']
        permanant_address = request.POST['permanant_address']
        email_address = request.POST['email']
        current_address = request.POST['current_address']
        created_date = request.POST.get('date')
        person_contact = Person_contact_details(full_name = full_name, company_name = company_name, company_location = company_location, contact_num = contact_num, permanant_address = permanant_address, 
                                email_address = email_address, current_address = current_address, created_date = created_date)
        person_contact.save()
    return render(request,'form_to_database.html')

#Below funstion is used for to get person details from database.
def person_info(request):
    post = Person_contact_details.objects.all()
    return render(request, "base.html", {"post":post})