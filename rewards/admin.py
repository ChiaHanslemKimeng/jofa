from django.contrib import admin
from .models import RewardSetting, RewardPoint

@admin.register(RewardSetting)
class RewardSettingAdmin(admin.ModelAdmin):
    list_display = ('id', 'points_per_amount', 'amount_spent', 'bonus_points', 'bonus_threshold', 'points_to_cash_ratio', 'expiry_days')

    def has_add_permission(self, request):
        has_permission = super().has_add_permission(request)
        if has_permission and RewardSetting.objects.exists():
            return False
        return has_permission

@admin.register(RewardPoint)
class RewardPointAdmin(admin.ModelAdmin):
    list_display = ('user', 'points', 'transaction_type', 'order_reference', 'created_at', 'expires_at')
    list_filter = ('transaction_type', 'created_at')
    search_fields = ('user__username', 'order_reference')
    readonly_fields = ('created_at',)
