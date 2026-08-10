from django.db import models

class Academy(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Academies"

class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)

    # ForeignKey linking the player to an academy.
    # 'null=True' allows a player to exist without an academy (e.g., free agent)
    academy = models.ForeignKey(
        Academy,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='players'
    )

    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"