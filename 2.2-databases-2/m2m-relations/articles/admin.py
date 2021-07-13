from django.contrib import admin

from .models import Article, Tag


class ScopesInline(admin.TabularInline):
    model = Tag.articles.through


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        ScopesInline
    ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [
        ScopesInline
    ]
    exclude = ('scope_set',)
