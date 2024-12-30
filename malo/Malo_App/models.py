from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import Group



# Create your models here.


class Ingredient(models.Model):
    name = models.CharField('Ingrediente', max_length=120) 
    '''nome do ingrediente'''
    exp_date = models.DateField('Data de validade') 
    '''data de validade'''
    quantity = models.FloatField('Quantidade') 
    '''quantidade que consta no estoque do ingrediente'''
    measure_unit = models.CharField('Unidade de medida',max_length=10) 
    '''unidade de medida utilzada ex.: kg, gramas, etc'''
    price = models.FloatField('Preço de compra(total)')
    '''preco de compra do ingrediente (total)'''
    obs = models.TextField('Observação', blank=True)
    '''ex.: marca parmalate, deixar na geladeira, etc'''

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField('Categoria', max_length=120)
    '''Nome da categoria'''
    def __str__(self):
        return self.name 

class Dish(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField('Nome do prato', max_length=120)
    '''Nome do prato'''
    price = models.FloatField('Preço de venda')
    '''Preço do prato'''
    description = models.TextField('Descrição')
    '''Descrição do prato'''

    def get_ingredients_children(self):
        return self.dishingredients_set.all()

    def __str__(self):
        return self.name

class DishIngredient(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    '''Prato que ele participa'''
    name = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    '''nome do ingrediente'''
    quantity = models.FloatField('Quantidade')
    '''quantidade que consta no estoque do ingrediente'''
    measure_unit = models.CharField('Unidade de medida',max_length=10)
    '''unidade de medida utilzada ex.: kg, gramas, etc'''

    def __str__(self):
        return self.name


class Mesa(models.Model):
    numero = models.IntegerField(unique=True)
    descricao = models.CharField(max_length=100, default='Mesa')

    @classmethod
    def proximo_numero(cls):
        ultima_mesa = cls.objects.order_by('-numero').first()
        numero = ultima_mesa.numero + 1 if ultima_mesa else 1
        return numero

    def __str__(self):
        return f'Mesa {self.numero}'

class Order(models.Model):
    numero = models.IntegerField(unique=True)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE, null=True, blank=True)
    total_price_local = models.FloatField(default=0)

    @classmethod
    def proximo_numero(cls):
        ultimo_pedido = cls.objects.order_by('-numero').first()
        numero = ultimo_pedido.numero + 1 if ultimo_pedido else 1
        return numero

    def __str__(self):
        return f'Pedido {self.numero}'
    
class OrderDish(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    obs = models.TextField('Observação', blank=True, null=True)

    def __str__(self):
        return str(self.dish)

class Garcom(models.Model):
    nome = models.CharField('Nome', max_length=120)
    cargo = models.CharField('Cargo', max_length=120)
    salario = models.FloatField('Salário')
    login = models.CharField('Login', max_length=120)

    def __str__(self):
        return self.nome

class Invoice(models.Model):
    name = models.CharField('nome',max_length=5)
    exp_employees = models.FloatField('Despesas funcionarios')
    tips = models.FloatField('servico')
    billing = models.FloatField('faturamento')
    feedstock = models.FloatField('insumos')