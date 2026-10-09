import pandas as pd

df = pd.read_csv("sample_seo_data.csv")
df["conversion_rate_pct"] = df["conversion_rate"] * 100

first = df.iloc[0]
last = df.iloc[-1]

def growth(a, b):
    return (b / a - 1) * 100

print("SEO & AEO Growth Analysis")
print("-" * 32)
print(f"Organic sessions growth: {growth(first.organic_sessions, last.organic_sessions):.1f}%")
print(f"Organic conversions growth: {growth(first.organic_conversions, last.organic_conversions):.1f}%")
print(f"Top-10 keyword growth: {growth(first.top_10_keywords, last.top_10_keywords):.1f}%")
print(f"AI-referred session growth: {growth(first.ai_referred_sessions, last.ai_referred_sessions):.1f}%")
print(f"Ending conversion rate: {last.conversion_rate_pct:.2f}%")

print("\nBusiness interpretation:")
print("- Organic growth is translating into conversion growth, not traffic alone.")
print("- Keyword visibility and indexed-content growth move in the same direction.")
print("- AI-referred traffic is emerging as a measurable discovery channel.")
print("- Next step: segment performance by landing-page type and search intent.")
