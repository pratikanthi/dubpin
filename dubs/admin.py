from django.contrib import admin
from dubs.models import Video, Dubs


class VideoAdmin(admin.ModelAdmin):
    pass

class DubsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Video,VideoAdmin)
admin.site.register(Dubs,DubsAdmin)
