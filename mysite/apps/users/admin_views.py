from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.template.response import TemplateResponse

from mysite.apps.users.forms import LoginForm


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return HttpResponse('success!')
    else:
        form = LoginForm()
    return TemplateResponse(request, 'login.html', {'form': form})


