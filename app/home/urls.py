from django.urls import path
from .views import IndexView, ContactUs, Error404, DetailPage, Famous_News_List, Category_News_List, Commenttttt

app_name='home'


urlpatterns=[
    path('', IndexView.as_view(), name='index'),
    path('famous_news/', Famous_News_List.as_view(), name='famous_newss'),
    path('contact/', ContactUs.as_view(), name='contact'),
    path('error/', Error404.as_view(), name='error'),
    path('detail/<int:id>/', DetailPage.as_view(), name='detail'),
    path('category/<int:id>/', Category_News_List.as_view(), name='category_news'),
    path('comment/', Commenttttt.as_view(), name="comment")
]