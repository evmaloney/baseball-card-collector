from django.db import models
from django.urls import reverse

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


class Card(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    seasons = models.IntegerField()
    brand = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'card_id': self.id})


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
