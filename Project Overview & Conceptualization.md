# Research Conceptualization & Variable Operationalization

[![Domain](https://img.shields.io/badge/Domain-E--Commerce_Analytics-blue?style=flat-square)]()
[![Focus](https://img.shields.io/badge/Focus-Dynamic_Pricing_%26_Consumer_Behavior-orange?style=flat-square)]()
[![Status](https://img.shields.io/badge/Status-Phase_1:_Conceptualization-brightgreen?style=flat-square)]()

---

## Research Context & Background

E-commerce marketplaces frequently leverage dynamic pricing strategies to maximize revenue and liquidate digital inventory ([Varian, 1980](https://www.jstor.org/stable/1803562); [Stigler, 1961](https://doi.org/10.1086/258464)). In the digital publishing sector, targeted price reductions serve as critical promotional mechanisms to boost product visibility and drive early conversion momentum ([Forman et al., 2008](https://doi.org/10.1287/isre.1080.0193)). 

This study investigates two central dynamics:
1. **Genre Variance:** How list price discounting strategies differ across distinct literary categories.
2. **Engagement Elasticity:** Whether deeper price reductions correlate with increased consumer engagement (measured via platform rating counts), and if high baseline genre popularity dampens the need for steep price cuts.

---

## Variable Framework

| Variable Type | Metric Name | Data Source | Scale / Type |
| :--- | :--- | :--- | :--- |
| **Independent** | List Price Discount (%) | `listPrice`, `retailPrice` | Continuous (Percentage) |
| **Dependent** | Consumer Engagement | `ratingsCount` | Continuous (Log-transformed) |
| **Grouping** | Book Category / Genre | `categories` | Categorical |
| **Confounding** | Genre Demand Baseline | Aggregate non-discounted metrics | Continuous |

---

## Operationalization Breakdown

### Independent Variable: List Price Discount
* **Conceptual Definition:** The relative price reduction applied to a title's official publisher list price on digital platforms.
* **Mathematical Model:**

$$\text{Discount Percentage (\%)} = \left( \frac{\text{List Price} - \text{Retail Price}}{\text{List Price}} \right) \times 100$$

> **Preprocessing Rule:** Records missing explicit values for either `listPrice` or `retailPrice` are filtered out during raw data ingestion to prevent zero-division errors.

---

### Dependent Variable: Consumer Engagement (Sales Proxy)
* **Conceptual Definition:** Total volume of user interaction recorded for a title, serving as a proxy metric for sales performance.
* **Mathematical Model:**

$$\text{Log Engagement} = \ln(\text{ratingsCount} + 1)$$

> **Statistical Rationale:** Raw rating counts typically follow a heavy right-skewed distribution. Logarithmic transformation normalizes variance for parametric statistical modeling.

---

### Grouping Variable: Book Category / Genre
* **Conceptual Definition:** The thematic classification assigned to a publication.
* **Operationalization:** Extracted from the `categories` array (e.g., *"Fiction"*, *"Computers"*, *"Business & Economics"*). Low-frequency categories are grouped into broader primary genres to ensure statistical power during cross-category ANOVA testing.

---

### Confounding Variable: Genre Popularity & Demand Trends
* **Conceptual Definition:** Baseline consumer interest for a specific genre independent of temporary price promotions.
* **Operationalization:** Calculated as the median rating count across non-discounted control titles within each category, weighted by search result market representation.

---

<details>
<summary><b> References (APA 7th Edition)</b></summary>

<br>

* Forman, C., Ghose, A., & Wiesenfeld, B. (2008). Examined versus unexamined review characteristics: The role of reviewer identity information in online product reviews. *Information Systems Research*, 19(3), 291–313. https://doi.org/10.1287/isre.1080.0193
* Stigler, G. J. (1961). The economics of information. *Journal of Political Economy*, 69(3), 213–225. https://doi.org/10.1086/258464
* Varian, H. R. (1980). A model of sales. *The American Economic Review*, 70(4), 651–659. https://www.jstor.org/stable/1803562

</details>
