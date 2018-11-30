from django.db import models

class Perro( models.Model ):

    ESTADO = (
        ('Disponible', 'Disponible'),
        ('Rescatado', 'Rescatado'),
        ('Adoptado','Adoptado'),
    )   


    id = models.AutoField( primary_key = True )
    nombre = models.CharField( max_length = 255 )
    raza = models.TextField( default= '' )
    caracteristica = models.TextField( default= '' )
    estado = models.CharField( max_length = 255, default = 'disponible',choices= ESTADO )
    imageUrl = models.CharField( max_length = 255, default = '' )

    def __str__( self ):
        return self.nombre


class User(models.Model):

    YES = '1'
    NO = '0'

    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    admin = models.CharField(max_length=10, default=NO)
