# other imports
import blog.views
from django.urls import path
from django.contrib import admin

urlpatterns = [
    # other patterns
    path("", blog.views.index),
    path('admin/', admin.site.urls),
        path("post/<slug>/", blog.views.post_detail, name="blog-post-detail")
]