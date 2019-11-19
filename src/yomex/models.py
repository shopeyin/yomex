import sys
from django.db import models
from django.db.models import Q
from django.utils.text import slugify
from .utils import unique_slug_generator
from django.urls import reverse
from django.conf import settings
from io import BytesIO
from django.db.models.signals import post_delete,pre_save
from django.dispatch import receiver
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image




def upload_location(instance, filename):
	file_path = 'yomex/{name}-{filename}'.format(
				name=str(instance.name), filename=filename)
	return file_path




class YomexStore(models.Model):
    name                = models.CharField(max_length=100)
    description         = models.CharField(max_length=100)
    image		 		= models.ImageField(upload_to=upload_location, null=False, blank=False)
    discount            = models.PositiveSmallIntegerField()
    price               = models.DecimalField(max_digits=100,decimal_places=2)
    date_uploaded 		= models.DateTimeField(auto_now_add=True, verbose_name="date uploaded")
    date_updated 		= models.DateTimeField(auto_now=True, verbose_name="date updated")
    
   
    class Meta:
        abstract = True


    def __str__(self):
        return self.name


class Perfume(YomexStore):
    slug 				= models.SlugField(blank=True, unique=True)

    class Meta:
        verbose_name_plural ='perfume'


def pre_save_perfume_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, instance.name,instance.slug)
pre_save.connect(pre_save_perfume_receiver, sender=Perfume)





class Shoes(YomexStore):
    size            = models.IntegerField()
    slug 			= models.SlugField(blank=True, unique=True)


    

    class Meta:
        verbose_name_plural ='shoes'

    def get_absolute_url(self):
       return reverse('yomex:detail_shoe', args=[str(self.slug)])

    
def pre_save_shoe_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, instance.name,instance.slug)
pre_save.connect(pre_save_shoe_receiver, sender=Shoes)





   

class WristWatch(YomexStore):
    slug 				= models.SlugField(blank=True, unique=True)

    class Meta:
        verbose_name_plural ='wristwatches'



    def get_absolute_url(self):
       return reverse('yomex:detail_watch', args=[str(self.slug)])


def pre_save_watch_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, instance.name,instance.slug)
pre_save.connect(pre_save_watch_receiver, sender=WristWatch)





class Glass(YomexStore):
    slug 				= models.SlugField(blank=True, unique=True)

    class Meta:
        verbose_name_plural ='glasses'

def pre_save_glass_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, instance.name,instance.slug)
pre_save.connect(pre_save_glass_receiver, sender=Glass)


    
@receiver(post_delete,sender=YomexStore)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)

