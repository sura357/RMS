"""FunRehab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from AppProject.views import *


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('index/', index),
    # path('listone/', listone),
    # path('listall/', listall),
    # path('login/', login),
    # path('logout/', logout),
    # path('patients/', select_patient),
    # path('patient_view/', patient_view),
    # path('plan_edit/', plan_edit),
    # path('patient_register/', patient_register),

    # 前端
    path('patient_Login/', patient_Login),
    path('patient_Logout/', patient_Logout),
    path('patient_home/', patient_home),
    path('patient_Information/', patient_Information),
    path('patient_medicalrecord/', patient_medicalrecord),
    path('patient_rehubrecord/', patient_rehubrecord),

    # 後端
    path('rehabilitator_Information/', rehabilitator_Information),
    path('rehabilitator_CheckPlan/', rehabilitator_checkPlan),
    path('rehabilitator_addPlan/', rehabilitator_addPlan),
    path('rehabilitator_contactrecord/', rehabilitator_contactrecord),
    path('rehabilitator_rentalrecords/', rehabilitator_rentalrecords),
    path('rehabilitator_rehubrecord/', rehabilitator_rehubrecord),
    path('rehabilitator_medicalrecord/', rehabilitator_medicalrecord),



    # path('userprofile/', userprofile),
    # path('deleteuser/<int:id>', deleteuser),
    # path('products', product),
    # path('product_detail/<int:id>', product_detail),
    # path('cart', cart),
    # path('buy/<int:id>', buy),
    # path('orderconfirm', orderconfirm),
    # path('orderprogress', orderprogress),
]
