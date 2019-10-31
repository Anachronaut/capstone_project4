from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_form, name='home_form'),
    path('result/<int:result_pk>', views.stored_result, name='stored_result'),
    path('delete', views.delete_result, name='delete_result')
]
