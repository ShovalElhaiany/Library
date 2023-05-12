from django.urls import path
from . import views


app_name = 'library'

urlpatterns = [
    path('', views.mysite_home, name='mysite_home'),
    path('library_home/', views.library_home, name='library_home'),
    path('library_home/form/', views.form, name='form'),
    path('library_home/customers/', views.customers, name='customers'),
    path('library_home/customers/<int:customer_id>/', views.customer_ditails, name='customer_ditails'),
    path('library_home/shop/', views.Shop.as_view(), name='shop'),
    path('library_home/login', views.log_in, name='login'),

]
