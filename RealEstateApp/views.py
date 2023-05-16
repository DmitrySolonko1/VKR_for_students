from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from .models import RealEstate
import folium
from geopy.geocoders import Nominatim
from .filters import *
from .forms import DateTimeForm


# Create your views here.
class MainPage(ListView):
    context_object_name = 'real_estate_list'
    template_name = 'RealEstateApp/MainPage.html'

    def get_queryset(self):
        queryset = RealEstate.objects.all()
        status = self.request.GET.get('status')
        if status:
            queryset = queryset.filter(status=status)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rental_list'] = self.get_queryset().filter(category__name='Аренда').order_by('-pk')
        context['sale_list'] = self.get_queryset().filter(category__name='Продажа').order_by('-pk')
        return context


class DetailRealEstatePage(DetailView):
    model = RealEstate
    template_name = 'RealEstateApp/DetailRealEstate.html'
    context_object_name = 'object'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = RealEstate.objects.get(pk=self.kwargs['pk']).address

        # map
        # Создание карты и изначального её расположения карты #
        m = folium.Map(location=[55.7887400, 49.1221400], zoom_start=12, min_zoom=6)
        popup = folium.Popup(
            'Город: ' + str(self.object.city) + '</br></br>' + 'Район: ' + str(self.object.district) +
            '</br></br>' + 'Площадь: ' + str(self.object.area) + '</br></br>' + 'Этаж: ' + str(self.object.floor) +
            '</br></br>' + 'Кол-во комнат: ' + str(
                self.object.rooms) + '</br></br>' + 'Планировка: ' + self.object.layout +
            '</br></br>' + 'Ремонт: ' + self.object.finishing + '</br></br>' + 'Сан.узел: ' + self.object.bathroom +
            '</br></br>' + 'Балкон: ' + self.object.balcony + '</br></br>', max_width=300)

        # getting geolocation
        geolocator = Nominatim(user_agent="RealEstate")
        print(f"{self.object.city}, {self.object.address}")
        location = geolocator.geocode(f"{self.object.city}, {self.object.address}")
        print(location)
        if location is not None:
            latitude = location.latitude
            print(latitude)
            longitude = location.longitude
            print(longitude)
            # Добавление объекта на карту
            folium.Marker(location=[latitude, longitude], tooltip='Нажмите чтобы узнать больше',
                          popup=popup).add_to(m)
        else:
            folium.Marker(location=[55.78809075, 49.21747788857183], tooltip='Нажмите чтобы узнать больше',
                          popup=popup).add_to(m)

        m = m._repr_html_()
        context['map'] = m
        return context


class RentalRealEstatesPage(ListView):
    model = RealEstate
    context_object_name = 'rental_objects'
    template_name = 'RealEstateApp/RentalListPage.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rental_filter'] = RentalFilter(self.request.GET,
                                                queryset=RealEstate.objects.filter(category__name='Аренда').order_by(
                                                    '-pk'))

        m = folium.Map(location=[55.7887400, 49.1221400], zoom_start=12, min_zoom=6)
        for object in RentalFilter(self.request.GET,
                                   queryset=RealEstate.objects.filter(category__name='Аренда').order_by('-pk')).qs:
            popup = folium.Popup(
                'Город: ' + str(object.city) + '</br></br>' + 'Район: ' + str(object.district) +
                '</br></br>' + 'Площадь: ' + str(object.area) + '</br></br>' + 'Этаж: ' + str(object.floor) +
                '</br></br>' + 'Кол-во комнат: ' + str(
                    object.rooms) + '</br></br>' + 'Планировка: ' + object.layout +
                '</br></br>' + 'Ремонт: ' + object.finishing + '</br></br>' + 'Сан.узел: ' + object.bathroom +
                '</br></br>' + 'Балкон: ' + object.balcony + '</br></br>', max_width=300)

            geolocator = Nominatim(user_agent="RealEstate")
            print(f"{object.city}, {object.address}")
            location = geolocator.geocode(f"{object.city}, {object.address}")
            print(location)
            if location is not None:
                latitude = location.latitude
                print(latitude)
                longitude = location.longitude
                print(longitude)
                # Добавление объекта на карту
                folium.Marker(location=[latitude, longitude], tooltip='Нажмите чтобы узнать больше',
                              popup=popup).add_to(m)
            else:
                folium.Marker(location=[55.78809075, 49.21747788857183], tooltip='Нажмите чтобы узнать больше',
                              popup=popup).add_to(m)
        m = m._repr_html_()
        context['map'] = m
        return context

    def get_queryset(self):
        queryset = super().get_queryset().filter(category__name='Аренда').order_by('-pk')
        return RentalFilter(self.request.GET, queryset=queryset).qs


