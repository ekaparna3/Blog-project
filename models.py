from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Userprofile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='profilepic')
    dob=models.DateField()  
    bio=models.CharField(max_length=100)
    followers=models.ManyToManyField(User,related_name='followers')
    
class CreatePost(models.Model):
    image=models.ImageField(upload_to='post_image')
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    likes=models.ManyToManyField(User,related_name='likes')

    def likes_count(self):
        return self.likes.all().count()
    
    def comment(self):
        return self.comments_set.all()
    
    def comment_count(self):
        return self.comment.all().count()


class Comments(models.Model):
    comment=models.CharField(max_length=100)
    post=models.ForeignKey(CreatePost,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)