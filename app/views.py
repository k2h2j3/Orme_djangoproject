from django.shortcuts import render
from django.views import View
# from django.urls import reverse_lazy, reverse
from user.models import User

class IndexMain(View):
    def get(self, request):
        return render(request, 'index.html')

def hello(request):
    context = {}

    login_session = request.session.get('login_session', '')

    if login_session == '':
        context['login_session'] = False
    else:
        context['login_session'] = True

    return render(request, 'index.html', context)