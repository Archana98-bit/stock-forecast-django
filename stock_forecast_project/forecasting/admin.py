from django.contrib import admin
from .models import StockData

@admin.register(StockData)
class StockDataAdmin(admin.ModelAdmin):
    list_display = ['date', 'open', 'high', 'low', 'close', 'volume']
    search_fields = ['date']


from .models import ForecastResult

@admin.register(ForecastResult)
class ForecastResultAdmin(admin.ModelAdmin):
    list_display = ['model_name', 'forecast_date', 'predicted_value', 'created_at']
    list_filter = ['model_name']
