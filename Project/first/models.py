from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150)
    bio = models.CharField(max_length=10000, blank=True, null=True)
    phone = models.IntegerField(null=True)
    image = models.ImageField(upload_to="images/avatars", default="images/avatars/avatar.png")

    def __str__(self):
        return self.user.username


class Image(models.Model):
    image = models.ImageField(upload_to="images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(default=timezone.now)
    place = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    # likes = models.IntegerField(default=0)


class Like(models.Model):
    """
    Создаем отдельную модель для лайка. Потом будем считать длину
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    @staticmethod
    def get_all_likes_of_photo(image_id):
        return len(Image.objects.all().filter(id=image_id))


@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    date = models.DateTimeField(default=timezone.now)
    text = models.CharField(max_length=512)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')


class Order(models.Model):
    address = models.CharField(max_length=512)
    date = models.CharField(max_length=50)
    info = models.CharField(max_length=512)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
