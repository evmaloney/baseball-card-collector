from django.shortcuts import render
from django.http import HttpResponse

class Card:
  def __init__(self, name, position, brand, year):
    self.name = name
    self.position = position
    self.brand = brand
    self.year = year

cards = [
  Card('Ken Griffey Jr.', 'CF', 'Topps', 1996),
  Card('Mark McGwire', '1B', 'Upper Deck', 1989),
  Card('Mariano Rivera', 'RP', 'Topps', 2001)
]
# Create your views here.


def home(request):
    return HttpResponse('<h1>hey</h1>')


def about(request):
    return render(request, 'about.html')

def cards_index(request):
  return render(request, 'cards/index.html', { 'cards': cards })