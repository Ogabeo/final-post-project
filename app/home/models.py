from django.db import models
from app.accounts.models import User
from ckeditor.fields import RichTextField
from django.utils.text import slugify

# Create your models here.


class BaseModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    uploaded_at=models.DateTimeField( auto_now=True )
    is_active=models.BooleanField(default=True)

    class Meta:
        abstract=True

        
class Category(BaseModel):
    name = models.CharField(max_length=50)
    slug=models.SlugField(verbose_name="slug")
    avatar=models.ImageField(upload_to="category_images")


    def __str__(self):
        return self.name
    
class Tags(BaseModel):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class New(BaseModel):
    title=models.CharField(max_length=150)
    slug=models.SlugField(verbose_name="slug")
    image=models.ImageField(upload_to="news_images")
    author=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="author_name")
    category=models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name="category_name")
    tag=models.ManyToManyField(Tags, blank=True)
    views=models.IntegerField(default=0)
    body=RichTextField()

    def __str__(self):
        return f"{self.author}-{self.title}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        return super().save(*args, **kwargs)
class About(BaseModel):
    facebook=models.CharField(max_length=100)
    twitter=models.CharField(max_length=100)
    youtube=models.CharField(max_length=100)
    linkedin=models.CharField(max_length=100)
    location=models.CharField(max_length=450)
    instagram=models.CharField(max_length=100)
    browser=models.CharField(max_length=100)
    telegram=models.CharField(max_length=100)
    email=models.EmailField(null=True)
    phone=models.CharField(max_length=20, null=True, blank=True)



    def __str__(self):
        return "About"

class ContactUs(BaseModel):
    email=models.EmailField()
    first_name=models.CharField(max_length=25)
    phone_number=models.CharField(max_length=17)
    subject=models.CharField(max_length=50)
    message=models.TextField()

    def __str__(self):
        return self.name

class Comment(BaseModel):
    full_name=models.CharField(max_length=60)
    email=models.EmailField()
    comment=models.TextField()

    def __str__(self):
        return self.full_name




