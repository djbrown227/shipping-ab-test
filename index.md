---
layout: default
title: A/B Testing Shipping Methods
---

# 📦 A/B Test: UPS Ground vs. UPS SurePost

This project simulates a real-world A/B test I performed to determine whether switching from **UPS Ground** to the more affordable **UPS SurePost** could reduce costs **without compromising delivery reliability**.

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
<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
  <iframe src="https://www.youtube.com/embed/VIDEO_ID" 
          frameborder="0" 
          allowfullscreen 
          style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;">
  </iframe>
</div>

---

## 📊 Visuals

### 📈 Distribution of Shipping Costs

*Histogram comparing cost distributions of UPS Ground and SurePost*

![Shipping Cost Distribution](assets/shipping_cost_distribution.png)

---

### 📦 Boxplot of Costs by Service

*Boxplot visualizing cost variation and outliers for each service*

![Shipping Cost Boxplot](assets/shipping_cost_boxplot.png)

---

## 📌 Key Findings

- **No statistically significant difference** in delivery success rates  
- **UPS SurePost** is **~$1 cheaper** per shipment on average  
- Projected **annual savings of $15,000–$20,000** based on historical shipping volumes

---

## 🛠️ Tools Used

- **Python**: pandas, numpy, scipy, seaborn, matplotlib  
- **Docker** for containerized runs  
- **Jekyll + GitHub Pages** for publishing this project  
- **CapCut** for video editing

---

## 🐳 Run This Project Locally with Docker

```bash
docker build -t ab_test .
docker run --rm ab_test
