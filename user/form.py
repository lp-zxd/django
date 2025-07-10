from django import forms

class Loginform (forms.Form):
    username=forms.CharField(max_length=20)
    password=forms.CharField(max_length=20)
class Drseform(forms.Form):
    Drname=forms.CharField(max_length=20)
class addDrform(forms.Form):
    DrName = forms.CharField(max_length=20)
    xb=forms.CharField(max_length=2)
    zw=forms.CharField(max_length=20)
    ks=forms.CharField(max_length=20)
    sr=forms.DateField()
    gzsj=forms.DateField()
    jdwsj=forms.DateField()
    qian=forms.IntegerField(min_value=0)
    about=forms.CharField(max_length=200)
class upDrform(forms.Form):
    ID=forms.IntegerField(min_value=0)
    DrName = forms.CharField(max_length=20)
    xb=forms.CharField(max_length=2)
    zw=forms.CharField(max_length=20)
    ks=forms.CharField(max_length=20)
    sr=forms.DateField()
    gzsj=forms.DateField()
    jdwsj=forms.DateField()
    qian=forms.IntegerField(min_value=0)
    about=forms.CharField(max_length=200)