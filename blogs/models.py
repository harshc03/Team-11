from django.db import models

# Create your models here.
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name

class Blogs(models.Model):
    blog_id = models.AutoField(primary_key=True)
    blog_title=models.CharField(max_length=255,null=True)
    blog_content = models.CharField(max_length=255)
    blog_image = models.ImageField(upload_to='blog_images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.blog_content

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.user_name
