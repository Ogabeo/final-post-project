from .models import Category, Tags, About, New




def index_processor(request):
    category=Category.objects.all()
    tags=Tags.objects.all().order_by('?')[:8]
    about=About.objects.all().first()
    random_two_news=New.objects.order_by('?')[:2]
    random_one_new=New.objects.order_by("?")
    
    recent_news=New.objects.all().order_by('-id')[:5]
    random_news=New.objects.all().order_by('?')[:6]
    famous_news=New.objects.all().order_by( '-views')[:4]
    
    # num_views=New.objects.filter(created_at)


    context={
        'random_one_new':random_one_new,
        'random_two_news':random_two_news,
        'category':category,
        'tags':tags,
        'about':about,
        'recent_news':recent_news,
        'random_news':random_news,
        'famous_news':famous_news,
    }

    return context
