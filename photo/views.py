from django.shortcuts import render,redirect
from django.http  import HttpResponse
import datetime as dt
from .models import Image,category,location,Photographer

# Create your views here.
global category,location
location = ['Nairobi','Nakuru','Mombasa','Kisumu']
category = ['Food','Clothing','Travel','Fashion']

def photo_of_today(request):
    date = dt.date.today()
    photo = Image.todays_photo()
    return render(request,'all-photos/today-photo.html',{'date': date, 'photo':photo,'category':category})

# View Function to present news from past days
def past_days_photos(request, past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(photo_of_today)

    photo = Image.days_photo(date)
    return render(request, 'all-photos/past-photo.html', {"date": date, 'photo':photo})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"images": searched_images, 'category':category})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message, 'category':category })

def category_results(request,category):
    searched_images=Image.filter_by_category(category)
    captions=f'{category}'

    return render (request,'all-photos/today_photo.html',{'photo':searched_images,'captions':captions, 'category' : category})

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-photos/image.html", {"image" :image})
