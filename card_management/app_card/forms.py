from django import forms


class GenerateForm(forms.Form):
    CHOISES_TERM = [('12', '1 год'), ('6', '6 месяцев'), ('1', '1 месяц')]
    series = forms.CharField(max_length=10)
    count = forms.IntegerField(min_value=1)
    term = forms.ChoiceField(choices=CHOISES_TERM)
