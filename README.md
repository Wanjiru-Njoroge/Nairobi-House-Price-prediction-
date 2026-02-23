# Nairobi House Price Prediction

This project is focused on predicting house prices in Nairobi, Kenya, using data-driven machine learning approaches. The goal is to help buyers, sellers, and real estate professionals make informed decisions by providing accurate price estimates based on historical property sales data.

## Project Overview
The Nairobi House Price Prediction project involves:
- Collecting and cleaning property sales data from Nairobi.
- Exploring and analyzing the data to understand key factors influencing house prices (such as location, number of bedrooms, property type, etc.).
- Building and evaluating machine learning models to predict house prices.
- Creating an interactive application for users to input property details and receive price predictions.

### Objectives
- Identify the main features affecting house prices in Nairobi.
- Develop a robust predictive model using regression techniques.
- Visualize trends and insights from the data.
- Provide a user-friendly interface for price prediction.

### Methodology
1. **Data Collection & Cleaning**: Raw property sales data is gathered and cleaned to remove inconsistencies, missing values, and outliers.
2. **Exploratory Data Analysis (EDA)**: Statistical and visual analysis is performed to understand distributions, correlations, and feature importance.
3. **Model Development**: Various regression models (e.g., Linear Regression, Random Forest, etc.) are trained and evaluated to select the best-performing model.
4. **Deployment**: The final model is integrated into a Python app and Jupyter notebook for easy access and visualization.

### Workflow
- Data scraping and preprocessing: `Nairobi_House_Price_Predictionscrap.ipynb`
- Model training and evaluation: `Nairobi_House_Price_Predictionmodel.ipynb`
- Prediction and visualization: `aNairobi_House_Price_Predictionapp.ipynb, app.py`

## Project Structure
- **Nairobi_House_Price_Predictionapp.ipynb**: Main notebook for running the prediction app and visualizations.
- **app.py**: Python script for the prediction application.
- **kenya_property24_data_dictionary.csv**: Data dictionary describing the dataset features.
- **kenya_property24_sales_cleaned.csv**: Cleaned property sales data.
- **kenya_property24_sales.csv**: Raw property sales data.
- **Nairobi_House_Price_Predictionmodel.ipynb**: Notebook for model development and evaluation.
- **Nairobi_House_Price_Predictionscrap.ipynb**: Notebook for data scraping and preprocessing.

## Usage
1. Explore and preprocess data in `scrap.ipynb`.
2. Develop and evaluate models in `model.ipynb`.
3. Run predictions and visualize results in `app.ipynb` and `app.py`.

## Example Workflow
1. Open `scrap.ipynb` to clean and prepare the data.
2. Use `model.ipynb` to analyze features and train regression models.
3. Test the prediction app in `app.ipynb` or run `app.py` for a script-based interface.
4. Visualize results and interpret model outputs.

## Requirements
- Python 3.8+
- Jupyter Notebook
- pandas, scikit-learn, matplotlib, seaborn (install via pip)

## Getting Started
1. Clone the repository or download the project files.
2. Install required packages:
   ```bash
   pip install pandas scikit-learn matplotlib seaborn
   ```
3. Open `app.ipynb` or `model.ipynb` in Jupyter Notebook to start exploring.

## Data
The project uses property sales data from Nairobi, Kenya. The dataset includes features such as:
- Location (neighborhood)
- Number of bedrooms and bathrooms
- Property type (apartment, house, etc.)
- Land size
- Sale price
See `kenya_property24_data_dictionary.csv` for detailed feature descriptions.

## License
This project is for educational purposes.

## Author
Cameline
