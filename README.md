# Winery sales app development.
This is a Python Flask web application for managing bar data. The app uses SQLite database to store and retrieve bar product and transaction data.

## Installation
To run the app, you'll need to have Python 3 and Flask installed on your machine. You can install Flask by running the following command:

 Copy code
```pip install flask```
## Usage
To start the app, run the following command:

## Copy code
```python app.py```
Once the app is running, you can access it by visiting http://localhost:5000 in your web browser.

## The app has two main pages:

Product List: This page displays a list of all bar products, including their product code, vendor code, name, retail price, base unit, country of origin, ABV, and size. You can click on the name of a product to view its orders.

Size Information: This page displays information about the size of a particular bar product, including the cost of storage, cost of bottle, cost of transportation, percentage markup, and discount percentage.

You can navigate between these pages using the links provided on the pages.

## Files
The following files are included in the app:

**app.py**: This is the main Flask application file. It defines the app's routes and views.

**bar_data.db**: This is the SQLite database file that stores the bar product and transaction data.

**schema.sql**: This file contains the SQL code used to create the database schema.

**templates/size.html**: This file defines the HTML code for the size information page.

**templates/product_list.html**: This file defines the HTML code for the product list page.

**static/style.css**: This file contains the CSS code used to style the app's pages.

**phone_data/Product_range (1).csv**: This file contains the bar product data.

**phone_data/Transactions.csv**: This file contains the transaction data.
