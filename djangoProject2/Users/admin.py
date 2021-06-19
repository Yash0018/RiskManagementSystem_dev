from django.contrib import admin
from .models import Document, Consultant_Profile, Client_Profile, Event
# we need to register models here to make them available on admin page


admin.site.register(Consultant_Profile)
admin.site.register(Client_Profile)
# admin.site.register(Role)
admin.site.register(Document)
admin.site.register(Event)
