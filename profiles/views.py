from django.shortcuts import render
from .models import Profile
import logging

logger = logging.getLogger(__name__)


def index(request):
    """
    View for the index page of the Profiles application.

    This view lists all profiles in the database. Each profile is associated with a user.
    The profiles are passed to the 'profiles/index.html' template as part of the context.

    :param request: HttpRequest object
    :return: HttpResponse object with rendered index page
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    logger.info('Rendering OC Lettings Profiles')
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Detail view for a specific profile in the Profiles application.

    This view retrieves a Profile based on the provided username. It then passes this
    profile to the 'profiles/profile.html' template as part of the context.

    :param request: HttpRequest object
    :param username: Username associated with the Profile to be retrieved
    :return: HttpResponse object with rendered profile page
    """
    try:
        profile = Profile.objects.get(user__username=username)
        context = {'profile': profile}
        return render(request, 'profiles/profile.html', context)
    except Profile.DoesNotExist:
        logger.warning(f'Profile for user {username} not found')
    except Exception as e:  # noqa: F841
        logger.error(f'Error loading profile for user {username}', exc_info=True)
    context = {'profile': profile}
