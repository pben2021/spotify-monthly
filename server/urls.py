"""server URL Configuration
"""
from django.contrib import admin
from django.urls import path
from core.views import front, year,january, february, march, april, may, june, july, august, september, october, november, december, noview

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", front, name="front"),
    path("year/", year, name="year"),
    path("january/", january, name="january"),
    path("february/", february, name="february"),
    path("march/", march, name="march"),
    path("april/", april, name="april"),
    path("may/", may, name="may"),
    path("june/", june, name="june"),
    path("july/", july, name="july"),
    path("august/", august, name="august"),
    path("september/", september, name="september"),
    path("october/", october, name="october"),
    path("november/", november, name="november"),
    path("december/", december, name="december"),
    path("month/<str:month>/", noview, name="noview"),
]
