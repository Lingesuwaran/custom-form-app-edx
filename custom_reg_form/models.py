from django.conf import settings
from django.db import models

# Backwards compatible settings.AUTH_USER_MODEL
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

Institution_choices = (
    ('IIT','Indian Institute of Technology'),
    ('JNU', 'Jawaharlal Nehru University'),
    ('BHU','Banaras Hindu University'),
    ('AVV','Amrita Vishwa Vidyapeetham'),
    ('JMI','Jamia Millia Islamia'),
    )

Class_choices = (
    ('CSE','Computer Science'),
    ('MECH','Mechanical'),
)

class ExtraInfo(models.Model):
    """
    This model contains two extra fields that will be saved when a user registers.
    The form that wraps this model is in the forms.py file.
    """
    user = models.OneToOneField(USER_MODEL, null=True,  related_name='user+', on_delete=models.CASCADE)
    
    nationality = models.CharField(
        verbose_name="Nationality",
        max_length=100,
    )
    
    age = models.CharField(
        verbose_name="Age",
        max_length=20,
    )

    phone_number = models.CharField(
        verbose_name="Phone Number",
        max_length=100,
    )    

    institution_name = models.CharField(max_length=100, choices=Institution_choices, default='IIT')

    class_name = models.CharField(max_length=100, choices=Class_choices, default='CSE')
  
    
    def __str__(self):
        result = '{0.user} {0.nationality} {0.age} {0.phone_number}'
        return result.format(self)
