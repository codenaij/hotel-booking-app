from django.db import models
from users import models as user_models
from rooms import models as room_models

# Create your models here.
from core import models as core_models


class Review(core_models.TimeStampedModel):

    review = models.TextField()
    accuracy = models.IntegerField()
    cleaniness = models.IntegerField()
    communication = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey(user_models.User,related_name="reviews", on_delete=models.CASCADE)
    room = models.ForeignKey(room_models.Room,related_name="reviews", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.review} - {self.room}'

    def rating_average(self):
        avg = (
            self.accuracy
            + self.cleaniness
            + self.communication
            + self.location
            + self.check_in
            + self.value
        ) / 6

        return round(avg, 2)
    rating_average.short_description = "Avg."
