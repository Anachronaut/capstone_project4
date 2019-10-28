from django.urls import path
from . import views

urlpatterns = [
    path('', views.place_list, name='place_list'),
    path('place/<int:place_pk>', views.stored_result, name='stored_result'),
    path('delete', views.delete_result, name='delete_result')
]
