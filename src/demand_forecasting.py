import pandas as pd

print("Generating Forecast...")

df = pd.read_csv("data/forecast_data.csv")

forecast_value = df["y"].tail(30).mean()

future_dates = pd.date_range(
    start=df["ds"].max(),
    periods=31,
    freq="D"
)[1:]

forecast = pd.DataFrame({
    "ds": future_dates,
    "yhat": forecast_value
})

forecast.to_csv(
    "data/forecast_results.csv",
    index=False
)

print("forecast_results.csv created successfully")
print(forecast.head())