---
layout: default
title: A/B Testing Shipping Methods
---

# 📦 A/B Test: UPS Ground vs. UPS SurePost

This project simulates a real-world A/B test I performed to determine whether switching from **UPS Ground** to the more affordable **UPS SurePost** could reduce costs **without compromising delivery reliability**.

🧠 Note: Due to confidentiality, the data shown here is simulated using Python to match the structure and characteristics of the original Shopify export.

---

## 🎯 Objective

- Evaluate whether **UPS SurePost** provides delivery reliability comparable to **UPS Ground**
- Estimate potential **annual cost savings**
- Simulate shipping data using Python and statistically test differences in delivery success

---

## 🧪 Methodology

- Synthetic shipping data generated with:
  - 10,000 random orders
  - Random assignment of shipping service
  - 95% delivery success rate for both services
  - Normal distribution of shipping costs (mean: $10 for Ground, $9 for SurePost)

- Statistical analysis:
  - **Chi-Square Test** to test for independence in delivery success between services
  - Comparison of average shipping costs to estimate annual savings

---

## 📽️ Walkthrough Video

<!-- Replace `VIDEO_ID` with your YouTube video ID -->
<iframe width="100%" height="400" src="https://www.youtube.com/embed/QNwY8eO2vUU" frameborder="0" allowfullscreen></iframe>

---

## 📊 Visuals

### 📈 Shipping Failure Rates

*Bar Chart comparing failure rates of UPS Ground and SurePost*

![Shipping Failure Rate Bar Chart](assets/Screenshot 2025-05-13 at 2.13.00 PM.png)

---
### 📈 Chi-Squared Test Results
*Chi-Squared Test testing failure rates of UPS Ground and SurePost*
![Shipping Failure Rate Bar Chart](assets/Screenshot 2025-05-13 at 2.16.09 PM.png)
---

### 📦 Boxplot of Costs by Service

*Boxplot visualizing cost variation and outliers for each service*

![Shipping Cost Boxplot](assets/Shipping_Cost_Boxplots.png)

---

## 📌 Key Findings

- **No statistically significant difference** in delivery success rates  
- **UPS SurePost** is **~$1 cheaper** per shipment on average  
- Projected **annual savings of $15,000–$20,000** based on historical shipping volumes

---

## 🛠️ Tools Used

- **Python**: pandas, numpy, scipy, seaborn, matplotlib  
- **Jekyll + GitHub Pages** for publishing this project  
- **CapCut** for video editing

---
