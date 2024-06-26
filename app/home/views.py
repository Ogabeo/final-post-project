from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import New, Category, Comment, Tags, Users_email, ContactUs
from django.contrib import messages
from django.db.models import Q
# from itertools import chain

# Create your views here.

class Famous_News_List(View):
    def get(self, request):
        famous_newss=New.objects.all().order_by('-views')[:15]
        context={
            'famous_news':famous_newss
        }
        return render(request, 'famous_news.html', context)

# class New_User(View):
#     def get

class Category_News_List(View):
    def get(self, request, slug):
        ctg=Category.objects.get(slug = slug)
        news=New.objects.filter(category=ctg)
        context ={
            'ctg':ctg,
            'news':news,
        }

        return render(request, 'category_news.html', context )




class IndexView(View):

    def get(self, request):
        most_famous_new=New.objects.all().order_by('-views').first()
        most_famous_new_list=New.objects.all().order_by('-views')[:6]
        famous_new_for_recommend=New.objects.all().order_by('-views')[:3]
        sport_famous_news=New.objects.filter(category__name='Sports').order_by('-id')[:6]
        kundalik_hayot_famous_news=New.objects.filter(category__name='Kundalik Hayot').order_by('-id')[:6]
        IT_famous_news=New.objects.filter(category__name='IT ga oid').order_by('-id')[:6]
        Technology_famous_news=New.objects.filter(category__name='Technology').order_by('-id')[:6]
        Futbol_famous_news=New.objects.filter(category__name='Futbol yangiliklari').order_by('-id')[:6]
        two_kundalik_hayot_famous_news=New.objects.filter(category__name='Kundalik Hayot').order_by('?')[:2]
        context={
            
            'IT_famous_news':IT_famous_news,
            'famous_new_for_recommend':famous_new_for_recommend,
            'kundalik_hayot_famous_news':kundalik_hayot_famous_news,
            'Futbol_famous_news':Futbol_famous_news ,
            'sport_famous_news':sport_famous_news,
            'Technology_famous_news':Technology_famous_news,
            'most_famous_new_list':most_famous_new_list,
            'two_kundalik_hayot_famous_news':two_kundalik_hayot_famous_news,



            'most_famous_new':most_famous_new,
        }
        return render(request, 'index.html', context)


class ContactUs_view(View):
    def get(self, request):
        return render(request, 'contact.html')
    def post(self, request):
        data=request.POST
        contact=ContactUs()
        contact.name=data.get('name')
        contact.email=data.get('email')
        contact.phone=data.get('phone')
        contact.subject=data.get('subject')
        contact.message=data.get('message')
        contact.save()
        
        return render(request, 'index.html')

class Error404(View):
    def get(self, request):
        return render(request, '404.html')
class DetailPage(View):

    def get(self, request, slug):
        data=New.objects.get( slug = slug )
        data.views+=1
        data.save()
        context={
            'data':data,
            'tags': data.tag.all()
        }
        return render(request, 'detail-page.html', context)

# class CategoryNew(View):
    # def get(self, request):
    #     ctg=Category.objects.get(id=id)
    #     category_news=New.objects.filter(category=ctg)

class Commenttttt(View):
    def get(self, request):
        return render(request, 'detail-page.html')
    def post(self, request):
        data = request.POST
        comment=Comment()   
        comment.full_name=data.get('full_name')
        comment.email=data.get('email')
        comment.comment=data.get('comment')
        comment.save()
        messages.success(request, 'Your comment was sent...')

        return render(request, 'index.html')

class SearchView(View):
    def get(self, request):
        query=request.GET.get('query')
        if not query:
            news = New.objects.all()
        
        news = New.objects.all().filter( Q(title__icontains = query) | Q(body__icontains = query))
        # tag=get_object_or_404(Tags, name=query)
        # tag_news= tag.new_set.all()
        # result_list = list(chain(tag_news, news))
        context={
            "searchnews":news,
            # "searchnewsss":result_list
        }
        return render(request, 'search.html', context )
class famous_news(View):
    def get(self, request):
        all_famous_news=New.objects.all().order_by('-views')[:20]
        context={
            'all_famous_news':all_famous_news
        }
        return render(request, 'famous_news.html', context)

class User_email_view(View):
    
    def post(self, request):
        data = request.POST
        user=Users_email()   
        user.email=data.get('email')
        user.save()
        messages.success(request, 'Your email was sent...')
        return redirect('home:index')
