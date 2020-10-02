from django.db import models

class Unit(models.Model):
    """A Unit the user is entering in the DB"""

    STATUS_CHOICES = {
        ('MISSING', 'Missing'),
        ('FAILED', 'Failed'),
        ('STICK', 'Stick'),
    }

    TYPES = {
        ('W', 'Winx'),
        ('E', 'Enable'),
        ('A', 'Arkle'),
        ('D', 'Denman'),
        ('K', 'Kauto'),
        ('F', 'Frankel'),
    }

    number = models.PositiveSmallIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=10, choices=TYPES, default='W')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='STICK')

    def __str__(self):
        """Returning a sring representation of the model"""
        name = f"{self.type}{self.number}"
        return name
