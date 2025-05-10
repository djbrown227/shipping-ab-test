import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data.generate_synthetic_data import generate_shipping_data
import pandas as pd
from scipy.stats import chi2_contingency

def run_ab_test():
    df = generate_shipping_data()  # generates AND returns a DataFrame

    # Now you use the freshly created data
    contingency_table = pd.crosstab(df['Service'], df['Was package delivered'])
    chi2, p_value, _, _ = chi2_contingency(contingency_table)

    avg_ground = df[df['Service'] == "UPS Ground"]['Cost to deliver'].mean()
    avg_surepost = df[df['Service'] == "UPS SurePost"]['Cost to deliver'].mean()
    cost_savings = (avg_ground - avg_surepost) * len(df)

    print("=== Contingency Table ===\n", contingency_table, "\n")
    print(f"Chi-square Statistic: {chi2:.4f}")
    print(f"P-value: {p_value:.4f}")
    print(f"Average Cost - UPS Ground: ${avg_ground:.2f}")
    print(f"Average Cost - UPS SurePost: ${avg_surepost:.2f}")
    print(f"Estimated Cost Savings for {len(df)} shipments: ${cost_savings:,.2f}")

if __name__ == "__main__":
    run_ab_test()
