"""newjango_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import demo
from django.conf import settings
from django.conf.urls.static import static
from employee_details_app.views import first, base, person_contact_infor, person_info

urlpatterns = [
    path('admin/', admin.site.urls),
    path("demo/", demo, name="demo"),
    path("first/", first, name="first"),
    path("base/", base, name="base"),
    path("person_contact_infor/", person_contact_infor, name="person_contact_infor"),
    path("person_info/", person_info, name="person_info")
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)