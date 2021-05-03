from django.db import models

class Event(models.Model):

    name = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now = False, auto_now_add = False)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    host = models.ForeignKey("Gamer", on_delete=models.CASCADE)