"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import RedirectView

# static and settigs, are necessary in order to serve images
from django.conf import settings
from django.conf.urls.static import static

# urlpatterns = patterns(
#     "",
#     (r"admin/", admin.site.urls),
#     # Redirect login to login/
#     # (r'^login$', RedirectView.as_view(url = '/login/')),
#     # Handle the page with the slash.
#     (r"^login/?$", include("challenges.urls")),
# )

handler404 = "challenges.views.custom_404"

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("blog/", include("blog.urls")),
        re_path(
            r"^challenges/$", RedirectView.as_view(url="/challenges")
        ),  # redir to rm /
        re_path(r"^challenges$", include("challenges.urls")),  # path without /
        re_path(r"^challenges/", include("challenges.urls")),  # path with /
        path("posts/", include("posts.urls")),
        path("book-outlet/", include("book_outlet.urls")),
        path("feedback/", include(arg="reviews.urls")),
        path("profiles/", include(arg="profiles.urls")),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
