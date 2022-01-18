from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cards/', views.cards_index, name='index'),
    path('cards/<int:card_id>', views.cards_detail, name="detail"),
    path('cards/create/', views.CardCreate.as_view(), name='cards_create'),
    path('cards/<int:pk>/update/', views.CardUpdate.as_view(), name='cards_update'),
    path('cards/<int:pk>/delete/', views.CardDelete.as_view(), name='cards_delete'),
    path('cards/<int:card_id>/add_winner/',
         views.add_winner, name='add_winner'),
    path('cards/<int:card_id>/assoc_case/<int:case_id>/',
         views.assoc_case, name='assoc_case'),
    path('cases/', views.CaseList.as_view(), name='cases_index'),
    path('cases/<int:pk>/', views.CaseDetail.as_view(), name='cases_detail'),
    path('cases/create/', views.CaseCreate.as_view(), name='cases_create'),
    path('cases/<int:pk>/update/', views.CaseUpdate.as_view(), name='cases_update'),
    path('cases/<int:pk>/delete/', views.CaseDelete.as_view(), name='cases_delete'),
]
