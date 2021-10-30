from django.db import models


class Guest(models.Model):
    CEDULA='CC'
    TARJETA_IDENTIDAD='TI'
    CEDULA_EXTRANJERIA='CE'
    PASAPORTE='PA'
    TYPE_DOC_CHOICES = [
        (CEDULA, 'Cedula'),
        (TARJETA_IDENTIDAD, 'Tarjeta de identidad'),
        (CEDULA_EXTRANJERIA, 'Cedula de extranjeria'),
        (PASAPORTE, 'Pasaporte'),       
    ]
    doc_id=models.CharField(primary_key=True,max_length=12)
    #Model.get_FOO_display() -> foo=campo/type_doc, muestra el human-readable del choice
    type_doc = models.CharField(null=False,max_length=4,choices=TYPE_DOC_CHOICES)
    first_name = models.CharField(null=False,max_length=100)
    last_name = models.CharField(null=False,max_length=100)
    birthdate = models.DateField(null=False)
    phone = models.IntegerField(null=False)
    email = models.EmailField(null=True)