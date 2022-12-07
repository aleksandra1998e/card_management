from django.db import models


class Card(models.Model):

    STATUS_CHOICES = [('a', 'active'), ('e', 'inactive'), ('n', 'expired')]
    series = models.CharField(null=False, max_length=10, verbose_name='серия')
    number = models.IntegerField(null=False, verbose_name='номер')
    release_date = models.DateTimeField(verbose_name='дата выпуска')
    end_date = models.DateTimeField(verbose_name='дата окончания', db_index=True)
    status = models.CharField(max_length=1, default='e', choices=STATUS_CHOICES, verbose_name='статус')

    class Meta:
        ordering = ['status', 'release_date']
        unique_together = ('series', 'number')

    def __str__(self):
        return '{} {}'.format(self.series, self.number)


class Purchase(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name='дата добавления')
    amount = models.FloatField(null=False, verbose_name='сумма')
    card = models.ForeignKey('card', null=False, related_name='purchases', on_delete=models.CASCADE, verbose_name='карта')

    class Meta:
        ordering = ['date']

    def __str__(self):
        return '{} {}'.format(self.card, self.amount)
