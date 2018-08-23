from django.contrib import admin

# Register your models here.

from .models import Topic_1, Entry_1, Topic_2, Entry_2, Topic_3, Entry_3, Topic_4, Entry_4

admin.site.register(Topic_1)
admin.site.register(Entry_1)

admin.site.register(Topic_2)
admin.site.register(Entry_2)


admin.site.register(Topic_3)
admin.site.register(Entry_3)

admin.site.register(Topic_4)
admin.site.register(Entry_4)
