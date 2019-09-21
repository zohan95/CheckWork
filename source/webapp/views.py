from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm, RecordSearch
from django.views import View


def main_page(request):
    if request.method == 'GET':
        records = Book.objects.filter(status='active').order_by('-date_create')
        return render(request, 'index.html', {'records': records, 'form': RecordSearch})
    elif request.method == 'POST':
        bound_form = RecordSearch(request.POST)
        if bound_form.is_valid():
            search_query = bound_form.cleaned_data['search_field']
            records = Book.objects.filter(author__icontains=search_query).filter(status='active').order_by(
                '-date_create')
            return render(request, 'index.html', {'records': records, 'form': RecordSearch})
        return redirect('main_url')


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
        record = get_object_or_404(Book, pk=pk)
        form = BookForm(instance=record)
        return render(request, 'record_edit.html', context={'form': form, 'pk1': record.pk})

    def post(self, request, pk):
        obj = get_object_or_404(Book, pk=pk)
        bound_from = BookForm(request.POST, instance=obj)
        if bound_from.is_valid():
            bound_from.save()
            return redirect('main_url')
        return render(request, 'record_edit.html', context={'form': bound_from})


def record_delete(request, pk):
    record = get_object_or_404(Book, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', {'record': record})
    elif request.method == 'POST':
        record.delete()
        return redirect('main_url')
