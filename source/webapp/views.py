from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
from django.views import View


def main_page(request):
    if request.method == 'GET':
        records = Book.objects.filter(status='active').order_by('-date_create')
        return render(request, 'index.html', {'records': records})


def record_create(request):
    if request.method == "GET":
        return render(request, 'record_create.html', {'form': BookForm})
    elif request.method == 'POST':
        bound_from = BookForm(request.POST)
        if bound_from.is_valid():
            bound_from.save()
            return redirect('main_url')
        return render(request, 'record_create.html', context={'form': bound_from})


class RecordEdit(View):
    def get(self, request, pk):
        record = Book.objects.get(pk=pk)
        form = BookForm(instance=record)
        return render(request, 'record_edit.html', context={'form': form, 'pk1': record.pk})

    def post(self, request, pk):
        obj = Book.objects.get(pk=pk)
        bound_from = BookForm(request.POST, instance=obj)
        if bound_from.is_valid():
            bound_from.save()
            return redirect('main_url')
        return render(request, 'record_edit.html', context={'form': bound_from})
