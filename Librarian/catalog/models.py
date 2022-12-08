from django.db import models

# Create your models here.
class Book(models.Model):

    #Variables
    LANGUAGE = [('EN', 'English'), ('FR', 'French'), ('DE', 'German'), ('ES', 'Spanish'), ('IT', 'Italian')]

    #Champs
    ISBN = models.CharField(max_length=25)
    name = models.CharField(max_length=50)
    subject = models.TextField()
    overview = models.TextField()
    publisher = models.CharField(max_length=50)
    publicationDate = models.DateField(auto_now_add=True)
    lang = models.CharField(max_length=50, choices=LANGUAGE)

    #Métadata (ordonnancement)
    class Meta:
        ordering = ['name']

    # Méthodes
    def __str__(self):
        """Représentation de MyModelName (Admin site etc.)."""
        return self.ISBN




