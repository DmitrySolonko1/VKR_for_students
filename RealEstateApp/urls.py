from django.urls import path, reverse_lazy
from .views import *

urlpatterns = [
    path('', MainPage.as_view(), name='main_page'),
    path('object/<int:pk>/', DetailRealEstatePage.as_view(), name='RealEstate_object'),
    path('rental', RentalRealEstatesPage.as_view(), name='rental_list'),
    path('selling', SellingRealEstatesPage.as_view(), name='selling_list'),
]
