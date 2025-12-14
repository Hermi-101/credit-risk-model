# credit-risk-model
Credit Scoring Business Understanding
1. How does the Basel II Accord’s emphasis on risk measurement influence our need for an interpretable and well-documented model?
The Basel II Capital Accord sets international standards for banking regulation, specifically concerning how banks should manage and measure risk. Its influence makes model interpretability and documentation non-negotiable requirements for Bati Bank:



Regulatory Compliance (Pillar 1): Basel II requires banks to calculate regulatory capital based on risk exposure. To use internal models for this calculation, Bati Bank must demonstrate that the model is robust, accurate, and, crucially, auditable. An interpretable model allows regulators to understand and validate the logic behind the risk scores, ensuring the bank is holding the correct amount of capital against potential losses.




Model Validation and Auditability: The Accord mandates continuous validation and monitoring of internal models. Well-documented, transparent models allow internal teams and external auditors to trace the relationship between input features and the resulting risk score, facilitating error checking and preventing significant "model risk".



Explainability for Decisions: Transparency is required to explain risk decisions to both regulators and customers. A simple, documented model allows the bank to justify why a customer received a specific risk probability score, which is vital for fair lending practices and compliance.

2. Since we lack a direct "default" label, why is creating a proxy variable necessary, and what are the potential business risks of making predictions based on this proxy?
Necessity of a Proxy Variable:

Traditional credit scoring relies on historical data of loan performance (e.g., direct default labels).

The data provided is from an eCommerce platform, and therefore, lacks this traditional label.

The core innovation in this project is the transformation of customer behavioral data (Recency, Frequency, Monetary - RFM patterns) into a synthetic predictive risk signal. The proxy variable (high-risk/low-risk) is necessary to create a binary target label for supervised machine learning, which then allows the model to output a continuous risk probability score.



Potential Business Risks of Using a Proxy:


Proxy Inaccuracy Risk: The fundamental risk is that the behavioral proxy (e.g., "low engagement" from RFM clustering ) may not perfectly correlate with actual credit default (the failure to repay a loan principal and interest ).



Financial Misclassification: An inaccurate proxy leads to:


False Positives (High-Risk/Good Customer): Denying credit to truly creditworthy customers, resulting in lost revenue opportunities for Bati Bank and the eCommerce partner.


False Negatives (Low-Risk/Bad Customer): Granting credit to customers who will actually default, leading to financial losses (principal and interest) for Bati Bank.

3. What are the key trade-offs between using a simple, interpretable model (like Logistic Regression with WoE) versus a complex, high-performance model (like Gradient Boosting) in a regulated financial context?\


Model Type,Primary Benefit,Key Trade-Off (Risk/Cost)
"Simple, Interpretable Model (e.g., Logistic Regression with WoE)","Regulatory Acceptance & Interpretability. The Weight of Evidence (WoE) transformation and Logistic Regression results in a transparent, scorecard-like model whose predictions are easy to explain and audit for Basel II compliance.","Lower Predictive Performance. It may not capture complex, non-linear relationships in the data as effectively as complex models, potentially leaving some predictive accuracy on the table."
"Complex, High-Performance Model (e.g., Gradient Boosting)","Higher Predictive Accuracy. It is typically better at capturing intricate data patterns, leading to a better separation between good and bad risk categories and potentially lower loss rates.","Poor Interpretability (""Black Box""). Explaining the exact reason for a customer's score is difficult. This opacity complicates regulatory validation and makes compliance with Basel II's transparency requirements challenging."