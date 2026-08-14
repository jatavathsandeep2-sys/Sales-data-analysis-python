# HRMS Onboarding, Performance & AI-Features Analytics Dashboard

Analysis of HRMS data across onboarding, performance, training, and employee exits — with tracked KPIs and workforce trend insights designed to power a Power BI dashboard for HR stakeholders.

## Tools & Libraries
SQL (DuckDB) · Python · Pandas · Matplotlib · Seaborn · Power BI (DAX)

## Dataset
`data/hrms_data.csv` — 800 employee records covering department, location, hire source, onboarding timeline, performance ratings, training completion, exit status/reason, and AI smart-feature usage logs (chatbot queries, recommendation clicks, mood index).

## What This Project Covers
- **Onboarding:** on-time completion rate by department
- **Performance:** average rating trends by department and location
- **Attrition:** exit rate by department and top exit reasons
- **Training:** module completion rate by department
- **Onboarding → Performance link:** does faster onboarding correlate with better early performance?
- **AI smart-features:** relationship between chatbot/recommendation engagement and employee mood index

SQL logic for every KPI is in [`sql_queries.sql`](sql_queries.sql); the same queries were also used to build the KPI measures for the accompanying Power BI dashboard.

## Key Findings
1. Onboarding on-time completion rate varies meaningfully across departments — some show clear process bottlenecks.
2. Performance ratings are fairly consistent org-wide (~3.4–3.9 average), no major outlier department.
3. Attrition is concentrated in specific departments, driven mainly by "Better Opportunity" and "Compensation" as exit reasons.
4. Employees with on-time onboarding show slightly higher early performance ratings.
5. Higher engagement with AI chatbot/recommendation features is associated with a modestly higher employee mood index.

## How to Run
```bash
pip install pandas numpy duckdb matplotlib seaborn jupyter
python generate_data.py         # generates data/hrms_data.csv
jupyter notebook HRMS_Analysis.ipynb
```

## Sample Output
![Attrition by Department](images/attrition_by_department.png)
![Performance by Department](images/performance_by_department.png)

---
*Part of my Data Analyst portfolio. Dataset is synthetically generated to reflect realistic organizational HR patterns.*
