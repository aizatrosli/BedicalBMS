from django.shortcuts import render


def mainpage(request, *args, **kwargs):
    print(dir(request))
    if request.user.is_anonymous:
        return login(request, *args, **kwargs)
    else:
        return render(request, 'index.html', {})


def profile(request, *args, **kwargs):
    return render(request, 'profile.html', {})


def login(request, *args, **kwargs):
    return render(request, 'login.html', {})
