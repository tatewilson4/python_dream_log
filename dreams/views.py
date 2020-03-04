from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.forms import ModelForm
from dreams.models import Dream


class DreamForm(ModelForm):
    class Meta:
        model = Dream
        fields = ['title', 'dream_audio', 'dream_text',]
        exclude = ['user']

def base(request, template_name='base.html'):
    return render(request, template_name)


def home(request, template_name='home.html'):
    user = request.user
    dream = Dream.objects.filter(user=user)
    data = {}
    data['object_list'] = dream
    return render(request, template_name, data)

def dream_view(request, pk, template_name='dream_view.html'):
    dream = get_object_or_404(Dream, pk=pk)
    return render(request, template_name, {'object': dream})

def dream_create(request, template_name="dream_form.html"):
    form = DreamForm(request.POST, request.FILES)
    if form.is_valid():
        dream = form.save(commit=False)
        dream.user = request.user
        dream.save()
        return redirect('home')
    return render(request, template_name, {'form': form})

def dream_update(request, pk, template_name='dream_form.html'):
    dream = get_object_or_404(Dream, pk=pk)
    form = DreamForm(request.POST, request.FILES, instance=dream)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, template_name, {'form': form})

def dream_delete(request, pk, template_name='dream_confirm_delete.html'):
    dream = get_object_or_404(Dream, pk=pk)
    if request.method == 'POST':
        dream.delete()
        return redirect('home')
    return render(request, template_name, {'object': dream})
