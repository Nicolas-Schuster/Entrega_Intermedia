from django import forms

class ElectrodomesticosForm(forms.Form):
    name =forms.CharField(max_length=50)
    price = forms.FloatField()
    description = forms.CharField(max_length=100)
    shipping_cost = forms.FloatField()
    stock = forms.BooleanField(required=False)



class TecnologiaForm(forms.Form):
    name =forms.CharField(max_length=50)
    price = forms.FloatField()
    description = forms.CharField(max_length=100)
    shipping_cost = forms.FloatField()
    stock = forms.BooleanField(required=False)



class HogarForm(forms.Form):
    name =forms.CharField(max_length=50)
    price = forms.FloatField()
    description = forms.CharField(max_length=100)
    shipping_cost = forms.FloatField()
    stock = forms.BooleanField(required=False)



class HerramientasForm(forms.Form):
    name =forms.CharField(max_length=50)
    price = forms.FloatField()
    description = forms.CharField(max_length=100)
    shipping_cost = forms.FloatField()
    stock = forms.BooleanField(required=False)



class IndumentariaForm(forms.Form):
    name =forms.CharField(max_length=50)
    price = forms.FloatField()
    description = forms.CharField(max_length=100)
    shipping_cost = forms.FloatField()
    stock = forms.BooleanField(required=False)



class PerfumeriaForm(forms.Form):
    name =forms.CharField(max_length=50)
    price = forms.FloatField()
    description = forms.CharField(max_length=100)
    shipping_cost = forms.FloatField()
    stock = forms.BooleanField(required=False)



class AutomotorForm(forms.Form):
    name =forms.CharField(max_length=50)
    price = forms.FloatField()
    description = forms.CharField(max_length=100)
    shipping_cost = forms.FloatField()
    stock = forms.BooleanField(required=False)