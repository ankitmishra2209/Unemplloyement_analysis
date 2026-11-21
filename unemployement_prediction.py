import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. Load BOTH Files ---
df1 = pd.read_csv("Unemployment_in_India.csv")
df2 = pd.read_csv("Unemployment_Rate_upto_11_2020.csv")

print(f"File 1: {len(df1)} rows")
print(f"File 2: {len(df2)} rows")

# Clean column names - both files have spaces problem
df1.columns = [c.strip() for c in df1.columns]
df2.columns = [c.strip() for c in df2.columns]

# File 2 has extra duplicate column 'Region.1' - drop it
if 'Region.1' in df2.columns:
    df2 = df2.drop(columns=['Region.1'])

# Rename same in both
rename_map = {
    'Estimated Unemployment Rate (%)': 'Unemployment',
    'Estimated Employed': 'Employed',
    'Estimated Labour Participation Rate (%)': 'Labour_Participation'
}
df1 = df1.rename(columns=rename_map)
df2 = df2.rename(columns=rename_map)

# --- 2. COMBINE ---
df = pd.concat([df1, df2], ignore_index=True)

# Date fix
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# Drop blank + duplicate rows (Jan-June 2020 is in BOTH files)
df = df.dropna(subset=['Unemployment', 'Date'])
df = df.drop_duplicates(subset=['Region', 'Date', 'Area'])
df = df.sort_values('Date')

print(f"\nAfter Merge: {len(df)} rows")
print(f"States: {df['Region'].nunique()}")
print(f"Full Range: {df['Date'].min().date()} to {df['Date'].max().date()}")
print(f"Avg Unemployment: {df['Unemployment'].mean():.2f}%")
print(f"Pre-Covid: {df[df['Date']<'2020-03-01']['Unemployment'].mean():.2f}%")
print(f"Apr 2020: {df[df['Date']=='2020-04-30']['Unemployment'].mean():.2f}%")
print(f"May 2020: {df[df['Date']=='2020-05-31']['Unemployment'].mean():.2f}%")
print(f"Oct 2020 (Recovery): {df[df['Date']=='2020-10-31']['Unemployment'].mean():.2f}%")

# --- 3. ALL 6 GRAPHS - Now with Full Timeline ---

# Graph 1: Full Trend May 2019 - Oct 2020
plt.figure(figsize=(13,5))
trend = df.groupby('Date')['Unemployment'].mean()
plt.plot(trend.index, trend.values, marker='o', color='red', linewidth=2)
plt.axvspan(pd.to_datetime('2020-03-01'), pd.to_datetime('2020-06-01'), color='yellow', alpha=0.3, label='Lockdown')
plt.title("1. Full Trend May 2019 - Oct 2020 - Covid Spike + Recovery")
plt.ylabel("Unemployment (%)"); plt.grid(alpha=0.3); plt.legend(); plt.show()

# Graph 2: Rural vs Urban - Full
plt.figure(figsize=(13,5))
rural = df[df['Area']=='Rural'].groupby('Date')['Unemployment'].mean()
urban = df[df['Area']=='Urban'].groupby('Date')['Unemployment'].mean()
plt.plot(rural.index, rural.values, marker='o', label='Rural', color='green')
plt.plot(urban.index, urban.values, marker='s', label='Urban', color='blue')
plt.title("2. Rural vs Urban - Urban Hit Harder")
plt.ylabel("Unemployment (%)"); plt.legend(); plt.grid(alpha=0.3); plt.show()

# Graph 3: Worst vs Best States
plt.figure(figsize=(12,6))
df.groupby('Region')['Unemployment'].mean().sort_values().tail(10).plot(kind='barh', color='red')
plt.title("3a. Worst 10 States (Combined Data)"); plt.xlabel("Avg %"); plt.show()

plt.figure(figsize=(12,6))
df.groupby('Region')['Unemployment'].mean().sort_values().head(10).plot(kind='barh', color='green')
plt.title("3b. Best 10 States (Combined Data)"); plt.xlabel("Avg %"); plt.show()

# Graph 4: Before vs Lockdown vs Recovery (Now till Oct)
plt.figure(figsize=(10,5))
df['Period'] = pd.cut(df['Date'], bins=[pd.to_datetime('2019-05-01'), pd.to_datetime('2020-02-29'), pd.to_datetime('2020-05-31'), pd.to_datetime('2020-10-31')], labels=['Pre-Covid', 'Lockdown\n(Apr-May 20)', 'Recovery\n(Jun-Oct 20)'])
df.groupby('Period', observed=True)['Unemployment'].mean().plot(kind='bar', color=['green','red','orange'])
plt.title("4. Covid Impact - Pre vs Lockdown vs Recovery (Till Oct 2020)")
plt.ylabel("Avg Unemployment (%)"); plt.xticks(rotation=0); plt.show()

# Graph 5: Labour Participation
plt.figure(figsize=(13,5))
lp = df.groupby('Date')['Labour_Participation'].mean()
plt.plot(lp.index, lp.values, marker='o', color='purple')
plt.title("5. Labour Participation Fell in Covid, Recovered After")
plt.ylabel("Labour Participation (%)"); plt.grid(alpha=0.3); plt.show()

# Graph 6: Correlation
plt.figure(figsize=(8,5))
sns.heatmap(df[['Unemployment','Employed','Labour_Participation']].corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title("6. Correlation Heatmap"); plt.show()