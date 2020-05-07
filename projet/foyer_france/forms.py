from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(label='email')
    password = forms.CharField(label='password')


class RegisterForm(forms.Form):
    managerName = forms.CharField(label='name', max_length=100)
    email = forms.EmailField(label='email')
    phoneNumber = forms.CharField(label='phoneNumber', max_length=100)
    password = forms.CharField(label='password', max_length=100)
    address = forms.CharField(label='address', max_length=100)
    postalCode = forms.CharField(label='postalCode', max_length=100)
    totalMembers = forms.IntegerField(label='members')

