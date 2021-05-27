from django.db import models

class Game(models.Model):

    name = models.CharField(max_length=50)
    difficulty = models.IntegerField()
    number_of_players = models.IntegerField()
    game_type = models.ForeignKey("GameType", on_delete=models.DO_NOTHING, null = True)
    gamer = models.ForeignKey("Gamer", on_delete=models.DO_NOTHING, null = True, default=1)