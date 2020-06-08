from django import forms
from newsite.models import AttTable

CAT1_CHOICES = (('liter', '인문'), ('nature', '자연'), ('leisure', '레저'))
CAT2_CHOICES = (('park', '공원'), ('mountain', '산'), ('seashore', '연안'), ('history', '역사'), ('culture', '문화'), ('archi', '건축'), ('activity', '활동'), ('healing', '힐링'))

class CatogoryForm(forms.Form):
    cat1 = forms.ChoiceField(required = False, widget = forms.CheckboxSelectMultiple, choices = CAT1_CHOICES)
    cat2 = forms.ChoiceField(required = False, widget = forms.CheckboxSelectMultiple, choices = CAT2_CHOICES)

