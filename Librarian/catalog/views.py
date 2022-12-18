from django.shortcuts import render
from catalog.models import Book, Author, BookItem
from django.contrib.auth.decorators import login_required
import operator
from functools import reduce
from django.views.generic.list import ListView
from django.db.models import Q

@login_required

# Create your views here.
def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookItem.objects.all().count()
    # Available books (status = 'a')
    num_instances_available = BookItem.objects.filter(lang__exact='French').count()
    # The 'all()' is implied by default.
    num_authors = Author.objects.count()
    book_items = BookItem.objects.all(),
    context = {
    'num_books': num_books,
    'num_instances': num_instances,
    'num_instances_available': num_instances_available,
    'num_authors': num_authors,
    'book_items' : book_items,
    }
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def search(request, q):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookItem.objects.all().count()
    # Available books (status = 'a')
    num_instances_available = BookItem.objects.filter(lang__exact='French').count()
    # The 'all()' is implied by default.
    num_authors = Author.objects.count()
    book_items = BookItem.objects.all(),
    context = {
    'num_books': num_books,
    'num_instances': num_instances,
    'num_instances_available': num_instances_available,
    'num_authors': num_authors,
    'book_items' : book_items,
    }
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def home(request):
    return render(request, 'base.html')


class ArticleSearchListView(ListView):
    model = BookItem
    context_object_name = "article_lst"
    template_name = "catalog/index.html"
    paginate_by = 10

    def get_queryset(self):
        result = super(ArticleSearchListView, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(title__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(content__icontains=q) for q in query_list))
            )

        return result