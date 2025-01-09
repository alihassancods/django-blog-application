from django.contrib import admin
from .models import Post
# Register your models here. This will add the models to admin panel
# admin.site.register(Post)
# Now to customize How the Models look in admin panel
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    The @admin.register() decorator performs the same function as the 
    admin.site.register() function that you replaced, registering the ModelAdmin class that it decorates
    """
    list_display = ['title','slug','publishDate','created','updated','author'] # list of details on admin panel
    list_filter = ['status','created','publishDate'] # list of details on which to filter
    search_fields = ['title','body'] # list of details on which to search
    prepopulated_fields = {'slug': ('title',)} # prepopulating the slug field using the title as input, if we do body as input then it will be using body
    raw_id_fields = ['author']
    date_hierarchy = 'publishDate' # below searchbar there is a date hierachy field
    ordering = ['status', 'publishDate'] # specifying the default sorting criteria
    show_facets = admin.ShowFacets.ALWAYS # facet counts showing total number of Post Objects Against each filter
