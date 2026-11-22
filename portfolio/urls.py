"""
URL configuration for portfolio project.
"""

from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve


def serve_static(request, path, **kwargs):
    """Serve static files from STATIC_ROOT or fallback to core/static."""
    static_root = settings.STATIC_ROOT
    if (static_root / path).exists():
        return serve(request, path, document_root=static_root, **kwargs)
    core_static = settings.BASE_DIR / 'core' / 'static'
    if (core_static / path).exists():
        return serve(request, path, document_root=core_static, **kwargs)
    return serve(request, path, document_root=static_root, **kwargs)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    re_path(r'^static/(?P<path>.*)$', serve_static),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
