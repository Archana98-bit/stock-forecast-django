from django.db import models

class StockData(models.Model):
    date = models.DateField(unique=True)
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.BigIntegerField()

    def __str__(self):
        return f"{self.date} - Close: {self.close}"


class ForecastResult(models.Model):
    model_name = models.CharField(max_length=50)  # e.g., 'ARIMA', 'Prophet', 'LSTM'
    forecast_date = models.DateField()
    predicted_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.model_name} - {self.forecast_date}: {self.predicted_value}"
