from django import forms
from django.forms import ModelForm
from .models import Ingredient, Dish, Category, DishIngredient, Order, OrderDish, Garcom
from django.contrib.auth.models import User, Group

class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ('name','exp_date','quantity','measure_unit','price','obs')

        labels = {
            'name':'Nome:',
            'exp_date':'Data de validade(aaaa-mm-dd):',
            'quantity':'Quantidade',
            'measure_unit':'Unidade de medida( Ex.: kg,gramas,litros,ml,unidades,etc)',
            'price':'Preço de compra:',
            'obs':'Observação:',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome'}),
            'exp_date': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Data de validade'}),
            'quantity': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Quantidade'}),
            'measure_unit': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Unidade de medida'}),
            'price': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Preço'}),
            'obs': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observação:'}),
        }

class DishIngredientForm(ModelForm):
    class Meta:
        model = DishIngredient
        fields = ('name','quantity','measure_unit')

        labels = {
            'name':'Ingrediente:',
            'quantity':'Quantidade',
            'measure_unit':'Unidade de medida( Ex.: kg,gramas,litros,ml,unidades,etc)',
        }

        widgets = {
            'name': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ingrediente'}),
            'quantity': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Quantidade'}),
            'measure_unit': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Unidade de medida'}),
        }

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ('category','name', 'price', 'description')

        labels = {
            'category': 'Categoria:',
            'name': 'Nome do prato:',
            'price': 'Preço:',
            'description': 'Descrição no cardápio:',
        }
        widgets = {
            'category': forms.Select(attrs={'class':'form-control', 'placeholder':'Categoria'}),
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome'}),
            'price': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Preço'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Descrição no cardápio'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        
        labels = {
            'name': 'Categoria:',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'categoria form-control', 'placeholder':'Categoria'}),
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderDish
        fields =('order','dish','quantity','obs')
        
        labels = {
            'order': 'Nº do Pedido:',
            'dish': 'Nome do prato:',
            'quantity': 'Quantidade:',
            'obs': 'Observação:',
        }
        widgets = {
            'order': forms.HiddenInput(),
            'dish': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Prato'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade'}),
            'obs': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição no cardápio'}),
        }


class AddGarcomForm(forms.ModelForm):
    cargo = forms.ChoiceField(choices=(), required=True)
    login = forms.ModelChoiceField(queryset=User.objects.all(), empty_label="Selecione um login", required=True)

    class Meta:
        model = Garcom
        fields = ('nome', 'cargo', 'salario', 'login')

        labels = {
            'nome': 'Nome:',
            'cargo': 'Cargo:',
            'salario': 'Salário:',
            'login': 'Login:',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'cargo': forms.Select(attrs={'class': 'form-control'}),
            'salario': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Salário'}),
            'login': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(AddGarcomForm, self).__init__(*args, **kwargs)
        self.fields['cargo'].choices = self.get_cargo_choices()

    def get_cargo_choices(self):
        group_choices = Group.objects.values_list('name', 'name')
        return [('', 'Selecione o cargo')] + list(group_choices)
    