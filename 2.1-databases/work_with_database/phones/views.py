from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


from django.shortcuts import render
from .models import Phone

def show_catalog(request, sort=None):
    if sort == 'name':
        phones = Phone.objects.order_by('name')
    elif sort == 'min_price':
        phones = Phone.objects.order_by('price')
    elif sort == 'max_price':
        phones = Phone.objects.order_by('-price')
    else:
        phones = Phone.objects.all()

    context = {'phones': phones}
    return render(request, 'catalog.html', context)






def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, 'product.html', context)

