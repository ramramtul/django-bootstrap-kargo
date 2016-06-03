from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db import transaction
from django.shortcuts import render, redirect
from orders.forms import ODOrderForm
from orders.forms import NCustomerForm
from orders.models import ODOrder
from orders.models import Detcus


def index(request):
    """
    Handle index page for order
    """

    return render(request, 'order/index.html')

def customer(request):
    """
    Showing list of customer in home page
    """

    # query on all order records
    orders = Detcus.objects.all()

    # structured order into simple dict, 
    # later on, in template, we can render it easily, ex: {{ orders }}
    data = {'orderku': orders}

    return render(request, 'customer/customer.html', data)

def create_customer(request):
    """
    Handle new customer creation
    """

    # Initial form and data
    data = {
        'form': NCustomerForm(),
    }

    # if user submit data from this page, we capture the POST data and save it
    if request.method == 'POST':

        # wrap POST data with the form
        form = NCustomerForm(request.POST)

        # Transaction savepoint (good to provide rollback data)
        sid = transaction.savepoint()

        if form.is_valid():

            # wrap form result into dict ODOrder model fields structure 
            orderku_data = {
                'name': form.cleaned_data.get('name'),
                'email': form.cleaned_data.get('email'),
                'phone': form.cleaned_data.get('phone'),
                'address': form.cleaned_data.get('address'),
            }

            try:
                Detcus.objects.create(**orderku_data)
            except:
                transaction.savepoint_rollback(sid)
                messages.error(request, "Oops! Something wrong happened!")

            messages.info(request, "A new record has been created!")

    return render(request, 'customer/create_customer.html', data)

def edit_customer(request, uuid=None):
    """
    How to remove customer
    """
    if not uuid:
        return redirect(reverse('customer:customer'))

    # validate given UUID match with record in database
    try:
        order = Detcus.objects.get(uuid=uuid)
    except Detcus.DoesNotExist:
        messages.error(request, "Record not found!")
        return redirect(reverse('order:customer'))

    data = {
        'form': NCustomerForm(instance=order),
    }

    # if user submit data from this page, we capture the POST data and save it
    if request.method == 'POST':

        # wrap POST data with the form
        form = NCustomerForm(request.POST, instance=order)

        # Transaction savepoint (good to provide rollback data)
        sid = transaction.savepoint()

        if form.is_valid():

            try:
                form.save()
            except:
                transaction.savepoint_rollback(sid)
                messages.error(request, "Oops! Something wrong happened!")

            messages.info(request, "Record has been updated!")

    return render(request, 'customer/edit_customer.html', data)

def delete_customer(request, uuid=None):
    """
    How to remove customer
    """
    if uuid:

        # finding given UUID to match order in database
        try:
            order = Detcus.objects.get(uuid=uuid)
        except Detcus.DoesNotExist:
            messages.error(request, "Customer not found")
        else:
            # delete order from database
            order.delete()
            messages.success(request, 'Order "{}" has been deleted'.format(order.name))

    return redirect(reverse('order:customer'))


def management(request):
    """
    Showing list of order in management home page
    """

    # query on all order records
    orders = ODOrder.objects.all()

    # structured order into simple dict, 
    # later on, in template, we can render it easily, ex: {{ orders }}
    data = {'orders': orders}

    return render(request, 'order/management.html', data)


def create_order(request):
    """
    Handle new order creation
    """

    # Initial form and data
    data = {
        'form': ODOrderForm(),
    }

    # if user submit data from this page, we capture the POST data and save it
    if request.method == 'POST':

        # wrap POST data with the form
        form = ODOrderForm(request.POST)

        # Transaction savepoint (good to provide rollback data)
        sid = transaction.savepoint()

        if form.is_valid():

            # wrap form result into dict ODOrder model fields structure 
            order_data = {
                'name': form.cleaned_data.get('name'),
                'phone': form.cleaned_data.get('phone'),
                'price': form.cleaned_data.get('price'),
            }

            try:
                ODOrder.objects.create(**order_data)
            except:
                transaction.savepoint_rollback(sid)
                messages.error(request, "Oops! Something wrong happened!")

            messages.info(request, "A new record has been created!")

    return render(request, 'order/create_order.html', data)


def edit_order(request, uuid=None):
    """
    How to remove order
    """
    if not uuid:
        return redirect(reverse('order:management'))

    # validate given UUID match with record in database
    try:
        order = ODOrder.objects.get(uuid=uuid)
    except ODOrder.DoesNotExist:
        messages.error(request, "Record not found!")
        return redirect(reverse('order:management'))

    data = {
        'form': ODOrderForm(instance=order),
    }

    # if user submit data from this page, we capture the POST data and save it
    if request.method == 'POST':

        # wrap POST data with the form
        form = ODOrderForm(request.POST, instance=order)

        # Transaction savepoint (good to provide rollback data)
        sid = transaction.savepoint()

        if form.is_valid():

            try:
                form.save()
            except:
                transaction.savepoint_rollback(sid)
                messages.error(request, "Oops! Something wrong happened!")

            messages.info(request, "Record has been updated!")

    return render(request, 'order/edit_order.html', data)


def delete_order(request, uuid=None):
    """
    How to remove order
    """
    if uuid:

        # finding given UUID to match order in database
        try:
            order = ODOrder.objects.get(uuid=uuid)
        except ODOrder.DoesNotExist:
            messages.error(request, "Order not found")
        else:
            # delete order from database
            order.delete()
            messages.success(request, 'Order "{}" has been deleted'.format(order.name))

    return redirect(reverse('order:management'))
