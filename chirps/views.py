from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Chirp

def home(request):
    context = {
        'chirps': Chirp.objects.all()
    }
    return render(request, 'chirps/home.html', context)

class ChirpListView(ListView):
    model = Chirp
    template_name = 'chirps/home.html'
    context_object_name = 'chirps'
    ordering = ['-date_posted']
    paginate_by = 5 # paginate by 5 chirp per page

class UserChirpListView(ListView):
    model = Chirp
    template_name = 'chirps/user_chirps.html'
    context_object_name = 'chirps'
    paginate_by = 5 # paginate by 5 chirp per page

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Chirp.objects.filter(author=user).order_by('-date_posted')

class ChirpDetailView(DetailView):
    model = Chirp
    template_name = 'chirps/chirp_detail.html'


class ChirpCreateView(LoginRequiredMixin, CreateView):
    model = Chirp
    template_name = 'chirps/chirp_form.html'
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ChirpUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Chirp
    template_name = 'chirps/chirp_form.html'
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        chirp = self.get_object()
        if self.request.user == chirp.author:
            return True
        return False


class ChirpDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Chirp
    template_name = 'chirps/chirp_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        chirp = self.get_object()
        if self.request.user == chirp.author:
            return True
        return False

def about(request):
    return render(request, 'chirps/about.html', {'title': 'About'})