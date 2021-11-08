from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm
from first.forms import *
from first.models import *
from django.utils import timezone


def show_start_page(request):
    images = Image.objects.all()
    orders = Order.objects.all()

    context = {
        "images": images,
        "orders": orders
    }
    return render(request, 'index.html', context)


def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.profile.first_name = form.cleaned_data.get('first_name')
        user.profile.last_name = form.cleaned_data.get('last_name')
        user.profile.email = form.cleaned_data.get('email')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'singup.html', {'form': form})


@login_required
def view_profile(request):
    images = Image.objects.all()

    context = {
        "images": images,
        "profile": request.user.profile
    }
    return render(request, 'profile.html', context)


@login_required
def upload_image(request):
    context = {}
    if request.method == 'POST':
        f = ImageForm(request.POST, request.FILES)
        if f.is_valid():
            image = f.save()
            image.author = request.user
            image.save()
        else:
            context['form'] = f
    else:
        context['form'] = ImageForm()
    return render(request, "profile.html", context)


@login_required
def change_avatar(request):
    context = {}
    if request.method == 'POST':
        f = AvatarForm(request.POST, request.FILES)
        if f.is_valid():
            request.user.profile.image = f.data['avatar']
            request.user.profile.save()
        else:
            context['form'] = f
    else:
        context['form'] = AvatarForm()
    return render(request, "profile.html", context)


@login_required
def like(request, image_id):
    image = Image.objects.get(id=image_id)
    new_like = Like(author=request.user, image=image)
    new_like.save()
    return redirect('/')


@login_required
def view_edit_page(request):
    context = {}
    if 'username_change' in request.POST:
        f = ChangeTextField(request.POST)
        if f.is_valid():
            request.user.username = f.data['field']
            request.user.save()
        else:
            context['form'] = f
    elif 'first_name_change' in request.POST:
        f = ChangeTextField(request.POST)
        if f.is_valid():
            request.user.profile.first_name = f.data['field']
            request.user.profile.save()
        else:
            context['form'] = f
    elif 'last_name_change' in request.POST:
        f = ChangeTextField(request.POST)
        if f.is_valid():
            request.user.profile.last_name = f.data['field']
            request.user.profile.save()
        else:
            context['form'] = f
    if 'bio_change' in request.POST:
        f = ChangeTextAresField(request.POST)
        if f.is_valid():
            request.user.profile.bio = f.data['field']
            request.user.profile.save()
        else:
            context['form'] = f
    return render(request, 'edit.html', context)


@login_required
def become_user(request):
    request.user.is_staff = 0
    request.user.save()

    images = Image.objects.all()

    likes = list()
    for i in images:
        likes.append(Like.get_all_likes_of_photo(i.id))
    context = {
        "images": images,
        "likes": likes,
        "profile": request.user.profile
    }

    return render(request, "profile.html", context)


@login_required
def become_photographer(request):
    request.user.is_staff = 1
    request.user.save()

    images = Image.objects.all()

    likes = list()
    for i in images:
        likes.append(Like.get_all_likes_of_photo(i.id))
    context = {
        "images": images,
        "likes": likes,
        "profile": request.user.profile
    }

    return render(request, "profile.html", context)


def view_user_profile(request, user_need):
    context = {'user': User.objects.get(id=user_need)}
    if request.user.id == user_need:
        return view_profile(request)
    if "write_message" in request.POST:
        if request.method == 'POST':
            f = MessageForm(request.POST)
            if f.is_valid():
                message = f.save()
                message.author = request.user
                message.receiver = User.objects.get(id=user_need)
                message.save()
            else:
                context['form'] = f
        else:
            context['form'] = MessageForm()
    return render(request, "user_profile.html", context)


@login_required
def order(request):
    context = {}
    if request.method == 'POST':
        f = OrderForm(request.POST)
        if f.is_valid():
            address1 = request.POST.get('address')
            date1 = request.POST.get('date')
            info1 = request.POST.get('info')
            order1 = Order(address=address1, date=date1, info=info1, author=request.user)
            order1.save()
        else:
            context['form'] = f
    else:
        context['form'] = OrderForm()
    return render(request, "order.html", context)


@login_required
def messages(request):
    context = {}
    return render(request, "messages.html", {})


@login_required
def show_messages_page(request):
    context = {}
    return render(request, "messages.html", {})


def show_list_page(request):
    images = Image.objects.all()

    likes = list()
    for i in images:
        likes.append(Like.get_all_likes_of_photo(i.id))
    context = {
        "images": images,
        "likes": likes,
    }
    return render(request, "list.html", context)


@login_required
def show_notifications_page(request):
    orders = Order.objects.all()
    context = {
        "orders": orders
    }
    return render(request, 'notifications.html', context)