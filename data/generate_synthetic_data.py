import pandas as pd
import numpy as np

def generate_shipping_data(n_samples=10000, seed=42):
    """
    Generate synthetic shipping data for A/B testing with cost distribution.

    Parameters:
        n_samples (int): Number of samples to generate
        seed (int): Random seed for reproducibility

    Returns:
        pd.DataFrame: Simulated shipping dataset
    """
    np.random.seed(seed)
    
    services = np.random.choice(["UPS Ground", "UPS SurePost"], n_samples)
    delivery_success = np.random.binomial(1, 0.95, n_samples)

    # Create cost distributions
    costs = []
    for service in services:
        if service == "UPS Ground":
            cost = np.random.normal(loc=10, scale=np.sqrt(3))  # mean=10, variance=3
        else:
            cost = np.random.normal(loc=9, scale=np.sqrt(3))   # mean=9, variance=3
        costs.append(round(cost, 2))  # round to 2 decimal places

    data = {
        "Order #": range(1, n_samples + 1),
        "Service": services,
        "Was package delivered": delivery_success,
        "Cost to deliver": costs
    }

    df = pd.DataFrame(data)

    # Save the data to a CSV file in the 'data' folder
    df.to_csv('data/shipping_data.csv', index=False)

    return df
