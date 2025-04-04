# urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from analyzer.views import ResumeUploadView

urlpatterns = [
    # other URL patterns
    path('api/upload/', ResumeUploadView.as_view(), name='resume-upload'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
