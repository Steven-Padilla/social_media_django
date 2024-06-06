from django.db import models
from django.contrib.auth.models import User


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='images/avatars')
    cover = models.ImageField(default='cover.jpg', upload_to='images/covers')
    is_public= models.BooleanField(default=True)
    name=models.CharField(max_length=30, blank=True)
    last_name=models.CharField(max_length=30, blank=True)
    age=models.SmallIntegerField(blank=True)

    def __str__(self):
        return self.user.username
    

class Post (models.Model):
    author=models.ForeignKey( Profile, on_delete=models.CASCADE)
    image= models.ImageField(default='post.jpg', upload_to='images/posts')
    description=models.TextField(max_length=300)

    def __str__(self) -> str:
        return self.description



