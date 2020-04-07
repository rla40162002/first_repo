from django.utils import timezone
from django.views.generic import ListView, DetailView, View
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models, forms


class HomeView(ListView):
    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["now"] = now
        return context


class RoomDetail(DetailView):
    """ RoomDetail Definition """

    model = models.Room
    pk_url_kwarg = "pk"  # pk 대신 다른 거로 대체 가능


class SearchView(View):
    """ SearchView Definition """

    def get(self, request):
        country = request.GET.get("country")

        if country:
            form = forms.SearchForm(request.GET)
            # 먼저 미확인된 정보 주고
            if form.is_valid():  # 그게 이상이 없는지 확인
                city = form.cleaned_data.get("city")
                country = form.cleaned_data.get("country")
                room_type = form.cleaned_data.get("room_type")
                price = form.cleaned_data.get("price")
                guests = form.cleaned_data.get("guests")
                bedrooms = form.cleaned_data.get("bedrooms")
                beds = form.cleaned_data.get("beds")
                baths = form.cleaned_data.get("baths")
                instant_book = form.cleaned_data.get("instant_book")
                superhost = form.cleaned_data.get("superhost")
                amenities = form.cleaned_data.get("amenities")
                facilities = form.cleaned_data.get("facilities")

                filter_args = {}

                if city != "Anywhere":
                    filter_args["city__startswith"] = city

                filter_args["country"] = country

                if room_type is not None:
                    filter_args["room_type"] = room_type

                if price is not None:
                    filter_args["price__lte"] = price

                if guests is not None:
                    filter_args["guests__gte"] = guests

                if bedrooms is not None:
                    filter_args["bedrooms__gte"] = bedrooms

                if beds is not None:
                    filter_args["beds__gte"] = beds

                if baths is not None:
                    filter_args["baths__gte"] = baths

                if instant_book is True:
                    filter_args["instant_book"] = True

                if superhost is True:
                    filter_args["host__superhost"] = True

                qs = models.Room.objects.filter(**filter_args).order_by("-created")
                for amenity in amenities:
                    qs = qs.filter(amenities=amenity)

                for facility in facilities:
                    qs = qs.filter(facilities=facility)

                paginator = Paginator(qs, 3)

                page = request.GET.get("page", 1)

                rooms = paginator.get_page(page)
                room_info = request.GET.copy()
                room_info = room_info.pop("page", True) and room_info.urlencode()
                return render(
                    request,
                    "rooms/search.html",
                    {"form": form, "rooms": rooms, "room_info": room_info},
                )

        else:
            form = forms.SearchForm()

        return render(request, "rooms/search.html", {"form": form},)
