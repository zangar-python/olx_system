from django.db import models

TYPE_CHOICES = [
    ("rating","rating"),
    ("ad","ad"),
    ("login","login"),
    ("register","register")
]

class StoryOfSystem(models.Model):
    type_of = models.CharField(max_length=15,choices=TYPE_CHOICES)
    info = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.type