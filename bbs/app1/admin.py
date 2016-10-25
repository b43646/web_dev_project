from django.contrib import admin
import models
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment','parent_comment','article')

admin.site.register(models.Article)
admin.site.register(models.Category)
admin.site.register(models.ThumbUp)
admin.site.register(models.Comment,CommentAdmin)
admin.site.register(models.UserProfile)
admin.site.register(models.UserGroup)