from django.shortcuts import render,redirect
from .models import Cart
from .forms import Cart_Form
from django.urls import reverse
from django.contrib import messages
from django.conf import settings
from decimal import Decimal
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    form = Cart_Form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cart')
    return render(request,'index.html',{'form':form})

def Cart_Data(request):
    data = Cart.objects.all()
    return render(request,'Cart_disp.html',{'data':data})

def Checkout(request,id):
    request.session['order_id'] = id
    return redirect('process_payment')

def Process_payment(request):
    order_id = request.session.get('order_id')
    order = Cart.objects.get(id=order_id)
    host = request.get_host()
    # print(f'host = {host}')
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': order.prod_price,
        'item_name': order.prod_name,
        'invoice': order.id,
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host,reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host,reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format(host,reverse('payment_canceled')),
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'process_payment.html', {'order': order, 'form': form})

@csrf_exempt
def Payment_done(request):
    return render(request, 'payment_done.html')
 
@csrf_exempt
def Payment_canceled(request):
    return render(request, 'payment_cancelled.html')

    
        