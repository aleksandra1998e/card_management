from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View, generic
from django.utils import timezone

from .models import Card
from .forms import GenerateForm
from .generate import generate


class MainView(View):
    def get(self, request):
        return render(request, 'app_card/main.html', {})


class GenerateFormView(View):
    def get(self, request):
        generate_form = GenerateForm()
        return render(request, 'app_card/generate.html', {'generate_form': generate_form})

    def post(self, request):
        generate_form = GenerateForm(request.POST)
        if generate_form.is_valid():
            card_series = request.POST.get('series')
            count = int(request.POST.get('count'))
            term = request.POST.get('term')
            generate(card_series, count, term)
            return HttpResponseRedirect('/')
        return redirect(GenerateFormView)


class CardListView(generic.ListView):
    data = timezone.now()
    cards = Card.objects.order_by('end_date')
    for card in cards:
        if card.end_date <= data:
            card.status = 'n'
            card.save()
        else:
            break
    model = Card
    template_name = 'app_card/card_list.html'
    context_object_name = 'card_list'


class CardDetailView(generic.DetailView):
    model = Card
    template_name = 'app_card/card_detail.html'

    def post(self, request, pk):
        card = Card.objects.get(id=pk)
        if card.status == 'e':
            card.status = 'a'
        elif card.status == 'a':
            card.status = 'e'
        card.save()
        return HttpResponseRedirect('/card/{}/'.format(pk))


class DeleteCardView(View):
    def get(self, request, card_id):
        card = Card.objects.get(id=card_id)
        card.delete()
        return HttpResponseRedirect('/card/')


class SearchCardListView(View):
    def post(self, request):
        req_text = request.POST.get('req')
        field = request.POST.get('fields')
        if field == 'series':
            cards = Card.objects.filter(series=req_text).all()
        elif field == 'number':
            req_text = int(req_text)
            cards = Card.objects.filter(number=req_text).all()
        else:
            req_text = req_text.title()
            if req_text == "Просрочена":
                req_text = 'n'
            elif req_text == "Активна":
                req_text = 'a'
            elif req_text == "Неактивна":
                req_text = 'e'
            cards = Card.objects.filter(status=req_text).all()
        return render(request, 'app_card/card_search.html', {'card_list': cards})

