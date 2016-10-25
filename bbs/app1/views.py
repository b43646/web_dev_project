from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.core.mail import send_mail
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

import models
from .form import NameForm,UserForm
# Create your views here.

def index(request):
    article_list = models.Article.objects.all().order_by('-publish_date')
    paginator = Paginator(article_list,5)
    page = request.GET.get('page')
    try:
        myarticles = paginator.page(page)
    except PageNotAnInteger:
        myarticles = paginator.page(1)
    except EmptyPage:
        myarticles = paginator(paginator.num_pages)

    return render(request,'index.html',{
        'articles':myarticles
    })


def article(request,id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login2/')
    item = models.Article.objects.get(id=id)

    return render(request,'article.html',{
        'article': item
    })


def login(request):
    if request.method == 'POST':
        form = NameForm(request.POST,request.FILES)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
            recipients = ['408514942@qq.com']
            #send_mail(subject,message,sender,recipients,fail_silently=False)
            filename = 'static/imags/upload/'+request.FILES['myfile'].name
            with open(filename,'w') as fd:
                for chunk in request.FILES['myfile'].chunks():
                    fd.writelines(chunk)
            return HttpResponseRedirect('/article/1/')
    else:
        form = NameForm()
    return render(request,'form.html',{'form':form.as_ul()})


def new(request):
    if request.method == 'POST':

        data = {
            'title':request.POST.get('title'),
            'content':request.POST.get('content'),
            'category_id':1,
            'summary':request.POST.get('summary'),
            'author_id':1,
            'head_img':'',
        }
        bbs_obj = models.Article(**data)
        bbs_obj.save()

        filename = 'static/imags/upload/' + request.FILES['head_img'].name
        with open(filename, 'w') as fd:
            for chunk in request.FILES['head_img'].chunks():
                fd.writelines(chunk)
        bbs_obj.head_img = filename
        bbs_obj.save()

        text = '''<a href="/article/%s/">%s</a> '''%(str(bbs_obj.id),bbs_obj.title)
        return HttpResponse(text)

    else:
        return render(request,'new_article.html')


def login2(request):
    if request.method == 'POST':
        print request.POST
        user = UserForm(request.POST)
        if user.is_valid():
            user2 = authenticate(username=user.cleaned_data['name'],password=user.cleaned_data['password'])
            if user2 is not None:
                if user2.is_active:
                    print 'User is valid'
                else:
                    print 'password is ok, but the account is disabled!'
            else:
                    print 'user name or password is not correct'
        return HttpResponseRedirect('/article/1/')
    else:
        user = UserForm()
        print  'Get'
        return render(request,'login2.html',{'form':user})
