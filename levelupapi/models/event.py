from django.db import models

class Event(models.Model):

    name = models.CharField(max_length=30)
    date = models.DateField(auto_now = False, auto_now_add = False)
    time = models.TimeField(auto_now = False, auto_now_add = False)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    host = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    attendees = models.ManyToManyField("Gamer", through="GamerEvent", related_name="attending")

    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value