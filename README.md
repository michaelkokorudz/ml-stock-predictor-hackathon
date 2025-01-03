# My Contributions to the McGill-FIAM Hackathon Project

## Overview
This README highlights my specific contributions as part of a five-member team participating in the McGill-FIAM Quant Hackathon. The project aimed to apply machine learning techniques to optimize portfolio management strategies. The complete project repository can be found [here](https://github.com/michaelkokorudz/ml-algorithmic-trading).

## My Sole Contributions
### 1. **Machine Learning Implementation**
   - Developed and implemented two machine learning models:
     - **ElasticNet**: A linear regression model that combines L1 and L2 regularization to address multicollinearity and enhance generalization.
     - **XGBoost**: A robust, non-linear gradient-boosting model optimized for speed and predictive accuracy.
   - Conducted extensive hyperparameter tuning for both models:
     - **ElasticNet**: Used time-series cross-validation to optimize regularization parameters.
     - **XGBoost**: Performed randomized search to fine-tune key parameters such as tree depth, learning rate, and estimators.

### 2. **Principal Component Analysis (PCA)**
   - Conducted PCA to reduce dimensionality and address multicollinearity among financial characteristics.
   - Used a scree plot to determine the optimal number of principal components, reducing the dataset to 35 components that retained the majority of variance.

### 3. **Ensemble Prediction Strategy**
   - Combined the predictions from ElasticNet and XGBoost to balance linear and non-linear insights.
   - Designed and evaluated a strategy to improve out-of-sample R², achieving an improvement of 0.00797 compared to the baseline model.

### 4. **Backtesting and Performance Evaluation**
   - Developed and tested a long-short equity portfolio strategy using Python.
   - Key metrics evaluated:
     - Out-of-sample R²
     - Annualized Sharpe Ratio
     - Portfolio alpha
     - Maximum drawdown and other performance statistics.

### 5. **Visualization and Reporting**
   - Created visualizations for:
     - PCA scree plot to illustrate the selection of components.
     - Cumulative return plots comparing strategy performance with benchmarks (e.g., S&P 500).

---

### Team Acknowledgment
This project was a collaborative effort, and my teammates made significant contributions in areas such as data preparation, alternative model implementations, and overall strategy design. I am grateful for their teamwork and support throughout the competition.

### Repository Link
[Complete Project Repository](https://github.com/michaelkokorudz/ml-algorithmic-trading)
