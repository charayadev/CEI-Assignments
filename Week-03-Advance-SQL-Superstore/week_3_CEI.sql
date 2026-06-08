
/*

Step 1: Setup Data

*/




-- create the superstore_raw

CREATE TABLE SUPERSTORE_RAW (
	ROW_ID INT,
	ORDER_ID VARCHAR(50),
	ORDER_DATE DATE,
	SHIP_DATE DATE,
	SHIP_MODE VARCHAR(50),
	CUSTOMER_ID VARCHAR(50),
	CUSTOMER_NAME VARCHAR(100),
	SEGMENT VARCHAR(50),
	COUNTRY VARCHAR(100),
	CITY VARCHAR(100),
	STATE VARCHAR(100),
	POSTAL_CODE INT,
	REGION VARCHAR(50),
	PRODUCT_ID VARCHAR(50),
	CATEGORY VARCHAR(50),
	SUB_CATEGORY VARCHAR(50),
	PRODUCT_NAME VARCHAR(255),
	SALES NUMERIC(10, 2),
	QUANTITY INT,
	DISCOUNT NUMERIC(5, 2),
	PROFIT NUMERIC(10, 2)
);

-- after the data import lets check the data
SELECT
	*
FROM
	SUPERSTORE_RAW;



-- Customers tables creation


CREATE TABLE customers AS
SELECT DISTINCT
    customer_id,
    customer_name,
    segment,
    country,
    city,
    state,
    postal_code,
    region
FROM superstore_raw;


-- check customers 
SELECT
	*
FROM
	CUSTOMERS;



-- Orders tables creation
CREATE TABLE orders AS
SELECT DISTINCT
    order_id,
    order_date,
    ship_date,
    ship_mode,
    customer_id,
    sales,
    quantity,
    discount,
    profit
FROM superstore_raw;


-- check orders
SELECT
	*
FROM
	ORDERS;


-- products table creation
CREATE TABLE products AS
SELECT DISTINCT
    product_id,
    category,
    sub_category,
    product_name
FROM superstore_raw;

-- check products
SELECT
	*
FROM
	PRODUCTS;




/*

Step 2: Perform Required Queries 

*/




-- 1. Find all orders where sales are greater than the average sales. (Subquery)  

SELECT
	*
FROM
	ORDERS
WHERE
	SALES > (
		SELECT
			AVG(SALES)
		FROM
			ORDERS
	);

	
-- Find the highest sales order for each customer. (Subquery)  

SELECT
	*
FROM
	SUPERSTORE_RAW AS S
WHERE
	SALES = (
		SELECT
			MAX(SALES)
		FROM
			SUPERSTORE_RAW AS C
		WHERE
			C.CUSTOMER_ID = S.CUSTOMER_ID
	);


-- Calculate total sales for each customer. (CTE)  

WITH
	CUSTOMER_SALES AS (
		SELECT
			CUSTOMER_ID,
			CUSTOMER_NAME,
			SUM(SALES) AS TOTAL_SALES
		FROM
			SUPERSTORE_RAW
		GROUP BY
			CUSTOMER_ID,
			CUSTOMER_NAME
	)

SELECT
	*
FROM
	CUSTOMER_SALES;


-- Find customers whose total sales are above average. (CTE + Subquery)  
WITH
	CUSTOMER_SALES AS (
		SELECT
			CUSTOMER_ID,
			CUSTOMER_NAME,
			SUM(SALES) AS TOTAL_SALES
		FROM
			SUPERSTORE_RAW
		GROUP BY
			CUSTOMER_ID,
			CUSTOMER_NAME
	)


SELECT
	*
FROM
	CUSTOMER_SALES
WHERE
	TOTAL_SALES > (
		SELECT
			AVG(TOTAL_SALES)
		FROM
			CUSTOMER_SALES
	);

--   Rank all customers based on total sales. (Window Function)
SELECT
	CUSTOMER_ID,
	CUSTOMER_NAME,
	SUM(SALES) AS TOTAL_SALES,
	RANK() OVER (
		ORDER BY
			SUM(SALES) DESC
	) AS SALES_RANK
FROM
	SUPERSTORE_RAW
GROUP BY
	CUSTOMER_ID,
	CUSTOMER_NAME;

-- the function dense rank can also when same value appears the dense rank differentiate



-- Assign row numbers to each order within a customer. (Window Function + PARTITION BY)  
SELECT
    CUSTOMER_ID,
	CUSTOMER_NAME,
    ORDER_ID,
    SALES,
    ROW_NUMBER() OVER
    (
        PARTITION BY CUSTOMER_ID
        ORDER BY SALES DESC
    ) AS ROW_NUM
