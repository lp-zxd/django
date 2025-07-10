from django import forms
class pasefrom(forms.Form):
    PaName=forms.CharField(max_length=20)
class addpafrom(forms.Form):
    PaName=forms.CharField(max_length=20)
    Gender=forms.CharField(max_length=2)
    KName=forms.CharField(max_length=20)
    Condition=forms.CharField(max_length=200)
    Dr=forms.CharField(max_length=20)
    BID=forms.IntegerField(min_value=0)
class uppafrom(forms.Form):
    ID=forms.IntegerField(min_value=0)
    PaName=forms.CharField(max_length=20)
    Gender=forms.CharField(max_length=2)
    KName=forms.CharField(max_length=20)
    Condition=forms.CharField(max_length=200)
    Dr=forms.CharField(max_length=20)
    BID=forms.IntegerField(min_value=0)