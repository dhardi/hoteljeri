from django.views import generic
from django.shortcuts import render
from .models import Post
from bookings.models import Review  # Importe o modelo Review do seu app bookings




def index(request):
    reviews = Review.objects.all()
    return render(request, 'rooms/index.html', {'reviews': reviews})


class PostList(generic.ListView):
    model = Post
    template_name = "rooms/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.all()  # Adicione todos os reviews ao contexto
        return context

def beaches(request):
    return render(request, 'rooms/beaches.html')