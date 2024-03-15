from django.shortcuts import render
from .models import Letting
import logging

logger = logging.getLogger(__name__)


def index(request):
    """
    View function for the index page of lettings.

    This view returns a list of all lettings to be displayed on the index page.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    logger.info('Rendering OC Lettings Lettings')
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    View function for displaying a specific letting.

    Retrieves a letting by its ID and displays its details. If the letting is not found,
    the request will result in a 404 error.

    Args:
        request: HttpRequest object.
        letting_id (int): The ID of the letting to retrieve.

    Returns:
        HttpResponse object with the letting details.
    """
    try:
        letting = Letting.objects.get(id=letting_id)
        context = {
            'title': letting.title,
            'address': letting.address,
        }
        return render(request, 'lettings/letting.html', context)
    except Letting.DoesNotExist:  # pragma: no cover
        logger.warning(f'Letting with id {letting_id} not found')
    except Exception as e:  # noqa: F841 pragma: no cover
        logger.error(f'Error loading letting with id {letting_id}', exc_info=True)
