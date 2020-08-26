from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="ShopHome"),
    path("about/",views.about,name="About-us"),
    path("contact/",views.contact,name="Contact-Us"),
    path("tracker/",views.tracker,name="trackerStatus"),
    path("search/",views.search,name="search"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("checkout/",views.checkout,name="checkout")
]