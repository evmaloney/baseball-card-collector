from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Card
from .forms import WinnerForm


class CardCreate(CreateView):
    model = Card
    fields = '__all__'
    success_url = '/cards/'


class CardUpdate(UpdateView):
    model = Card
    fields = ['position', 'seasons', 'brand', 'year']


class CardDelete(DeleteView):
    model = Card
    success_url = '/cards/'

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def cards_index(request):
    cards = Card.objects.all()
    return render(request, 'cards/index.html', {'cards': cards})


def cards_detail(request, card_id):
    card = Card.objects.get(id=card_id)
    winner_form = WinnerForm()
    return render(request, 'cards/detail.html', {
        'card': card,
        'winner_form': winner_form
    })


def add_winner(request, card_id):
    form = WinnerForm(request.POST)
    if form.is_valid():
        new_winner = form.save(commit=False)
        new_winner.card_id = card_id
        new_winner.save()
    return redirect('detail', card_id=card_id)
