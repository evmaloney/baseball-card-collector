from django.contrib import admin
from .models import Card, Winner, Case, Photo

# Register your models here.
admin.site.register(Card)
admin.site.register(Winner)
admin.site.register(Case)
admin.site.register(Photo)
