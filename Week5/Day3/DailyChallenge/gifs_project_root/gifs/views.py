from django.shortcuts import render
from .models import Gif, Category
from .forms import GifForm, CategoryForm

# Create your views here.
def homepage(request) :
    gifs = Gif.objects.all()
    return render(request, 'homepage.html', {'gifs': gifs})
  
def new_gif(request) :
    if request.method == 'POST':
        form = request.POST
        filled_form = GifForm(form)
        filled_form.save()

    gif_form = GifForm()
    context = {'form': gif_form}
    return render(request, 'new_gif.html', context)

def new_category(request) :
    if request.method == 'POST':
        form = request.POST
        filled_form = CategoryForm(form)
        filled_form.save()

    category_form = CategoryForm()
    context = {'form': category_form}
    return render(request, 'new_category.html', context)

def category(request, category_id) :
    category = Category.objects.get(id=category_id)
    return render(request, 'category.html', {'category': category})

def categories(request) :
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})

def gif(request,gif_id) :
    gif = Gif.objects.get(id=gif_id)
    return render(request, 'gif.html', {'gif': gif})

def popular_gifs(request):
    gifs = Gif.objects.filter(likes__gt=0).order_by('-likes')
    return render(request, 'popular_gifs.html', {'gifs': gifs})