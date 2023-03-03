
from django.contrib import admin
from django.urls import path
from invoice_app.views import InvoiceAPI, ProductList, ProductDetials

urlpatterns = [
    path('admin/', admin.site.urls),
    path('invoice/', InvoiceAPI.as_view()),
    path('products/', ProductList.as_view()),
    path('products/<int:pk>/', ProductDetials.as_view()),
]
