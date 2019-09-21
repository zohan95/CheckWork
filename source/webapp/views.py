from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm


def main_page(request):
    if request.method == 'GET':
        records = Book.objects.filter(status='active').order_by('-date_create')
        return render(request, 'index.html', {'records': records})


def record_create(request):
    if request.method == "GET":
        return render(request, 'title_create.html', {'form': BookForm})
    elif request.method == 'POST':
        bound_from = BookForm(request.POST)
        if bound_from.is_valid():
            bound_from.save()
            return redirect('main_url')
        return render(request, 'title_create.html', context={'form': bound_from})
