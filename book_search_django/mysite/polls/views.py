from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from .models import Book
# Create your views here.

book_list = []
name_list = []
author_list = []
cls_list = []

def get_name_list():
	book_list = Book.objects.all()
	for i in book_list:
		if i.name not in name_list:
			name_list.append(i.name)


def get_author_list():
	book_list = Book.objects.all()
	for i in book_list:
		if i.author not in author_list:
			author_list.append(i.author)


def get_cls_list():
	book_list = Book.objects.all()
	for i in book_list:
		if i.cls not in cls_list:
			cls_list.append(i.cls)


def index(request):
	get_name_list()
	get_author_list()
	get_cls_list()
	print name_list, author_list,cls_list
	context = {'name_list' : name_list, 'author_list':author_list,'cls_list':cls_list}
	return render(request, 'polls/1.html', context)

def search(request):
	book_list_search = Book.objects.all()
	if request.POST['name']:
		book_list_search = book_list_search.filter(name=request.POST['name'])
	if request.POST['author']:
		book_list_search = book_list_search.filter(author=request.POST['author'])
	if request.POST['cls']:
		book_list_search = book_list_search.filter(cls=request.POST['cls'])
	context = {'name_list' : name_list, 'author_list':author_list,'cls_list':cls_list, 'book_list_search':book_list_search}
	return render(request, 'polls/1.html', context)
