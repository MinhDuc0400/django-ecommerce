from pyexpat import model
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.db.models import Func, F
from django.core.paginator import Paginator

from books.models import BookItem
from clothes.models import ClothesItem
from electronics.models import ElectronicItem, Laptop, MobilePhone, Tivi
from shoes.models import ShoesItem

# Create your views here.


class HomeView(ListView):
    context_object_name = 'bookItems'
    queryset = BookItem.objects.filter(status=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['electronicsItems'] = ElectronicItem.objects.filter(
            status=True)
        context['shoesItems'] = ShoesItem.objects.filter(status=True)
        context['clothesItems'] = ClothesItem.objects.filter(status=True)
        return context

    template_name = 'home.html'


class CategoryElectronicView(ListView):
    context_object_name = 'electronicItems'

    def get_queryset(self):
        electronicItems = ElectronicItem.objects.filter(status=True)
        _manufacturer = self.request.GET.get('manufacturer')
        _price = self.request.GET.get('price')
        _sort = self.request.GET.get('sort')
        _page = self.request.GET.get('page')
        if _manufacturer:
            electronicItems = electronicItems.filter(
                electronic__manufacturer=_manufacturer)
        if _price:
            if _price == 'duoi5tr':
                electronicItems = electronicItems.annotate(priceBought=F(
                    'price')*((100-F('discount'))/100)).filter(priceBought__lt=5000000)
            elif _price == '5trden10tr':
                electronicItems = electronicItems.annotate(priceBought=F(
                    'price')*((100-F('discount'))/100)).filter(priceBought__gte=5000000, priceBought__lt=10000000)
            elif _price == '10trden15tr':
                electronicItems = electronicItems.annotate(priceBought=F(
                    'price')*((100-F('discount'))/100)).filter(priceBought__gte=10000000, priceBought__lt=15000000)
            elif _price == '15trden25tr':
                electronicItems = electronicItems.annotate(priceBought=F(
                    'price')*((100-F('discount'))/100)).filter(priceBought__gte=15000000, priceBought__lt=25000000)
            elif _price == 'tren25tr':
                electronicItems = electronicItems.annotate(priceBought=F(
                    'price')*((100-F('discount'))/100)).filter(priceBought__gte=25000000)
        if _sort:
            if _sort == 'low-to-high':
                electronicItems = electronicItems.annotate(priceBought=F(
                    'price')*((100-F('discount'))/100)).order_by('priceBought')
            elif _sort == 'high-to-low':
                electronicItems = electronicItems.annotate(priceBought=F(
                    'price')*((100-F('discount'))/100)).order_by('-priceBought')

        paginator = Paginator(electronicItems, 8)
        electronicItems = paginator.get_page(_page)

        return electronicItems

    template_name = 'category_electronic.html'


class CategoryElectronicDetailView(DetailView):
    model = ElectronicItem

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sameItems'] = ElectronicItem.objects.filter(
            status=True).exclude(barCode=self.kwargs['pk']).order_by('?')
        print(ElectronicItem.objects.filter(
            status=True).exclude(barCode=self.kwargs['pk']).order_by('?'))
        return context

    template_name = 'electronic_detail.html'