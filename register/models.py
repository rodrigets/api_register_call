from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

CALLING_TYPE = (
    ('Start', 'start'),
    ('Stop', 'stop'), 
)


class Register(models.Model):
    name ='register'
    
    call_type = models.CharField(max_length=5, choices=CALLING_TYPE)
    time = models.DateTimeField() 
    call_id = models.ForeignKey('register', on_delete=models.CASCADE,)
    source = models.IntegerField(validators=[MaxValueValidator(9),
            MinValueValidator(8)])
    destination = models.IntegerField(validators=[MaxValueValidator(9),
            MinValueValidator(8)])

    def __str__(self):
        return self.call_type + ' - ' + str(self.source)
