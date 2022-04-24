from django.contrib import admin
from django.urls import path

from app.views import home, transaction_data

urlpatterns = [
    path('', home, name='home'),
    path('<str:txn_hash>', transaction_data, name='transaction_date')
]
