from django.shortcuts import render,get_object_or_404
from .models import Category,Product
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger,InvalidPage

def allProdCat(request, c_slug=None):
    c_page = None
    products_list = None


    if c_slug != None:

        c_page = get_object_or_404(Category, slug=c_slug)
        products_list = Product.objects.filter(category=c_page,available=True)

    else:
        products_list = Product.objects.filter(available=True)

    paginator = Paginator(products_list,6)
    page_number = request.GET.get('page')

    try:
        products = paginator.page(page_number)

    except PageNotAnInteger:
        products = paginator.page(1)

    except EmptyPage:
        products = paginator.page((paginator.num_pages))

    return render(request,"category.html",{'category': c_page, 'products': products})





def proDetail(request,c_slug,product_slug):
    product = Product.objects.get(category__slug=c_slug, slug=product_slug)
    return render(request,'product.html', {'product': product})






