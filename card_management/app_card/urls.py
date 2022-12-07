from django.urls import path
from .views import MainView, GenerateFormView, CardListView, CardDetailView, DeleteCardView, SearchCardListView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('add_new/', GenerateFormView.as_view(), name='generate'),
    path('card/', CardListView.as_view(), name='card_list'),
    path('card/<int:pk>/', CardDetailView.as_view(), name='main'),
    path('card/delete/<int:card_id>/', DeleteCardView.as_view(), name='delete'),
    path('card/search/', SearchCardListView.as_view(), name='search')
]
