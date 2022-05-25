from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('meetings/',views.meetings,name='meetings'),
    path('meeting_details/',views.meeting_details,name='meeting_details'),
    path('contact/',views.contact,name='contact'),
    path('pujan_samagri/',views.pujan_samagri,name='pujan_samagri')
]