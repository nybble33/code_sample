from django.contrib import admin

from cms.models import Page, MenuItem

# Register your models here.


class PageAdmin(admin.ModelAdmin):
    radio_fields = {"status": admin.HORIZONTAL}
    ordering = ['title']
    prepopulated_fields = {'slug' : ('title',)}
    list_display = (
        'title',
        'collection',
        'slug',
        'modified',
        'status'
        )
    list_editable = ('collection', 'status')
    search_fields = ('title', 'slug')
    list_filter = ('modified',)
    date_hierarchy = 'modified'
    fields = (
        'title',
        'collection',
        'slug',
        'content_type',
        'category_type',
        'show_for_users',
        'status', 'content',
        'meta_keywords',
        'meta_description'
        )

    class Media:
        js = (
                #'/static/js/tinymce.min.js',
                'https://cdn.tiny.cloud/1/78rxwcvjub5zwac30yn285bg5vhopuu80m3obgyemo99oczj/tinymce/5/tinymce.min.js',
                '/static/js/admin/page.js',
                )

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class MenuItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'slug', 'parent','url', 'active')
    list_editable = ('parent', 'slug', 'url', 'active')

admin.site.register(Page, PageAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
