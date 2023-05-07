
from django.shortcuts import render, get_object_or_404
from phones.models import Phone

def catalog(request):
    sort_by = request.GET.get('sort', 'name')  # Default sorting by name
    phones = Phone.objects.all().order_by(sort_by)
    return render(request, 'catalog.html', {'phones': phones})



def phone_details(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    return render(request, 'product.html', {'phone': phone})


