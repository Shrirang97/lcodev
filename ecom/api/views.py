from django.http import JsonResponse

# Create your views here.


def home(request):
    return JsonResponse({'Info': 'Django React Course', 'name': 'Shrirang'})
