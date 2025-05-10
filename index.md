---
layout: default
title: A/B Testing Shipping Methods
---

# 📦 A/B Test: UPS Ground vs. UPS SurePost

This project simulates an A/B test I conducted in a real-world shipping scenario, using Python and Docker.

🎯 **Goal**: Test if switching to SurePost maintains delivery reliability while saving costs.

💰 **Result**: $15K–$20K annual savings, no statistically significant drop in reliability.

---

## 📽️ Walkthrough Video

<video width="100%" controls>
  <source src="assets/video.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

---

## 🧪 Live Results

[Click here to view the analysis results](docs/ab_test_analysis.html)

---

## 🛠 Tools Used

- Python (pandas, numpy, scipy)
- Docker
- GitHub Pages + Jekyll
- CapCut (video editing)

---

## 🐳 Run This Project Locally with Docker

```bash
docker build -t ab_test .
docker run --rm ab_test
