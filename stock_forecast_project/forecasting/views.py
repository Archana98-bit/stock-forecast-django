import os
import pandas as pd
from django.shortcuts import render

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def home(request):
    csv_path = os.path.join(BASE_DIR, 'forecasting', 'data', 'ibm_stock_cleaned.csv')
    df = pd.read_csv(csv_path, parse_dates=['Unnamed: 0'])
    df.rename(columns={'Unnamed: 0': 'date'}, inplace=True)
    recent_data = df.tail(30)
    context = {
        'recent_data': recent_data.to_dict(orient='records'),
        'plot_close': 'forecasting/arima_forecast_comparison.png',
        'bg_class': 'bg-dark text-white',
    }
    return render(request, 'forecasting/home.html', context)

def forecasts(request):
    context = {
        'arima_plot': 'forecasting/arima_forecast_comparison.png',
        'prophet_plot': 'forecasting/prophet_forecast.png',
        'lstm_plot': 'forecasting/lstm_forecast_comparison.png',
        'bg_class': 'bg-dark text-white',
    }
    return render(request, 'forecasting/forecasts.html', context)

def metrics(request):
    metrics_path = os.path.join(BASE_DIR, 'forecasting', 'data', 'model_comparison_metrics.csv')
    metrics_df = pd.read_csv(metrics_path)
    metrics = metrics_df.to_dict(orient='records')
    context = {
        'metrics': metrics,
        'bg_class': 'bg-dark text-white',
    }
    return render(request, 'forecasting/metrics.html', context)


from forecasting.models import StockData
import pandas as pd

def get_stock_dataframe():
    queryset = StockData.objects.all().order_by('date')
    df = pd.DataFrame(list(queryset.values('date', 'open', 'high', 'low', 'close', 'volume')))
    return df


from django.shortcuts import render
from forecasting.models import ForecastResult
import pandas as pd
import plotly.express as px
import plotly.io as pio

def forecast_dashboard(request):
    queryset = ForecastResult.objects.all().order_by('forecast_date')
    df = pd.DataFrame(list(queryset.values()))

    if df.empty:
        chart_html = "<p>No Forecasts Available.</p>"
    else:
        fig = px.line(df, x='forecast_date', y='predicted_value', color='model_name',
                      title='Forecast Results')
        chart_html = pio.to_html(fig, full_html=False)

    return render(request, 'forecasting/dashboard.html', {'chart': chart_html, 'bg_class': 'bg-dark text-black'})
