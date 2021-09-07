from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import Http404 
# from django.core.paginator import Paginator, EmptyPage
from django.views.generic import ListView, DetailView
# from django.utils import timezone
from django_countries import countries
from . import models


class HomeView(ListView):

    """Home view Definition"""

    model = models.Room
    paginate_by = 10
    ordering = 'created'
    paginate_orphans = '5'
    context_object_name = 'rooms'

    # def get_context_data(self, **kwargs):
    #     context = super(HomeView, self).get_context_data(**kwargs)
    #     now = timezone.now()
    #     context['now'] = now
    #     return

# FBV
# def home(request):
#     page = request.GET.get('page', 1)
#     room_list = models.Room.objects.all()
#     paginator = Paginator(room_list, 10, orphans=5)
#     try:
#         rooms = paginator.page(int(page))
#         return render(request, "rooms/home.html", context={"page": rooms})
#     except EmptyPage:
#         return redirect('/')


# FBV
# def home(request):
#     page = (request.GET.get('page', 1))
#     page = int(page or 1)
#     page_size = 10
#     limit = page_size * page
#     offset = limit - page_size
#     page_count = ceil(models.Room.objects.count() / page_size)
#     all_rooms = models.Room.objects.all()[offset:limit]
#     return render(request, "rooms/home.html", context={
#         "rooms": all_rooms,
#         "page": page,
#         "page_count": page_count,
#         "page_range": range(1, page_count + 1),
#     })


class RoomDetail(DetailView):
    model = models.Room

# FBV
# def room_detail(request, pk):
#     try:
#         room = models.Room.objects.get(pk=pk)
#         return render(request, "rooms/room_detail.html", {"room": room})
#     except models.Room.DoesNotExist:
#         raise Http404()
#         # return redirect(reverse("core:home"))


def search(request):
    city = request.GET.get('city', 'Anywhere')
    city = str.capitalize(city)
    country = request.GET.get('country', 'NG')
    room_type = int(request.GET.get('room_type', 0))
    price = int(request.GET.get('price', 0))
    guests = int(request.GET.get('guests', 0))
    bedrooms = int(request.GET.get('bedrooms', 0))
    beds = int(request.GET.get('beds', 0))
    baths = int(request.GET.get('baths', 0))
    instant = request.GET.get('instant', False)
    super_host = request.GET.get('super_host', False)
    s_amenities = request.GET.getlist('amenities')
    s_facilities = request.GET.getlist('facilities')
    print()

    form = {
        "city": city,
        "s_room_type": room_type,
        "s_country": country,
        "price": price,
        "guests": guests,
        "bedrooms": bedrooms,
        "beds": beds,
        "baths": baths,
        "s_facilities": s_facilities,
        "s_amenities": s_amenities,
        "instant": instant,
        "super_host": super_host,
    }

    room_types = models.RoomType.objects.all()
    amenities = models.Amenity.objects.all()
    facilities = models.Facility.objects.all()
    # house_rules = models.HouseRule.objects.all()
    choices = {
        "countries": countries,
        "room_types": room_types,
        "amenities": amenities,
        "facilities": facilities,
        # "house_rules": house_rules,
    }
    return render(request, "rooms/search.html", {**form, **choices})


# {**form, **choices} This is known as unpacking
