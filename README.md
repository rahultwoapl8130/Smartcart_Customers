# Smartcart Customer Analysis

This project focuses on analyzing customer data to uncover insights regarding purchasing habits, demographics, and campaign responses. The analysis is designed to assist in customer segmentation and targeted marketing strategies.

## Project Overview

The core of this project is a data analysis pipeline built inside a Jupyter Notebook. We explore a dataset of customers to identify patterns in how different demographics interact with various product categories (like wines, fish, sweets, and gold products) and purchasing channels (web, store, catalog).

### Key Features
- **Demographic Analysis:** Explores relationships between age, education, marital status, income, and household composition.
- **Purchasing Behavior:** Analyzes spending across multiple categories and through various shopping mediums.
- **Data Visualization:** Uses Pandas, Matplotlib, and Seaborn to create intuitive graphs and charts to display findings.

## Files in this Repository

- `smartcart_customer.ipynb`: The main Jupyter Notebook containing the Python code, data processing steps, visualizations, and insights.
- `requirements.txt`: The list of Python dependencies required to run the notebook and serve it interactively.

## Deployment via Render (Voilà)

This project is configured to be deployed as an interactive web application using **Voilà** on [Render.com](https://render.com/). Voilà transforms the Jupyter Notebook into a secure, standalone web application, hiding the source code and only displaying the interactive outputs and markdown text.

### How to Run Locally

If you want to run this project on your own machine:

1. Clone the repository:
   ```bash
   git clone https://github.com/rahultwoapl8130/Smartcart_Customers.git
   ```
2. Navigate into the folder:
   ```bash
   cd Smartcart_Customers
   ```
3. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the notebook interactively using Voilà:
   ```bash
   voila smartcart_customer.ipynb
   ```
   Or open it in Jupyter Notebook/Lab to edit the code:
   ```bash
   jupyter notebook
   ```
