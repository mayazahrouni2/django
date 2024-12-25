from django.contrib import admin
from categoryApp.models import Category
#vous indiquez que les utilisateurs pourront rechercher des catégories en fonction de leur titre.
class CategoryAdmin(admin.ModelAdmin):
    search_fields= ('title',)

admin.site.register(Category,CategoryAdmin)
