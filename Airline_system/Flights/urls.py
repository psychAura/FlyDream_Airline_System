from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:flight_id>', views.flight, name="flight"),
    path('<int:flight_id>/book', views.book_flight, name= "book_flight"),
    path('book/', views.book, name= "book" ),
    path('search/', views.search, name="search"),
    path('search/<int:flight_id>/book_flight', views.book_flight, name="book_flight"),
    path('booking/success/<int:booking_id>/', views.booking_success, name='booking_success'),
    path('about/', TemplateView.as_view(template_name='flights/about.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='flights/contact.html'), name='contact'),

   
]