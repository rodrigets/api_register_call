from django.db import models
import uuid

CALLING_TYPE = (
    ('start', 'Start'),
    ('stop', 'Stop'),
)


class Register(models.Model):
    name = 'register'

    call_type = models.CharField(max_length=5, 
                                 choices=CALLING_TYPE)

    call_datetime = models.DateTimeField()

    source_number = models.CharField(max_length=11)

    destine_number = models.CharField(max_length=11)

    call_code = models.UUIDField(editable=False,
                                 default=uuid.uuid1)

    def __str__(self):
        return self.call_type + ' - ' + str(self.source_number)

    def get_form(self, request, obj=None, **kwargs):
       self.exclude = ("call_code", )
       form = super(Register, self).get_form(request, obj, **kwargs)
       return form
