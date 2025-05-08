from django.db import models
from django.utils.text import slugify

class Imovel(models.Model):
    TIPO_CHOICES = [
        ('casa', 'Casa'),
        ('apartamento', 'Apartamento'),
        ('terreno', 'Terreno'),
        ('comercial', 'Comercial'),
        ('rural', 'Rural'),
    ]
    
    FINALIDADE_CHOICES = [
        ('venda', 'Venda'),
        ('aluguel', 'Aluguel'),
    ]

    titulo = models.CharField('Título', max_length=200)
    tipo = models.CharField('Tipo', max_length=20, choices=TIPO_CHOICES)
    finalidade = models.CharField('Finalidade', max_length=20, choices=FINALIDADE_CHOICES)
    endereco = models.CharField('Endereço', max_length=200)
    bairro = models.CharField('Bairro', max_length=100)
    cidade = models.CharField('Cidade', max_length=100)
    preco = models.DecimalField('Preço', max_digits=12, decimal_places=2)
    metragem = models.DecimalField('Metragem', max_digits=8, decimal_places=2)
    quartos = models.PositiveIntegerField('Quartos')
    banheiros = models.PositiveIntegerField('Banheiros')
    vagas = models.PositiveIntegerField('Vagas de Garagem')
    ano_fabricacao = models.PositiveIntegerField('Ano de Fabricação')
    descricao = models.TextField('Descrição')
    data_publicacao = models.DateTimeField('Data de Publicação', auto_now_add=True)
    destaque = models.BooleanField('Destaque', default=False)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name = 'Imóvel'
        verbose_name_plural = 'Imóveis'
        ordering = ['-data_publicacao']

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

class ImagemImovel(models.Model):
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE, related_name='imagens')
    imagem = models.ImageField('Imagem', upload_to='imoveis/%Y/%m/')
    ordem = models.PositiveIntegerField('Ordem', default=0)

    class Meta:
        verbose_name = 'Imagem'
        verbose_name_plural = 'Imagens'
        ordering = ['ordem']

    def __str__(self):
        return f'Imagem {self.ordem} do imóvel {self.imovel.titulo}'
