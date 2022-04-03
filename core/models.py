from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=150)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do evento') #customiza no admin 'data evento' por 'data do evento'
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) #se o usuário for excluido da aplicação serão excluidos também todos os eventos dele!

    class Meta:
        db_table = 'evento' #a tabela que irá ser criada será obrigada a se chamar evento, sem isto iria se chamar core_evento 

    def __str__(self):
        return self.titulo #irá retornar o título que for escrito dentro do django admin!
    
    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H %M Hrs') #formatando a data e a hora