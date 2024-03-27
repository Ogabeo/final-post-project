from django.shortcuts import render
from django.views import View
from .models import New, Category, Comment
from django.contrib import messages
# Create your views here.

class Famous_News_List(View):
    def get(self, request):
        famous_newss=New.objects.all().order_by('-views')[:15]
        context={
            'famous_news':famous_newss
        }
        return render(request, 'famous_news.html', context)



class Category_News_List(View):
    def get(self, request, id):
        ctg=Category.objects.get(pk=id)
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
        sport_famous_news=New.objects.filter(category__name='Sport').order_by('-id')[:6]
        kundalik_hayot_famous_news=New.objects.filter(category__name='Kundalik Hayot').order_by('-id')[:6]
        IT_famous_news=New.objects.filter(category__name='IT ga oid').order_by('-id')[:6]
        Technology_famous_news=New.objects.filter(category__name='Technology').order_by('-id')[:6]
        Futbol_famous_news=New.objects.filter(category__name='Futbol yangiliklari').order_by('-id')[:6]
        two_kundalik_hayot_famous_news=New.objects.filter(category__name='Kundalik Hayot').order_by('?')[:2]
        context={
            'most_famous_new_list':most_famous_new_list,
            'IT_famous_news':IT_famous_news,
            'kundalik_hayot_famous_news':kundalik_hayot_famous_news,
            'Futbol_famous_news':Futbol_famous_news ,
            'sport_famous_news':sport_famous_news,
            'Technology_famous_news':Technology_famous_news,
            'most_famous_new_list':most_famous_new_list,
            'two_kundalik_hayot_famous_news':two_kundalik_hayot_famous_news,



            'most_famous_new':most_famous_new,
        }
        return render(request, 'index.html', context)


class ContactUs(View):
    def get(self, request):
        return render(request, 'contact.html')
class Error404(View):
    def get(self, request):
        return render(request, '404.html')
class DetailPage(View):

    def get(self, request, id):
        data=New.objects.get(id=id)
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
