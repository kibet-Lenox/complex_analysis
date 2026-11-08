

## Nairobi Produce Market - Price Tracker

A 6-month price volatility tracker for Nairobi market produce.
Logs monthly prices for Tomato, Onion, Cabbage, Kale, and Carrot. Identifies the most volatile vegetable, its peak price month, and generates a color-coded trend chart.

## What It Does

- Accepts 6-month produce data (month, vegetable, price KES per kg)
- Calculates price volatility using standard deviation per vegetable
- Finds peak price month for the most volatile crop
- Generates a 6-month trend chart per vegetable

## Setup
pip install pandas matplotlib
## Usage
from produce_tracker import analyze_market

result = analyze_market()
print(result["volatile"])
print(result["peak"])
## Sample Output

NAIROBI PRODUCE MARKET.


1. Most volatile vegetable is : Tomato.
2.On 2026-01, Tomato had its peak at KES 150.
Trend chart saved as `trend_color.png` - Tomato peaks in Jan 2026 during shortage season.

## Stack

Python, pandas, matplotlib
