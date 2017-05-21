from django.http import HttpResponse , Http404
from django.shortcuts import render , redirect ,get_object_or_404
from django.views.generic import *
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from .forms import UserrForm
from django.views.generic import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required



def inscription(request):

    form=UserrForm(request.POST)
    if form.is_valid():
        u=User()
        u.username=form.cleaned_data["username"]
        u.email=form.cleaned_data["email"]
        x=form.cleaned_data["password"]
        u.set_password(x)
        u.save()
        return render("http://127.0.0.1:8000")

    return redirect("http://127.0.0.1:8000/login",locals())

@login_required
def profile(request):

    return redirect("http://127.0.0.1:8000/ui")

def logout(request):
    response = HttpResponseRedirect('http://127.0.0.1:8000/')
    response.delete_cookie('sessionid')
    return response
