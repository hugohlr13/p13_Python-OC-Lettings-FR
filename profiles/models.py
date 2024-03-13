from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Model representing a user profile.

    This model extends the base Django User model to include additional information
    specific to the OC Lettings Site, such as the user's favorite city. The 'user'
    field is a one-to-one link to the Django standard User model, ensuring that
    each user can have only one profile and vice versa.
    """    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """         
        return self.user.username
