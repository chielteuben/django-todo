from django.contrib import admin
from todo.models import Item, Category, User, List, Comment

class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'list', 'category', 'priority', 'due_date')
    list_filter = ('list', 'category',)
    ordering = ('priority',)
    search_fields = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'enabled',)

admin.site.register(List)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment)
admin.site.register(Item,ItemAdmin)
