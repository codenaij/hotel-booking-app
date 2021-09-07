from django.db import models


class TimeStampedModel(models.Model):
    """TimeStamped Model"""

    """This model would have the created and updated at fields, which will be inherited by other apps so as not to repeat created and updated at. 
    It will not be migrated. Hence the use of Meta Class to add other info, then we set abstract to true"""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
