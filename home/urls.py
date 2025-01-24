from django.urls import path
from .views import index, dashboard, pricing, about, contact, faq, services, add_property

urlpatterns = [
    path('', index, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('pricing/', pricing, name='pricing'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('faq/', faq, name='faq'),
    path('services/', services, name='services'),
    path('add-property/', add_property, name='add_property'),
    
]