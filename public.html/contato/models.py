from django.db import models

class MensagemContato(models.Model):
    nome = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail')
    telefone = models.CharField('Telefone', max_length=20)
    mensagem = models.TextField('Mensagem')
    data = models.DateTimeField('Data', auto_now_add=True)

    class Meta:
        verbose_name = 'Mensagem de Contato'
        verbose_name_plural = 'Mensagens de Contato'
        ordering = ['-data']

    def __str__(self):
        return f'Mensagem de {self.nome} em {self.data.strftime("%d/%m/%Y %H:%M")}'
