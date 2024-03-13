from django.contrib import admin
from django.urls import path, include
import logging

from . import views

logger = logging.getLogger(__name__)


def trigger_error(request):
    try:
        division_by_zero = 1 / 0  # noqa: F841
    except Exception as e:  # noqa: F841
        logger.error('Triggered error for Sentry debugging', exc_info=True)


urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls', namespace='lettings')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),
]
