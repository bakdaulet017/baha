from django.http import JsonResponse
from .models import Book

def book_list(request):
    books = list(Book.objects.values())
    return JsonResponse(books, safe=False)

def book_detail(request, id):
    try:
        book = Book.objects.values().get(id=id)
        return JsonResponse(book)
    except Book.DoesNotExist:
        return JsonResponse({'error': 'Книга не найдена'}, status=404)
