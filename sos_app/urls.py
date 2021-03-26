from django.urls import path

from . import views

urlpatterns = [
    path('', views.add_details, name='add_contacts'),
    path('home/<slug:user_id>', views.send_sos, name='home'),
    path('location/', views.get_location, name='location')
]
