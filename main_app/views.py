from django.shortcuts import render
from .models import Card


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
    return render(request, 'cards/detail.html', {'card': card})
