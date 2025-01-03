# My Contributions to the McGill-FIAM Hackathon Project

## Overview
This README highlights my specific contributions as part of a five-member team participating in the McGill-FIAM Quant Hackathon. The project aimed to apply machine learning techniques to optimize portfolio management strategies. The complete project repository can be found [here](https://github.com/michaelkokorudz/ml-algorithmic-trading).

## My Sole Contributions

### 1. **Machine Learning Implementation**
   - Developed and implemented two machine learning models:
     - **ElasticNet**: A linear regression model that combines L1 and L2 regularization to address multicollinearity and enhance generalization.
       - Used `ElasticNetCV` for hyperparameter tuning via time-series cross-validation.
       - Optimized `alpha` and `l1_ratio` parameters to maximize predictive performance.
     - **XGBoost**: A robust, non-linear gradient-boosting model optimized for speed and predictive accuracy.
       - Conducted hyperparameter tuning using `RandomizedSearchCV` with a predefined parameter grid.
       - Integrated time-series cross-validation for robust parameter optimization.

### 2. **Principal Component Analysis (PCA)**
   - Conducted PCA on stock-related variables to reduce dimensionality and address multicollinearity among features.
   - Retained the top 35 (out of 147) principal components based on variance explained, as visualized in a scree plot.

### 3. **Ensemble Prediction Strategy**
   - Combined the predictions from ElasticNet and XGBoost to balance linear and non-linear insights.
   - Averaged the predictions from both models to create a robust final prediction.
   - Achieved an out-of-sample R² of **0.008**, significantly improving upon the provided baseline model's R² of **0.005**.

### 4. **Backtesting and Performance Evaluation**
   - Utilized an expanding window approach for out-of-sample prediction:
     - **Training**: 8 years of historical data.
     - **Validation**: 2 years of data for hyperparameter tuning.
     - **Testing**: 1 year of data for model evaluation.
   - Evaluated strategy performance using key metrics:
     - Out-of-sample R² for ElasticNet, XGBoost, and their averaged predictions.
     - Other metrics calculated included Sharpe Ratio, portfolio alpha, and maximum drawdown.

### 5. **Visualization and Reporting**
   - Created visualizations for:
     - PCA scree plot to illustrate dimensionality reduction.
     - Cumulative return plots comparing the strategy's performance against benchmarks.

### 6. **Data Preprocessing**
   - Applied rank transformation and scaling to stock-related variables for standardization across months.
   - Addressed missing data by filling with monthly medians to ensure consistency in training.

---

### Team Acknowledgment
This project was a collaborative effort, and my teammates made significant contributions in areas such as data preparation, alternative model implementations, and overall strategy design. I am grateful for their teamwork and support throughout the competition.

### Repository Link
[Complete Project Repository](https://github.com/michaelkokorudz/ml-algorithmic-trading)

