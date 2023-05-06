from django.db import models
from django.apps import apps
AppConfig = apps.get_app_config('storyapp')

class Componente(models.Model):
    class Meta:
        app_label = 'storyapp'
        
    TIPO_CHOICES = (
        ('video', 'Video'),
        ('imagen', 'Imagen'),
        ('letra', 'Letra'),
    )
    tipo = models.CharField(max_length=6, choices=TIPO_CHOICES)
    contenido = models.TextField()
    duracion = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.tipo

class Pregunta(models.Model):
    texto = models.CharField(max_length=200)
    opcion_a = models.CharField(max_length=100)
    opcion_b = models.CharField(max_length=100)
    opcion_c = models.CharField(max_length=100)
    opcion_d = models.CharField(max_length=100)
    respuesta_correcta = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])

    def __str__(self):
        return self.texto

class Resultado(models.Model):
    story = models.ForeignKey('Story', on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta_elegida = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])

    def __str__(self):
        return f'{self.story.titulo} - {self.pregunta.texto} - {self.respuesta_elegida}'

class Story(models.Model):
    titulo = models.CharField(max_length=100)
    componentes = models.ManyToManyField(Componente)
    preguntas = models.ManyToManyField(Pregunta)

    def __str__(self):
        return self.titulo
