from django.urls import path, reverse_lazy

from . import views
from .views import *

urlpatterns = [
    path('', MainPage.as_view(), name='main_page'),
    path('object/<int:pk>/', DetailRealEstatePage.as_view(), name='RealEstate_object'),
    path('rental', RentalRealEstatesPage.as_view(), name='rental_list'),
    path('selling', SellingRealEstatesPage.as_view(), name='selling_list'),
    path('confirmation', BookingConfirmation.as_view(), name='confirmation'),
    path('book/<int:pk>/', BookingObject.as_view(), name='book_object'),
]
