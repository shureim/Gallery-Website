from django.db import models
import datetime as dt

# Create your models here.



class Photographer(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['first_name']

    def save_photography(self):
        self.save()

class location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    def save_location(self):
        save.self()

    def delete_location(self):
        self.delete()

    @classmethod
    def update_location(cls,location,update):
         updated = cls.objects.filter(image_name=location).update(name=update)
         return updated

# class category(models.Model):
#     category = models.CharField(max_length = 30)
#     def save_category(self):
#         save.self()
#
#
#
#     def delete_location(self):
#         self.delete()
#
#     @classmethod
#     def update_location(cls,location,update):
#          updated = cls.objects.filter(image_name=location).update(name=update)
#          return updated
#
#     verbose_name_plural = "Categories"
#
# class Image(models.Model):
#     image = models.ImageField(upload_to = 'images/',blank = True)
#     image_name = models.CharField(max_length = 30)
#     image_description = models.TextField(max_length = 200)
#     photography = models.ForeignKey(Photographer)
#     image_category = models.ManyToManyField(category)
#     image_location = models.ForeignKey(location)
#     photo_date = models.DateTimeField(auto_now_add=True)
#
#     @classmethod
#     def todays_photo(cls):
#         today = dt.date.today()
#         photo = cls.objects.filter(photo_date__date = today)
#         return photo
#
#     @classmethod
#     def days_photo(cls,date):
#         photo = cls.objects.filter(photo_date = date)
#         return photo
#
#
#     @classmethod
#     def get_all(cls):
#         images = cls.objects.order_by('-post_date')
#         return images
#
#     @classmethod
#     def get_image(cls, id):
#         image = cls.objects.get(id=id)
#         return image
#
#     @classmethod
#     def searched(cls, query):
#         result = cls.objects.filter(image_description =query).order_by('-post_date')
#         return result
#
#
#
#     # @classmethod
#     # def today_pics(cls):
#     #     today = dt.date.today()
#     #     images = cls.objects.filter(post_date__date=today)
#     #     return images
#
#
#     @classmethod
#     def filter_by_Location(cls, loc):
#         loc = cls.objects.filter(location=loc)
#         return cls.objects.filter(location=loc)
#
#     @classmethod
#     def search_by_category(cls,search_term):
#         photo = cls.objects.filter(image_category = search_term)
#         return photo
