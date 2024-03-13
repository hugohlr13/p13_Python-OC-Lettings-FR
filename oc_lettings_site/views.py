from django.shortcuts import render

# Global views for the OC Lettings Site application.


def index(request):
    """
    View for the index page of the OC Lettings Site.

    This view returns the main homepage rendered from the 'index.html' template.
    It doesn't pass any context to the template,
    as the homepage currently doesn't require any dynamic information.
    """
    return render(request, 'index.html')
