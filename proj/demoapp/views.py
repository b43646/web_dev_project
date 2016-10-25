from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from tasks import add
import models



# Create your views here.

@cache_page(60 * 1)
def index(request):
	test = models.test.objects.all().order_by('-id')
	if request.method == 'POST':
		print cache.get('mytext')
		sum=add.delay(int(request.POST['v1']),int(request.POST['v2']))
		#return render(request,'index.html',{'sum':test[0].sum})
		return HttpResponseRedirect('/index/')
		#HttpResponse('index.html',{'sum':sum})
	else:
		cache.set('mytext','Hello redis')
		return render(request,'index.html',{'sum':test[0].sum})
		#HttpResponse('index.html',{'sum':0})
		
