from django.contrib import admin

from . import models


class CampaignAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created', 'is_active', )
    list_filter = ('is_active', 'created', )


class UserReferrerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'reward', )
    raw_id_fields = ('user', 'campaign', )


class ReferrerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'user_referrer', )
    raw_id_fields = ('registered_user', 'user_referrer', )


class UserReferrerStatsAdmin(admin.ModelAdmin):
    raw_id_fields = ('user_referrer', )


admin.site.register(models.Campaign, CampaignAdmin)
admin.site.register(models.UserReferrer, UserReferrerAdmin)
admin.site.register(models.Referrer, ReferrerAdmin)
admin.site.register(models.UserReferrerStats, UserReferrerStatsAdmin)
