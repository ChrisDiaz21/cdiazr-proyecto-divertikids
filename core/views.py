from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from .models import Review

def home(request):
    return render(request, "core/index.html")

@login_required
def carrito(request):
    # Lógica para el carrito
    return render(request, 'core/carrito.html')  # Asegúrate de que la ruta sea correcta





@login_required
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('add_review')  # Redirige a la misma página después de guardar
    else:
        form = ReviewForm()
    
    reviews = Review.objects.all().order_by('-created_at')  # Obtiene todas las reseñas ordenadas por fecha de creación
    return render(request, 'core/add_review.html', {'form': form, 'reviews': reviews})

def reviews(request):
    reviews = Review.objects.all()
    return render(request, 'reviews.html', {'reviews': reviews})

def review_list(request):
    reviews = Review.objects.all().order_by('-created_at')
    return render(request, 'core/review_list.html', {'reviews': reviews})


def public_reviews(request):
    reviews = Review.objects.all().order_by('-created_at')
    return render(request, 'core/public_reviews.html', {'reviews': reviews})
