from django.db import models

# Statut pour le petit déjeuner et la disponibilité
STATUS = (
    (0, "Non"),
    (1, "Oui")
)
TYPE_CHOICES = {
    0: "Simple",
    1: "Double",
    2: "Suite"
}

# Create your models here.
class ChambreHotel(models.Model):
    numeroChambre = models.IntegerField(unique=True)
    type = models.CharField(choices=TYPE_CHOICES, default=0)
    etage = models.IntegerField()
    prix = models.PositiveIntegerField()
    petit_dejeuner = models.BooleanField(choices=STATUS, default=0)
    disponibilite = models.BooleanField(choices=STATUS, default=0)
    description = models.TextField()
