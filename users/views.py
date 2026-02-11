from django.shortcuts import render

from django.contrib.auth import logout
from django.shortcuts import redirect


def logout_view(request):
    logout(request)  # <-- ОДНА СТРОКА для завершения сессии
    return redirect('users:login')
