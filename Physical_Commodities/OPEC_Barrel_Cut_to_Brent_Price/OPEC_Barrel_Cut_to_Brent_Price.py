import pandas as pd
import matplotlib.pyplot as plt

# Paste in manually — just 6 rows per event, no API needed
data = {
    'Event': ['Vienna 2016', 'COVID Cut 2020', 'Nov 2022 Cut', 'Saudi 2023'],
    'Price_Month_Before': [53.31, 18.38, 93.33, 74.84],  # $ per barrel — look these up
    'Price_Month_After':  [54.58, 29.38, 80.92, 80.11],  # fill in from EIA data
}

df = pd.DataFrame(data)
df['Price_Change'] = df['Price_Month_After'] - df['Price_Month_Before']
df['Pct_Change'] = (df['Price_Change'] / df['Price_Month_Before']) * 100

print(df[['Event', 'Price_Month_Before', 'Price_Month_After', 'Pct_Change']])

# Bar chart
plt.bar(df['Event'], df['Pct_Change'], color=['green' if x > 0 else 'red' for x in df['Pct_Change']])
plt.axhline(0, color='black', linewidth=0.8)
plt.title('Brent Price Change (%) After OPEC Cut Announcements')
plt.ylabel('% Change (Month Before → Month After)')
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()