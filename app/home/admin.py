from django.contrib import admin
from .models import Category, ContactUs, About, New, Tags, Comment, Users_email

# Register your models here.

class NewAdmin(admin.ModelAdmin):
    list_display=('id','title', 'author', 'category', 'views', 'created_at', 'is_active',)
    list_display_links=('id', 'title')
    readonly_fields=('views',)
    list_editable=('author', 'category',)
    filter_horizontal=('tag',)
    prepopulated_fields={'slug':['title']}  

class CategoryAdmin(admin.ModelAdmin):
    list_display=('id', 'name')
    list_display_links=('id', 'name')
    prepopulated_fields={'slug':['name']}

class CommentAdmin(admin.ModelAdmin):
    list_display=('id', 'full_name', 'email')
    list_display_links=('id', 'full_name', 'email')

class User_email_admin(admin.ModelAdmin):
    list_display=('id', 'email')


admin.site.register(New, NewAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ContactUs)
admin.site.register(About)
admin.site.register(Tags)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Users_email, User_email_admin)




