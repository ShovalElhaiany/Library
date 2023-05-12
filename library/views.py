from . models import Customer
from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse, HttpResponsePermanentRedirect
from library.forms import CustomerForm, ShopForm
from django.urls import reverse
from django.views import View, generic
from django.contrib.auth import login


def mysite_home(request):
    return render(request, 'library/mysite_home.html')


def library_home(request):
    return render(request, 'library/library_home.html')


def form(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        for field in form.fields:
            form.fields[field].required = False
        if form.is_valid():
            form.save()
            return render(request, 'library/registration.html', {'form': CustomerForm})
        else:
            print(form.errors.as_text())
            return HttpResponsePermanentRedirect(reverse('library:library_home'))
    else:
        context = {"form": CustomerForm}
        return render(request, 'library/registration.html', context)


def log_in(request):
    # login(request, user)
    return HttpResponsePermanentRedirect('library/login.html')


def customers(request):
    all_customers = Customer.objects.all()
    context = {"all_customers": all_customers}
    return render(request, 'library/customers.html', context=context)


def customer_ditails(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)
    context = {"customer": customer}
    return render(request, 'library/customer_ditails.html', context=context)


class Shop(View):

    def post(self, request):
        form = ShopForm(request.POST)
        if form.is_valid():
            book_name = form.cleaned_data['book_name']
            amount = form.cleaned_data['amount']
            # c=Customer(book_name, amount)
            # c.save()
            Customer.objects.create(book_name=book_name, amount=amount)
            return HttpResponsePermanentRedirect(reverse('library:library_home'))
        else:
            message = 'error'
            return render(request, 'library:library_home')

    def get(self, request):
        form = ShopForm()
        context = {'form': form}
        return render(request, 'library/shop.html', context=context)


# class customer2(generic.ListView):
#     template_name = "ibrary/customers.html"
#     context_object_name = "all_customers"

#     def get_queryset(self):
#         return Customer.objects.all()


# class customers2(generic.ListView):
#     model = Customer
#     template_name = "ibrary/customer.html"
