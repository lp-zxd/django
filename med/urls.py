# med/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('s_gongju',views.s_gongju,name='s_gongju'),
    path('s_med',views.s_med,name='s_med'),
path('deme',views.deme,name='deme'),
path('addme',views.addme,name='addme'),
path('upme',views.upme,name='upme'),
path('addgj',views.addgj,name='addgj'),
path('degj',views.degj,name='degj'),
path('upgj',views.upgj,name='upgj'),
]