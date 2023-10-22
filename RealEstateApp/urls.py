from django.urls import path, reverse_lazy
from .views import *

urlpatterns = [
    path('', MainPage.as_view(), name='main_page'),
    path('object/<int:pk>/', DetailRealEstatePage.as_view(), name='RealEstate_object'),
    path('rental', RentalRealEstatesPage.as_view(), name='rental_list'),
    path('selling', SellingRealEstatesPage.as_view(), name='selling_list'),
    path('confirmation', BookingConfirmation.as_view(), name='confirmation'),
    path('contacts', ContactsPage.as_view(), name='contacts'),
    path('book/<int:pk>/', BookingObject.as_view(), name='book_object'),
    path('add_object', AddingObject.as_view(), name='adding_object'),
    path('create_contract', CreateContract.as_view(), name='create_contract')
]
