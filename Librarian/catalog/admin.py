from django.contrib import admin
from catalog.models import Book, BookItem, Account, Author, Patron 

# Register your models here.
admin.site.register(Book)
admin.site.register(BookItem)
admin.site.register(Account)
admin.site.register(Author)
admin.site.register(Patron)