from django.db import models
# from django.contrib.auth.models import User
from app_auth.models import User


# Create your models here.

class Expertise(models.Model):
    """
    Description:
    Model for expertise by User

    """
    BEGINNER = 'Beginner'
    INTERMEDIATE = 'Intermediate'
    ADVANCE = 'Advance'
    EXPERT = 'Expert'
    LEGEND = 'Legend'

    LEVEL_CHOICE = (
        (BEGINNER, BEGINNER),
        (INTERMEDIATE, INTERMEDIATE),
        (ADVANCE, ADVANCE),
        (EXPERT, EXPERT),
        (LEGEND, LEGEND),
    )

    user = models.ForeignKey(to=User)

    expertise = models.CharField('Expertise', max_length=45)
    level = models.CharField('Level', choices=LEVEL_CHOICE, max_length=15)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.expertise

    class Meta:
        ordering = ('expertise', 'created_at')
