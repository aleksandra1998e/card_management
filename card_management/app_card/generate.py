from .models import Card
from datetime import datetime, timedelta


def generate(card_series, count, term):
    for i in range(count):
        card = Card()
        card.series = card_series
        card.number = i
        card.release_date = datetime.now()
        if term == '12':
            card.end_date = datetime.now()+timedelta(days=365)
        elif term == '6':
            card.end_date = datetime.now()+timedelta(days=183)
        elif term == '1':
            card.end_date = datetime.now()+timedelta(days=30)
        card.save()
