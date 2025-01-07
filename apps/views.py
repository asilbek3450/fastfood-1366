from django.shortcuts import render
from .models import Category, Product, BookTable
# Create your views here.
def home_page(request):
    kategoriyalar = Category.objects.all()
    productlar = Product.objects.all()

    if request.method == "POST":
        ism = request.POST["ism"]
        telefon = request.POST["telefon"]
        soni = request.POST["soni"]
        sana = request.POST["sana"]
        BookTable.objects.create(ism=ism, telefon=telefon, soni=soni, sana=sana)
    
    context = {
        'categories': kategoriyalar,
        'products': productlar
    }

    return render(request, template_name='index.html', context=context)