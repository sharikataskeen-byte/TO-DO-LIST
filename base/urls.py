from django.urls import path
from .views import *

urlpatterns=[
    path('home/',home,name='home'),
    path('add/',add,name='add'),
    path('completed/',completed,name='completed'),
    path('trash/',trash,name='trash'),
    path('about/',about,name='about'),
    path('update/<int:pk>',update,name='update'),
    path('hcompleted/<int:pk>',hcompleted,name='hcompleted'),
    path('hdelete/<int:pk>',hdelete,name='hdelete'),
    path('hcompletedall/',hcompletedall,name='hcompletedall'),
    path('deleteall/',deleteall,name='deleteall'),
    path('delete/<int:pk>/',delete,name='delete'),
    path('crestore/<int:pk>/',crestore,name='crestore'),
    path('crestoreall/',crestoreall,name='crestoreall'),
    path('cdelete/<int:pk>',cdelete,name='cdelete'),
    path('cdeleteall/',cdeleteall,name='cdeleteall'),
    path('tdeleteall/',tdeleteall,name='tdeleteall'),
    path('trestore/<int:pk>/',trestore,name='trestore'),
    path('trestoreall/',trestoreall,name='trestoreall'),
]
