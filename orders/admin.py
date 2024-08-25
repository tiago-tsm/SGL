from django.contrib import admin
from .models import Orders, Product



class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'produto', 'quantidade', 'forma_pagamento', 'total_compra', 'data_hora_registro')
    search_fields = ('cliente__nome', 'produto__title')
    list_filter = ('forma_pagamento', 'data_hora_registro')
    readonly_fields = ('total_compra',)  # Se você deseja que total_compra seja somente leitura

    def save_model(self, request, obj, form, change):
        # Atualiza o total_compra antes de salvar o objeto
        obj.total_compra = obj.produto.selling_price * obj.quantidade
        super().save_model(request, obj, form, change)


admin.site.register(Orders, OrdersAdmin)
