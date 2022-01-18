from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Card, Case, Photo
from .forms import WinnerForm
import os
import uuid
import boto3


class CardCreate(CreateView):
    model = Card
    fields = ['name', 'position', 'seasons', 'brand', 'year']
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


def cards_detail(request, card_id):
    card = Card.objects.get(id=card_id)
    cases_card_doesnt_have = Case.objects.exclude(
        id__in=card.cases.all().values_list('id'))
    winner_form = WinnerForm()
    return render(request, 'cards/detail.html', {
        'card': card, 'winner_form': winner_form,
        'cases': cases_card_doesnt_have
    })


def assoc_case(request, card_id, case_id):
    Card.objects.get(id=card_id).cases.add(case_id)
    return redirect('detail', card_id=card_id)


def add_photo(request, card_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + \
            photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, card_id=card_id)
        except:
            print('An error occurred uploading file to S3')
        return redirect('detail', card_id=card_id)


class CaseList(ListView):
    model = Case


class CaseDetail(DetailView):
    model = Case


class CaseCreate(CreateView):
    model = Case
    fields = '__all__'


class CaseUpdate(UpdateView):
    model = Case
    fields = ['type', 'material']


class CaseDelete(DeleteView):
    model = Case
    success_url = '/cases/'
