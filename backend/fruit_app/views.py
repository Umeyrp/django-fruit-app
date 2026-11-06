from django.http import JsonResponse, HttpResponse


# Create your views here.
def send_fruits(request):
    fruits = [
        {"name": "zitrone", "gewicht": "25g", "farbe": "gelb"},
        {"name": "apfel", "gewicht": "20g", "farbe": "rot"},
        {"name": "mango", "gewicht": "50g", "farbe": "gelb"},
        {"name": "traube", "gewicht": "4g", "farbe": "grün"},
        {"name": "blaubeere", "gewicht": "2g", "farbe": "blau"},
    ]

    return JsonResponse(fruits, safe=False)
