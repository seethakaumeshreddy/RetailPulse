import pandas as pd
import matplotlib.pyplot as plt

forecast = pd.read_csv(
    "data/forecast_results.csv"
)

plt.figure(figsize=(10,5))

plt.plot(
    forecast["ds"],
    forecast["yhat"]
)

plt.xticks(rotation=45)

plt.title(
    "Sales Forecast"
)

plt.tight_layout()

plt.savefig(
    "reports/forecast.png"
)

plt.show()

print("Forecast graph saved")