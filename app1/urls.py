from django.urls import path

from .views import index,Cart_Data,Checkout,Payment_done,Process_payment,Payment_canceled

urlpatterns = [
    path('',index,name='index'),
    path('cart/',Cart_Data,name='cart'),
    path('check/<int:id>/',Checkout,name='check'),
    
    path('payment_process/',Process_payment,name='process_payment'),
    path('payment_done/',Payment_done,name='payment_done'),
    path('payment_canceled/',Payment_canceled,name='payment_canceled'),  
]
