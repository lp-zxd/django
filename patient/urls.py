# med/urls.py
from django.urls import path
from . import views

urlpatterns = [
path('patient',views.patient,name='patient'),
path('s_patient',views.s_patient,name='s_patient'),
path('bed',views.bed,name='bed'),
path('s_bed',views.s_bed,name='s_bed'),
path('depa',views.depa,name='depa'),
path('addpa',views.addpa,name='addpa'),
path('uppa',views.uppa,name='uppa'),
]