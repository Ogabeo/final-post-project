from django.db import models
from django.contrib.auth.models import AbstractUser  
from django.core.validators import FileExtensionValidator 

# Create your models here.

class User(AbstractUser):
    phone=models.CharField(max_length=15)
    about_user=models.TextField()
    avatar=models.ImageField(upload_to="avatar_images", null=True, blank=True, 
                            validators=[FileExtensionValidator(allowed_extensions=('jpg', 'png', 'jpeg', 'heic'))] )
    @property
    def full_name(self):
        return f"{self.first_name}-{self.last_name}"
    def hashing_password(self):
        if not self.password.startswith("pbkdf2_sha256"):
            self.set_password(self.password)

    def save(self, *args, **kwargs):
        self.hashing_password()
        return super().save(*args, **kwargs) 
    
    

          
       