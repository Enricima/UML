from django.db import models

# Create your models here.

class Author(models.Model):

    #Champs
    name = models.TextField(primary_key=True)
    biografy = models.TextField()
    birthDate = models.DateField()
    books = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)

    #Métadata (ordonnancement)
    class Meta:
        ordering = ['name']

    # Méthodes
    def __str__(self):
        return self.name

class FullName(models.Model):

    #Champs
    nom = models.CharField(max_length=25)
    prenom = models.CharField(max_length=25)

    #Métadata (ordonnancement)
    class Meta:
        ordering = ['nom']

    # Méthodes
    def __str__(self):
        return self.nom + " " + self.prenom

class Adresse(models.Model):

    #Champs
    numero = models.IntegerField()
    streetName = models.TextField()
    city = models.CharField(max_length=40)
    zipCode = models.IntegerField()

    #Métadata (ordonnancement)
    class Meta:
        ordering = ['city']

    # Méthodes
    def __str__(self):
        return self.numero + " " + self.streetName + " " + self.city + " " + self.zipCode 

class Book(models.Model):

    #Variables
    #LANGUAGE = [('EN', 'English'), ('FR', 'French'), ('DE', 'German'), ('ES', 'Spanish'), ('IT', 'Italian')]

    #Champs
    ISBN = models.CharField(max_length=25, primary_key=True)
    name = models.CharField(max_length=50)
    subject = models.TextField()
    overview = models.TextField()
    publisher = models.CharField(max_length=50)
    publicationDate = models.DateField(auto_now_add=True)
    #lang = models.CharField(max_length=50, choices=LANGUAGE)
    authors = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)

    #Métadata (ordonnancement)
    class Meta:
        ordering = ['name']

    # Méthodes
    def __str__(self):
        """Représentation de MyModelName (Admin site etc.)."""
        return self.ISBN

class BookItem(Book):

    #Variables
    FORMAT = [('PA', 'Paperback'), ('HA', 'Hardcover'), ('AB', 'Audiobook'), ('AC', 'Audio CD'), ('MP', 'MP3 CD'), ('PD', 'PDF')]
    LANGUAGE = [('EN', 'English'), ('FR', 'French'), ('DE', 'German'), ('ES', 'Spanish'), ('IT', 'Italian')]

    #Champs
    barcode = models.TextField()
    tag = models.TextField()
    title = models.CharField(max_length=50)
    isReferenceOnly = models.BooleanField(default=False)
    lang = models.CharField(choices=LANGUAGE, max_length=15)
    numberOfPages = models.IntegerField()
    format = models.TextField(choices=FORMAT)
    borrowed = models.DateField()
    loanPeriod = models.IntegerField()
    dueDate = models.DateField()
    isOverdue = models.BooleanField(default=False)

    #Métadata (ordonnancement)
    class Meta:
        ordering = ['ISBN']

    # Méthodes
    def __str__(self):
        return self.ISBN

class Catalog(models.Model):
    
    #Champs
    records = models.ForeignKey(BookItem, on_delete=models.SET_NULL, null=True)

    # Méthodes
    def __str__(self):
        return self.records

class Account(models.Model):
    #Variables
    ACCOUNTSTATE = [('AC', 'Active'), ('FR', 'Frozen'), ('CL', 'Closed')]

    #Champs
    number = models.IntegerField(primary_key=True)
    #history = ?
    opened = models.DateField(auto_now_add=True)
    state = models.TextField(choices=ACCOUNTSTATE)
    borrowed = models.ForeignKey(BookItem, on_delete=models.SET_NULL, null = True, related_name='%(class)s_requests_created')
    reserved = models.ForeignKey(BookItem, on_delete=models.SET_NULL, null=True)

    #Métadata (ordonnancement)
    class Meta:
        ordering = ['number']

    # Méthodes
    def __str__(self):
        return self.number

class Library(models.Model):

    #Champs
    name = models.TextField(max_length=50)
    address = models.OneToOneField(Adresse, on_delete=models.CASCADE)
    accounts = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    catalog = models.OneToOneField(Catalog, on_delete=models.CASCADE)

    #Métadata (ordonnancement)
    class Meta:
        ordering = ['name']

    # Méthodes
    def __str__(self):
        return self.name

class Patron(models.Model):

    #Champs
    name = models.OneToOneField(FullName, on_delete=models.CASCADE)
    address = models.OneToOneField(Adresse, on_delete=models.CASCADE)
    account = models.OneToOneField(Account, on_delete=models.SET_NULL, null=True)

    #Métadata (ordonnancement)
    class Meta:
        ordering = ['name']

    # Méthodes
    def __str__(self):
        return self.name

class Librarian(models.Model):

    #Champs
    name = models.OneToOneField(FullName, on_delete=models.CASCADE)
    address = models.OneToOneField(Adresse, on_delete=models.CASCADE)
    position = models.CharField(max_length=25)

    #Métadata (ordonnancement)
    class Meta:
        ordering = ['name']

    # Méthodes
    def __str__(self):
        return self.name




