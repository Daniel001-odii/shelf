from django.contrib import admin
from .models import Post
from django.contrib.auth import get_user_model
# Register your models here.



class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('Book_author', 'uploaded_on', 'uploaded_by')
    search_fields = ['title', 'level']
    prepopulated_fields = {'slug': ('title',)}

'''
    def get_form(self, request, obj=None, **kwargs):
        form = super(PostAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['uploaded_by'].initial = request.user
        return form
'''

    #--------auto select user while making posts-----------#
'''   
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "uploaded_by":
            kwargs["queryset"] = get_user_model().objects.filter(
                username=request.user.username
            )
        return super(PostAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
        )

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return self.readonly_fields + ("uploaded_by",)
        return self.readonly_fields

    def add_view(self, request, form_url="", extra_context=None):
        data = request.GET.copy()
        data["uploaded_by"] = request.user
        request.GET = data
        return super(PostAdmin, self).add_view(
            request, form_url="", extra_context=extra_context
        )
'''
admin.site.register(Post, PostAdmin)