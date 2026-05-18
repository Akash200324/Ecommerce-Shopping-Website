from django.urls import path
from .import views

urlpatterns = [
    path('', views.home),
    path('street-flex/', views.street_flex, name='street_flex'),
    path('simple-swag/', views.simple_swag, name='simple_swag'),
    path('fit-gear/', views.fit_gear, name='fit_gear'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
]