# Data Science Project Checklists


---

## 1. Initial Data Loading & Setup
```
□ Import necessary libraries (pandas, numpy, matplotlib, seaborn)
□ Set plotting style and warning filters
□ Load dataset and display first few rows
□ Check dataset shape (rows, columns)
□ Examine data types for each column
□ Identify target variable and predictors
```

## 2. Data Quality Assessment
```
□ Check for missing values (.isna(), .count())
□ Look for duplicate rows
□ Examine unique values in categorical columns
□ Check data ranges (min/max) for numerical columns
□ Identify obviously wrong values (negative ages, impossible measurements)
□ Verify data types match expected types
□ Check for placeholder values (999, -1, "Unknown", etc.)
```

## 3. Data Cleaning & Preprocessing
```
□ Handle missing values (drop, impute, or flag)
□ Remove or fix obvious data errors
□ Standardize column names (lowercase, underscores)
□ Convert units if needed (metric to imperial, etc.)
□ Create categorical variables from numerical if appropriate
□ Remove unnecessary columns (IDs, redundant features)
□ Handle date/time formatting if applicable
```

## 4. Exploratory Data Analysis (EDA)
```
□ Generate summary statistics (.describe())
□ Create distribution plots for all numerical variables
□ Calculate and interpret skewness and kurtosis
□ Create correlation matrix and heatmap
□ Generate box plots to visualize outliers
□ Compare distributions by categorical groups
□ Create scatter plots against target variable
□ Test for normality (Shapiro-Wilk, Q-Q plots)
□ Document key findings and patterns
```

## 5. Outlier Detection & Treatment
```
□ Apply IQR method for outlier detection
□ Apply Z-score method (values > 3 std devs)
□ Visualize outliers with box plots
□ Investigate outliers (data errors vs. legitimate extremes)
□ Decide treatment approach (remove, cap, or keep)
□ Document outlier treatment decisions
□ Compare before/after statistics
```

## 6. Feature Engineering
```
□ Create derived features (BMI, ratios, rates)
□ Generate interaction terms between important variables
□ Create polynomial features if non-linear relationships exist
□ Bin continuous variables into categories if needed
□ Create dummy variables for categorical features
□ Apply feature scaling/normalization
□ Feature selection (remove low-variance or highly correlated)
□ Validate new features make logical sense
```

## 7. Pre-Modeling Preparation
```
□ Split data into train/validation/test sets
□ Ensure no data leakage between sets
□ Handle class imbalance if classification problem
□ Final feature selection based on importance/correlation
□ Scale features if required by chosen algorithms
□ Create baseline model for comparison
□ Define evaluation metrics
```

## 8. Model Building & Evaluation
```
□ Start with simple baseline model
□ Try multiple algorithm types (linear, tree-based, ensemble)
□ Perform cross-validation
□ Tune hyperparameters systematically
□ Evaluate on validation set using chosen metrics
□ Check for overfitting (train vs. validation performance)
□ Analyze feature importance
□ Test final model on holdout test set
```

## 9. Model Interpretation & Validation
```
□ Generate feature importance plots
□ Create partial dependence plots for key features
□ Analyze residuals (for regression) or confusion matrix (classification)
□ Test model assumptions
□ Validate model makes business/logical sense
□ Check model performance across different subgroups
□ Document model limitations and assumptions
```

## 10. Documentation & Reporting
```
□ Document data sources and collection methods
□ Summarize key findings from EDA
□ Explain feature engineering rationale
□ Document model selection process
□ Report final model performance with confidence intervals
□ Create visualizations for stakeholder presentation
□ List recommendations and next steps
□ Archive code and data for reproducibility
```

---

## Quick Reference: "Must-Do" Minimums

### For Every Project (The 80/20):
```
□ Check data types and missing values
□ Look at distributions (histograms)
□ Check correlations
□ Detect obvious outliers
□ Split train/test sets properly
□ Start with simple baseline model
```

### Red Flags to Always Check:
```
□ Perfect correlations (data leakage)
□ Impossible values (negative ages, 200% percentages)
□ Suspicious patterns (all values ending in 0 or 5)
□ Target variable distribution (severely imbalanced?)
□ Train/test performance gap (overfitting?)
```

### Common Mistakes to Avoid:
```
□ Using test set for feature engineering decisions
□ Scaling before train/test split
□ Ignoring domain knowledge when creating features
□ Not validating that engineered features make sense
□ Optimizing too heavily on validation set
□ Forgetting to check model assumptions
```
