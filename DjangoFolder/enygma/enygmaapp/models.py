from django.db import models
from django.contrib.auth import get_user_model
#
# UserModel = get_user_model()
# user = UserModel.objects.create(username="guestuser100", password="123")
# user.save()
# # Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50)
    emailaddress = models.CharField(max_length=100)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)

class Mystery(models.Model):
    mystery_title = models.CharField(max_length=250)
    mysteryid = models.CharField(max_length=3)
    genre = models.CharField(max_length=15)
    difficulty = models.CharField(max_length=10)
    percentage_solved = models.IntegerField(default=0)
    storyparagraphs = models.CharField(max_length=25500)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

user = models.OneToOneField(User, on_delete=models.CASCADE)
def __str__(self):
    return " ID: "+str(self.id)+" -- "+self.user.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(default="default.jpg", upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username
