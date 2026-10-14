from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Genero(models.Model):
    nome = models.CharField('Gênero', max_length=100)

    def __str__(self):
        return self.nome

class Plataforma(models.Model):
    nome = models.CharField('Plataforma', max_length=100)

    def __str__(self):
        return self.nome

class Jogo(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    data_lancamento = models.DateField('Data de lançamento')
    foto = models.ImageField()
    destaque = models.BooleanField('Destaque', default=False)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    plataforma = models.ManyToManyField(Plataforma)

    def __str__(self):
        return self.nome

class Avaliacao(models.Model):
    nome_visitante = models.CharField('Nome visitante', max_length=100)
    nota = models.DecimalField('Nota', validators=[MinValueValidator(1), MaxValueValidator(5)]) #usamos para poder definir o valor mínimo e o valor máximo da nota
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    comentario = models.TextField('Comentário')

    def __str__(self):
        return f'{self.nome_visitante} - {self.jogo.nome} ({self.nota}/5)'

    