class SellingRealEstatesPage(ListView):
    model = RealEstate
    template_name = 'RealEstateApp/SellingListPage.html'
    paginate_by = 10
    context_object_name = 'selling_objects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['selling_filter'] = RentalFilter(self.request.GET,
                                                 queryset=RealEstate.objects.filter(category__name='Продажа').order_by(
                                                     '-pk'))
        m = folium.Map(location=[55.7887400, 49.1221400], zoom_start=12, min_zoom=6)
        for object in RentalFilter(self.request.GET,
                                   queryset=RealEstate.objects.filter(category__name='Продажа').order_by('-pk')).qs:
            popup = folium.Popup(
                'Город: ' + str(object.city) + '</br></br>' + 'Район: ' + str(object.district) +
                '</br></br>' + 'Площадь: ' + str(object.area) + '</br></br>' + 'Этаж: ' + str(object.floor) +
                '</br></br>' + 'Кол-во комнат: ' + str(
                    object.rooms) + '</br></br>' + 'Планировка: ' + object.layout +
                '</br></br>' + 'Ремонт: ' + object.finishing + '</br></br>' + 'Сан.узел: ' + object.bathroom +
                '</br></br>' + 'Балкон: ' + object.balcony + '</br></br>', max_width=300)

            geolocator = Nominatim(user_agent="RealEstate")
            print(f"{object.city}, {object.address}")
            location = geolocator.geocode(f"{object.city}, {object.address}")
            print(location)
            if location is not None:
                latitude = location.latitude
                print(latitude)
                longitude = location.longitude
                print(longitude)
                # Добавление объекта на карту
                folium.Marker(location=[latitude, longitude], tooltip='Нажмите чтобы узнать больше',
                              popup=popup).add_to(m)
            else:
                folium.Marker(location=[55.78809075, 49.21747788857183], tooltip='Нажмите чтобы узнать больше',
                              popup=popup).add_to(m)
        m = m._repr_html_()
        context['map'] = m

        return context

    def get_queryset(self):
        queryset = super().get_queryset().filter(category__name='Продажа').order_by('-pk')
        return RentalFilter(self.request.GET, queryset=queryset).qs


# def book_object(request, object_id):
#     object = RealEstate.objects.get(pk=object_id)
#     if request.method == 'POST':
#         form = DateTimeForm(request.POST)
#         if form.is_valid():
#             time_slot = form.cleaned_data['time_slot']
#             if time_slot.is_available:
#                 booking = Booking.objects.create(object=object, time_slot=time_slot, client_name=form.cleaned_data['client_name'])
#                 time_slot.is_available = False
#                 time_slot.save()
#                 return redirect('confirmation', booking_id=booking.id)
#     else:
#         form = DateTimeForm()
#     return render(request, 'RealEstateApp/BookingObject.html', {'object': object, 'form': form})

class BookingObject(DetailView):
    model = RealEstate
    template_name = 'RealEstateApp/BookingObject.html'
    context_object_name = 'object'
    form_class = DateTimeForm  # Добавляем кастомную форму

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = DateTimeForm()  # Добавляем форму в контекст
        return context

    def post(self, request, pk):
        if request.method == 'POST':
            form = DateTimeForm(request.POST)
            if form.is_valid():
                time_slot = TimeSlot.objects.create(time=form.cleaned_data['time'])
                booking = Booking.objects.create(object=self.get_object(), time_slot=time_slot,
                                                 client_name=request.user, realtor=self.get_object().realtor)
                return redirect('confirmation')
            else:
                form = DateTimeForm()
                return redirect('main_page')


class BookingConfirmation(TemplateView):
    template_name = 'RealEstateApp/BookingConfirmation.html'
