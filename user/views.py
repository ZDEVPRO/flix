from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            messages.success(request, 'Muvoffaqiyatli ro`yxatdan o`tildi ' + first_name)
            return redirect('login')

    context = {'form': form}
    return render(request, 'signup/base.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Foydalanuvchi nomi yoki parol noto`g`ri')

    context = {}
    return render(request, 'signin/base.html', context)


def logout_func(request):
    logout(request)
    return HttpResponseRedirect('/users/login/')
