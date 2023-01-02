from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    
    path("",views.index,name="ShopHome"),
    path("about/",views.about,name="AboutUs"),
    path("contact/",views.contact,name="contactus"),
    path("tracker/",views.tracker,name="trackeus"),
    path("search/",views.search,name="search"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("checkout/",views.checkout,name="checkout")
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)