import pandas as pd
from django.core.management.base import BaseCommand
from forecasting.models import ForecastResult

class Command(BaseCommand):
    help = 'Export forecast results to a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Output CSV file path')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        forecasts = ForecastResult.objects.all().values('model_name', 'forecast_date', 'predicted_value', 'created_at')
        df = pd.DataFrame(forecasts)
        df.to_csv(csv_file, index=False)
        self.stdout.write(self.style.SUCCESS(f'Exported {len(df)} rows to {csv_file}'))
