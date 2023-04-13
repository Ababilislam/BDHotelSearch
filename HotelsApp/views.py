from django.shortcuts import render
from .models import Hotels
from django.http import JsonResponse
def home(request):
    return render(request, "HotelsApp/home.html")


def API_Hotels(request):
    hotels = Hotels.objects.all()
    price = request.GET.get('price')
    features =request.GET.get('features')
    # print(price)
    if price:
        hotels = hotels.filter(price__lte=price)

    if features:
        feature_list = features.split(',')
        fe = []
        for item in feature_list:
            try:
                fe.append(int(item))
            except Exception as e:
                print("your data is not correct!")
                print("wrong feature:",item)
        # print(fe)

        hotels = hotels.filter(features__in=fe).distinct()
    payload = []
    for hotel in hotels:
        result = {}
        result["hotel_name"] = hotel.hotel_name
        result["hotel_description"] = hotel.hotel_description
        result["hotel_image"] = hotel.hotel_image
        result["price"] = hotel.price
        # result["features"] = hotel.features
        payload.append(result)

    return JsonResponse(payload, safe=False)


