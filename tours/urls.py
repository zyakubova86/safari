from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('en/', home, name='home_en'),

    path('tours/<int:pk>/', tours_list_by_category, name='tours_list_by_category'),
    path('en/tours/<int:pk>/', tours_list_by_category, name='tours_list_by_category_en'),

    path('tour/<int:pk>/', tour_detail, name='tour_detail'),
    path('en/tour/<int:pk>/', tour_detail, name='tour_detail_en'),

    path('book-ticket/', book_ticket, name='book_ticket'),
    path('en/book-ticket/', book_ticket, name='book_ticket_en'),

    path('contact/', contact, name='contact'),
    path('en/contact/', contact, name='contact_en'),

    path('uzbekistan/', uzbekistan, name='uzbekistan'),
    path('en/uzbekistan/', uzbekistan, name='uzbekistan_en'),

]
