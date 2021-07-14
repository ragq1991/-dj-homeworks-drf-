from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        save_access = False
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            if form.cleaned_data.get('is_main') is True:
                save_access = True
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
        if save_access is False:
            raise ValidationError('Не указан главный Тэг')
        return super().clean()  # вызываем базовый код переопределяемого метода


class ScopeInline(admin.StackedInline):
    model = Scope
    formset = ScopeInlineFormset


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


# @admin.register(Tag)
# class TagAdmin(admin.ModelAdmin):
#     inlines = [
#         ScopesInline
#     ]
#     exclude = ('scope',)
