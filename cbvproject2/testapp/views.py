from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from testapp.models import Book
from django.urls import reverse_lazy

# Create your views here.
# def list_view(request):
#     books_list = Book.objects.all()
#     return render(request, 'testapp/books.html', {'books_list':books_list})

class BookListView(ListView):
    model = Book
    # default template file: book_list.html
    # default context object name: book_list
    template_name = 'testapp/books.html'
    context_object_name = 'books'

class BookListView2(ListView):
    model = Book
    # default template file: book_list.html
    # default context object name: book_list
    template_name = 'testapp/books2.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    # Default Template file is book_detail.html
    # Default context object is book or object


class BookCreateView(CreateView):
    model = Book
    fields = {'title', 'author', 'pages', 'price'}

class BookUpdateView(UpdateView):
    model = Book
    #fields = {'pages', 'price'}
    fields = '__all__'
    #The default template is book_form.html

class BookDeleteView(DeleteView):
    model = Book
    # After delete operation to to list page
    success_url = reverse_lazy('listbooks')
