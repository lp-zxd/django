from django import forms
class segjform(forms.Form):
    GName=forms.CharField(max_length=20)
class semeform(forms.Form):
    MName=forms.CharField(max_length=20)
class addmeform(forms.Form):
    MName = forms.CharField(max_length=20)
    Price= forms.DecimalField(max_digits=10, decimal_places=2)
    Many=forms.IntegerField()
    About = forms.CharField(max_length=100, required=False)
class upmeform(forms.Form):
    ID=forms.IntegerField(max_value=20)
    MName = forms.CharField(max_length=20)
    Price= forms.DecimalField(max_digits=10, decimal_places=2)
    Many=forms.IntegerField()
    About = forms.CharField(max_length=100, required=False)
class addgjform(forms.Form):
    GName = forms.CharField(max_length=20)
    Price= forms.DecimalField(max_digits=10, decimal_places=2)
    Many=forms.IntegerField()
    About = forms.CharField(max_length=100, required=False)
class upgjform(forms.Form):
    ID=forms.IntegerField(max_value=20)
    GName = forms.CharField(max_length=20)
    Price= forms.DecimalField(max_digits=10, decimal_places=2)
    Many=forms.IntegerField()
    About = forms.CharField(max_length=100, required=False)