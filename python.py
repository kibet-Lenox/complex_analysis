import pandas as pd
import matplotlib.pyplot as plt

produce_data = pd.DataFrame({"Month": ["2025-11","2025-12","2025-12","2026-01","2026-02","2026-03","2026-04","2025-11","2025-12","2025-12","2026-01","2026-02","2026-03","2026-04","2025-11","2025-12","2025-12","2026-01","2026-02","2026-03","2026-04","2025-11","2025-12","2025-12","2026-01","2026-02","2026-03","2026-04","2025-11","2025-12","2025-12","2026-01","2026-02","2026-03","2026-04"], "Vegetable": ["Tomato","Tomato","Tomato","Tomato","Tomato","Tomato","Tomato","Onion","Onion","Onion","Onion","Onion","Onion","Onion","Cabbage","Cabbage","Cabbage","Cabbage","Cabbage","Cabbage","Cabbage","Kale","Kale","Kale","Kale","Kale","Kale","Kale","Carrot","Carrot","Carrot","Carrot","Carrot","Carrot","Carrot"], "Price_KES_per_kg": [85,95,110,150,75,65,60,110,115,118,120,122,115,112,45,40,45,50,40,43,44,35,37,38,40,36,35,34,70,73,78,82,75,72,71]})
f = '='* 30

print(f)
print('NAIROBI PRODUCE MARKET.')
print(f)
print()

#vegetable with most price volatility
volatile = produce_data.groupby('Vegetable')['Price_KES_per_kg'].std().idxmax()
print(f'1. Most volatile vegetable is : {volatile}.')

#When does the most volatile peak?
tomato_data = produce_data[produce_data['Vegetable']=='Tomato']
peak = tomato_data.loc[tomato_data['Price_KES_per_kg'].idxmax()]
print(f"2.On {peak['Month']}, {peak['Vegetable']} had its peak at KES {peak['Price_KES_per_kg']}.")

#Trend chart per vegetable.
colors = {
 "Tomato":"#E74C3C",
 "Onion":"#F1C40F",
 "Cabbage":"#27AE60",
 "Kale":"#2ECC71",
 "Carrot":"#E67E22"
}

plt.figure(figsize=(10,6))
for veg in produce_data['Vegetable'].unique():
    df = produce_data[produce_data['Vegetable']==veg].sort_values('Month')
    plt.plot(df['Month'], df['Price_KES_per_kg'], color=colors[veg], marker='o', label=veg, linewidth=2.5)

plt.xlabel('Month')
plt.ylabel('Price KES per kg')
plt.title('6-Month Vegetable Price Trend')
plt.legend()
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('/storage/emulated/0/Download/trend_color.png', dpi=300)
plt.show()
