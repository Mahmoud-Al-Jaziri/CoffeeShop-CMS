from django.shortcuts import render ,redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import *
from .forms import OrderForm , CreateUserForm , CustomerForm
from .filter import OrderFilter
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user , allowed_users , admin_only

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            
            messages.success(request,'Account was created for ' + username + ', please login')
            return redirect('loginPage')

    context = {'form':form}
    return render(request,'shopFront/register.html', context)
    
@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('homePage')
        else:
            messages.info(request, 'Username OR password is incorrect')
            

    context = {}
    return render(request,'shopFront/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('loginPage')

@login_required(login_url='loginPage')
def homePage(request):
    return render(request,'shopFront/home.html')

@login_required(login_url='loginPage')
@admin_only
def dashboard(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(payment_status='COMPLETE').count
    pending = orders.filter(payment_status='PENDING').count

    context = {'orders':orders,'customers':customers,
               'total_orders':total_orders,'delivered':delivered,
               'pending':pending}
    
    return render(request,'shopFront/dashboard.html',context)

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin'])
def customer(request,pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all()
    total_orders = orders.count()

    myFilter = OrderFilter(request.GET,queryset=orders)
    orders = myFilter.qs

    context = {'customer':customer,'orders':orders,'total_orders':total_orders,'myFilter':myFilter}
    return render(request,'shopFront/customer.html',context)

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin'])
def products(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'shopFront/products.html',context)

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin'])
def createOrder(request,pk):
    OrderFormSet = inlineformset_factory(Customer,Order,fields=('product','payment_status','note'))
    customer = Customer.objects.get(id=pk)
    formset =OrderFormSet(queryset=Order.objects.none(),instance=customer)
    #form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        formset =OrderFormSet(request.POST,instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect(reverse('dashboardPage'))
    context={'formset':formset}
    return render(request,'shopFront/order_form.html',context)

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin'])
def updateOrder(request,pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    print('ORDER:', order)
    if request.method == 'POST':
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect(reverse('dashboardPage'))
    context = {'form':form}
    return render(request,'shopFront/order_form.html',context)

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request,pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect(reverse('dashboardPage'))
    context = {'item':order}
    return render(request,'shopFront/delete.html',context)

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    orders = request.user.customer.order_set.all()

    total_orders = orders.count()
    delivered = orders.filter(payment_status='COMPLETE').count
    pending = orders.filter(payment_status='PENDING').count
    print('ORDERS:',orders)
    context = {'orders':orders,
               'total_orders':total_orders,'delivered':delivered,
               'pending':pending}
    return render(request,'shopFront/user.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def accountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES,instance=customer)
        if form.is_valid():
            form.save()
    
    context = {'form':form}
    return render(request,'shopFront/account_settings.html', context)

def contactus(request):
    context = {}
    return render(request,'shopFront/contactus.html')