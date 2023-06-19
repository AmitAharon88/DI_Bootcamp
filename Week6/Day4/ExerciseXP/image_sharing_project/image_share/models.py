from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model) :
    image_file = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
    description = models.TextField()
    upload_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self) :
        return self.title

class Profile(models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    num_images = models.IntegerField(default=0)
    
    # def get_num_images(self):
    #     return self.profile.num_images.count()
    
    def __str__(self):
        return self.user.username
    
    # def __str__(self):
    #     return self.profile.num_images