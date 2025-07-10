# med/urls.py
from django.urls import path
from . import views

urlpatterns = [
path('login/',views.login,name='login'),
path('register/',views.register,name='register'),
    path('Dr',views.Dr,name='Dr'),
path('s_Dr',views.s_Dr,name='s_Dr'),
    path('deDr',views.deDr,name='deDr'),
path('addDr',views.addDr,name='addDr'),
path('upDr',views.upDr,name='upDr')
]