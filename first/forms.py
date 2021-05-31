from django import forms
from first.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput


class ImageForm(forms.ModelForm):
    image = forms.ImageField(help_text='Profile Image')
    place = forms.CharField(max_length=256, required=False)
    name = forms.CharField(max_length=256, required=False)

    class Meta:
        model = Image
        fields = ('image', 'place', 'name')


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=100, widget=TextInput(attrs={'placeholder': 'Username'}))
    first_name = forms.CharField(max_length=100, widget=TextInput(attrs={'placeholder': 'First name'}))
    last_name = forms.CharField(max_length=100, widget=TextInput(attrs={'placeholder': 'Last name'}))
    email = forms.EmailField(max_length=150, widget=TextInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(max_length=150, widget=TextInput(attrs={'placeholder': 'Password', 'type': 'password'}))
    password2 = forms.CharField(max_length=150,
                                widget=TextInput(attrs={'placeholder': 'Password Confirmation', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2',)


class AvatarForm(forms.Form):
    avatar = forms.ImageField()


class ChangeTextField(forms.Form):
    field = forms.CharField(max_length=512)


class ChangeTextAresField(forms.Form):
    field = forms.CharField(label='Комментарий', required=True,
                            widget=forms.Textarea(
                                attrs={"class": "form-control mb-2", 'placeholder': 'Напишите что-нибудь...',
                                       'rows': '3', 'maxlength': '256'}))


class MessageForm(forms.ModelForm):
    text = forms.CharField(max_length=256, required=False)

    class Meta:
        model = Message
        fields = ('text',)


class OrderForm(forms.ModelForm):
    address = forms.CharField(max_length=256, required=True, widget=forms.TextInput(attrs={"id": "address_suggest", 'placeholder': 'Введите адрес...'}))
    date = forms.CharField(max_length=256, required=True, widget=forms.TextInput(attrs={"id": "order_time", "type": "datetime-local", 'placeholder': 'Выберите дату'}))
    info = forms.CharField(max_length=256, required=False, widget=forms.Textarea(
        attrs={"id": "order_info", "class": "form-control mb-2", 'placeholder': 'Напишите здесь свои пожелания к заявке',
               'rows': '3', "cols": "140",  'maxlength': '256'}))

    class Meta:
        model = Order
        fields = ('address', 'date', 'info')
