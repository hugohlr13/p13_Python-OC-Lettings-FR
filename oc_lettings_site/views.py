from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

# Global views for the OC Lettings Site application.


def index(request):
    """
    View for the index page of the OC Lettings Site.

    This view returns the main homepage rendered from the 'index.html' template.
    It doesn't pass any context to the template,
    as the homepage currently doesn't require any dynamic information.
    """
    logger.info('Rendering OC Lettings Site homepage')
    return render(request, 'index.html')
