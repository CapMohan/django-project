from django.db import models
from datetime import datetime

# Create your models here.

class Employees_details(models.Model):
    title = models.CharField(max_length = 100)
    name = models.CharField(max_length = 50)
    age = models.IntegerField()
    salary = models.IntegerField()
    location = models.CharField(max_length = 100)
    about_self = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title   

# <!-- {% block content %}

# {% for i in post %}
# {{i.title}}<br>
# {{i.name}}<br>
# {{i.age}}<br>
# {{i.salary}}<br>

# {% endfor %}
# {% endblock content %} -->

class Person_contact_details(models.Model):
    full_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    company_location = models.CharField(max_length=100)
    contact_num = models.CharField(max_length=10)
    permanant_address = models.TextField()
    email_address = models.CharField(max_length=200)
    current_address = models.TextField()
    created_date = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return self.full_name