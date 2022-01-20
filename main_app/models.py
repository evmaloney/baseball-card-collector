from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

MATERIALS = (
    ('P', 'Plastic'),
    ('G', 'Glass')
)

LEAGUES = (
    ('NL', 'National League'),
    ('AL', 'American League')
)

AWARDS = (
    ('MVP', 'MVP'),
    ('CY', 'Cy Young'),
    ('ROTY', 'Rookie of the Year')
)

# Create your models here.


class Case(models.Model):
    type = models.CharField(max_length=100)
    material = models.CharField(
        max_length=1,
        choices=MATERIALS,
        default=MATERIALS[0][0]
    )

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse('cases_detail', kwargs={'pk': self.id})


class Card(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    seasons = models.IntegerField()
    brand = models.CharField(max_length=100)
    year = models.IntegerField()
    cases = models.ManyToManyField(Case)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'card_id': self.id})

    def should_get_case(self):
        return self.seasons == 0


class Winner(models.Model):
    year = models.IntegerField()
    league = models.CharField(
        max_length=2,
        choices=LEAGUES,
        default=LEAGUES[0][0]
    )
    award = models.CharField(
        max_length=4,
        choices=AWARDS,
        default=AWARDS[0][0]
    )
    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.year} {self.get_league_display()} {self.get_award_display()}"

    class Meta:
        ordering = ['-year']


class Photo(models.Model):
    url = models.CharField(max_length=200)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for card_id: {self.card_id} @{self.url}"
