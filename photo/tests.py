from django.test import TestCase
from .models import Photographer,location,category,Image

# Create your tests here.
class PhotographerTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james= Photographer(first_name = 'pitz', last_name ='Peter', email ='pitz@moringaschool.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.pitz,Photographer))

        # Testing Save Method
    def test_save_method(self):
        self.james.save_photography()
        photography = Photographer.objects.all()
        self.assertTrue(len(photographers) > 0)

class ImageTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.james= Photographer(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        self.james.save_photography()

        # Creating a new tag and saving it
        self.new_category = category(name = 'testing')
        self.new_category.save()

        self.new_image= Image(image = ' ',image_name = 'Test Image',image_description = 'This is a random test Post',photography = self.james, image_category='',image_location='')
        self.new_image.save()

        self.new_image.category.add(self.new_category)

    def tearDown(self):
        Photographer.objects.all().delete()
        category.objects.all().delete()
        location.objects.all().delete()
        Image.objects.all().delete()
