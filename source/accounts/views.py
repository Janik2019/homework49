from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.


def login_view(request):
    context = {}
    next = request.GET.get('next')
    request_page = request.session.setdefault('request_page', next)
    print(next)
    if request.method == 'POST':

        username = request.POST.get('username')

        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request_page)
        else:
            context['has_error'] = True

    return render(request, 'login.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('index')

