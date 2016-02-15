from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from .models import Book
# Create your views here.

def index(request):
	book_list = Book.objects.all()
	context = {'book_list' : book_list}
	return render(request, 'polls/1.html', context)

def search(request):
	book_list = Book.objects.all()
	if request.POST['name']:
		book_list = book_list.filter(name=request.POST['name'])
	if request.POST['author']:
		book_list = book_list.filter(author=request.POST['author'])
	if request.POST['cls']:
		book_list = book_list.filter(cls=request.POST['cls'])
	context = {'book_list' : book_list}
	return render(request, 'polls/1.html', context)