FROM SUPERSTORE_RAW;

-- Display top 3 customers based on total sales. (Window Function)  


WITH customer_ranking AS
(
    SELECT
        CUSTOMER_ID,
        CUSTOMER_NAME,
        SUM(SALES) AS total_sales,
        RANK() OVER
        (
            ORDER BY SUM(SALES) DESC
        ) AS rank_number
    FROM SUPERSTORE_RAW
    GROUP BY CUSTOMER_ID, CUSTOMER_NAME
)

SELECT *
FROM customer_ranking
WHERE rank_number <= 3;





/*
   Step 3: Final Combined Query 

Write one final query that shows: 

Customer Name  

Total Sales  

Rank  

(Use JOIN + CTE + Window Function together) 

*/



WITH customer_sales AS
(
    SELECT
        customer_id,
        SUM(sales) AS total_sales
    FROM superstore_raw
    GROUP BY customer_id
),
customer_master AS
(
    SELECT DISTINCT
        customer_id,
        customer_name
    FROM superstore_raw
)

SELECT
    cm.customer_name,
    cs.total_sales,
    DENSE_RANK() OVER
    (
        ORDER BY cs.total_sales DESC
    ) AS customer_rank
FROM customer_sales cs
JOIN customer_master cm
    ON cs.customer_id = cm.customer_id
ORDER BY customer_rank;





/*



Mini Project: Customer Sales Insights 

Answer the following using SQL: 

Who are the top 5 customers?  

Who are the bottom 5 customers?  

Which customers made only one order?  

Which customers have above-average sales?  

What is the highest order value per customer? 



*/


-- Who are the top 5 customers?  
SELECT
	CUSTOMER_NAME,
	SUM(SALES) AS TOTAL_SALES
FROM
	SUPERSTORE_RAW
GROUP BY
	CUSTOMER_NAME
ORDER BY
	TOTAL_SALES DESC
LIMIT
	5;

/*

Top 5 customers are as follow : - 
Name 					sale amount 
Sean Miller 			25043.07
Tamara Chand 			19052.22
Raymond Buch 			15117.35
Tom Ashbrook     		14595.62
Adrian Barton    		14473.57
*/	


-- Bottom 5 Customers


SELECT
	CUSTOMER_NAME,
	SUM(SALES) AS TOTAL_SALES
FROM
	SUPERSTORE_RAW
GROUP BY
	CUSTOMER_NAME
ORDER BY
	TOTAL_SALES 
LIMIT
	5;




/*

bottom 5 customers are as follow : - 
Name 					sale amount
Thais Sissman			4.84
Lela Donovan			5.30
Carl Jackson			16.52
Mitch Gastineau			16.74
Roy Skaria				22.33
*/	


-- Which customers made only one order?  

SELECT
	CUSTOMER_NAME,
	COUNT(DISTINCT (ORDER_ID)) AS TOTAL_ORDERS
FROM
	SUPERSTORE_RAW
GROUP BY
	CUSTOMER_NAME
HAVING
	COUNT(DISTINCT (ORDER_ID)) = 1;



/*

customer_name
Anemone Ratner
Anthony O'Donnell
"Carl Jackson
Jenna Caffey
Jocasta Rupert
Lela Donovan
Mitch Gastineau
Patricia Hirasaki
Ricardo Emerson
Roland Murray
Susan MacKendrick
Theresa Coyne

*/

-- Above Average Sales Customers

WITH
	CUSTOMER_SALES AS (
		SELECT
			CUSTOMER_NAME,
			SUM(SALES) AS TOTAL_SALES
		FROM
			SUPERSTORE_RAW
		GROUP BY
			CUSTOMER_NAME
	)

SELECT
	*
FROM
	CUSTOMER_SALES
WHERE
	TOTAL_SALES > (
		SELECT
			AVG(TOTAL_SALES)
		FROM
			CUSTOMER_SALES
	);

/*
The above  query will give all the customers having sale greater than the average sales 
there are total 294 customres who have more than the average sales in the dataset given

*/


-- What is the highest order value per customer? 
SELECT
	CUSTOMER_NAME,
	MAX(SALES) AS HIGHEST_ORDER_VALUE
FROM
	SUPERSTORE_RAW
GROUP BY
	CUSTOMER_NAME
ORDER BY
	HIGHEST_ORDER_VALUE DESC;

/*
 The above qurey will the give the output and shows the 
 customer highest order value sales.

*/



























 
