from django.shortcuts import render
from django.views import generic
from .models import Book, BookInstance, Author, Genre

def index(request):
    num_books = Book.objects.all().count()
    num_authors = Author.objects.all().count()
    num_book_inctances = BookInstance.objects.all().count()
    num_book_inctances_available = BookInstance.objects.filter(status__exact='a').count()
    num_with_a = Book.objects.filter(title__contains='и' ).count()
    return render(request, 'index.html', context={
        'num_books':num_books, 
        'num_authors': num_authors,
        'num_book_inctances':num_book_inctances,
        'num_book_inctances_available': num_book_inctances_available,
        'num_with_a':num_with_a
    })

class BookListView(generic.ListView):
    model = Book
    # paginate_by = 3

'''def book_detail_view(request,pk):
    try:
        book_id=Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")

    #book_id=get_object_or_404(Book, pk=pk)

    return render(
        request,
        'catalog/book_detail.html',
        context={'book':book_id,}
    )'''

class BookDetailView(generic.DetailView):
    model = Book