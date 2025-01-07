from django.shortcuts import render
from .models import Category, Product
# Create your views here.
def home_page(request):
    kategoriyalar = Category.objects.all()
    productlar = Product.objects.all()

    context = {
        'categories': kategoriyalar,
        'products': productlar
    }

    return render(request, template_name='index.html', context=context)