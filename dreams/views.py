from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.forms import ModelForm
from dreams.models import Dream


class DreamForm(ModelForm):
    class Meta:
        model = Dream
        fields = ['dream_audio', 'dream_text',]
        exclude = ['user']

def base(request, template_name='base.html'):
    return render(request, template_name)


def home(request, template_name='home.html'):
    return render(request, template_name)

def dream_view(request, pk, template_name='dream_view.html'):
    pass

def dream_create(request, template_name="dream_form.html"):
    pass

def dream_update(request, pk, template_name='dream_form.html'):
    pass

def dream_delete(request, pk, template_name='dream_confirm_delete.html'):
    pass
