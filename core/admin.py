from django.contrib import admin
from core.models import Autor,Categoria, Editora, Livro, ItensCompra, Compra

# Register your models here.
admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Livro)


class ItensInline(admin.TabularInline):
    model = ItensCompra

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    inlines = (ItensInline,)


