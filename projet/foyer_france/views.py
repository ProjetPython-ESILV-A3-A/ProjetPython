from foyer_france.helpers import get_hash_password
from foyer_france.models import Product
from .forms import LoginForm, RegisterForm
from .models import HouseHold, Command
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render


def login(request):
    # if we get a post method
    if request.method == 'POST':
        form = LoginForm(request.POST,auto_id=False)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                house_hold = HouseHold.objects.get(email=email, password=get_hash_password(password))
                request.session['email'] = email
                # todo redirect to the page of products
            except ObjectDoesNotExist:
                pass  # todo handle the user doesn't exists

        else:
            pass

    return render(request, 'login.html')


def register(request):
    # if we get a post method
    if request.method == 'POST':
        form = RegisterForm(request.POST, auto_id=False)
        if form.is_valid():
            manager_name = form.cleaned_data['managerName']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phoneNumber']
            password = form.cleaned_data['password']
            address = form.cleaned_data['address']
            postal_code = form.cleaned_data['postalCode']
            total_members = form.cleaned_data['totalMembers']

            house_hold, created = HouseHold.objects.get_or_create(
                email=email,
                defaults={
                    'managerName': manager_name,
                    'phoneNumber': phone_number,
                    'password': get_hash_password(password),
                    'address': address,
                    'postalCode': postal_code,
                    'totalMembers': total_members,
                }
            )
            if created:
                request.session['email'] = email
                pass  # todo return to the products page
            else:
                pass  # todo the user with this email exists
        else:
            print('error occur')

    return render(request, 'signup.html')


def cart_panel(request):
    email = request.session['email']
    if request.method == 'DELETE':
        product_name = request.cleaned_data['product_name']
        try:
            command = Command.objects.get(houseHold=email, product=product_name)
            command.delete()
            # todo send the answe
        except ObjectDoesNotExist:
            pass  # todo return an error

    elif request.method == 'POST':
        pass  # todo redirect to another service

    products = Command.objects.get(houseHold=email)
    # todo render the cart view
    pass


def add_to_panel(request):
    email = request.session['email']
    if request.method == 'POST':
        product_name = request.cleaned_data['product_name']
        quantity = request.cleaned_data['quantity']
        command, created = Command.objects.get_or_create(
            houseHold=email,
            product=product_name,
            defaults={
                quantity: quantity
            }
        )
        if created:
            pass  # todo send the created response
        else:
            command.quantity += quantity
            command.save()
            pass  # todo send updated response

    products = Product.objects.all()
    pass  # todo send all the product to the view
