from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# needed to check if we are in development mode
import environ
env = environ.Env()
environ.Env.read_env()

urlpatterns = [
    path('api/lctecadmin-6A6573757363687269737469736B696E67/', admin.site.urls),
    # djoser library is a REST implementation of Django authentication system
    path('api/lctec/v1/', include('djoser.urls')),
    path('api/lctec/v1/', include('djoser.urls.authtoken')),
    # path('api/lctec/v1/', include ('lctec_user.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# yellow header title and login title
admin.site.site_header = 'LC Technologies'
# white header under and left side browser tab title
admin.site.index_title = ' '
# right side browser tab title
admin.site.site_title = 'Admin'