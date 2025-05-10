# A/B Test: UPS Ground vs. SurePost

This project simulates an A/B test comparing delivery times between UPS Ground and UPS SurePost.

## 📈 Purpose

Reduce shipping costs by verifying whether SurePost is as reliable as Ground for orders over $40.

## 🧪 Analysis Summary

- Statistical test: Two-sample t-test
- Result: No significant difference in delivery times (p > 0.05)
- Savings: $15,000–$20,000/year

## 🚀 Run Analysis Locally

```bash
docker build -t ab_test .
docker run --rm ab_test
