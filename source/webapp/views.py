from django.shortcuts import render
from .models import Book


def main_page(request):
    if request.method == 'GET':
        titles = Book.objects.filter(status='active').order_by('-date_create')
        return render(request, 'index.html', {'titles': titles})
