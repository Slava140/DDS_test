from django.contrib import admin
from django.urls import path, include

from transactions.urls import urlpatterns as transaction_urls

admin.site.site_header = 'Движение денежных средств'

urlpatterns = [
    path('', include(transaction_urls)),
    path('', admin.site.urls),
]
