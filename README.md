# BuyRentKenya Rent Data End-to-End Data Pipeline
### Description
This GitHub project demonstrates the process of scraping rent data from the website, [BuyRentKenya](https://www.buyrentkenya.com/property-for-rent), transforming it using AWS Lambda, storing it in S3 buckets, inferring the data schema using AWS Glue Crawler, creating a data catalog with AWS Glue Data Catalog, querying the data with Athena, and finally visualizing the results in Power BI. The project is designed to showcase a complete end-to-end data pipeline for analysis.

### Schema Diagram
![Schema](https://github.com/MuthoniGathu/rent-end-to-end-data-pipeline/assets/32902183/dcadd2b7-04c6-4a5e-ba0f-4b668cafb8db)

### Project Steps
1. ### Data Scraping
The Python script in BuyRentKenya Scape Function scrapes rent data from the [BuyRentKenya](https://www.buyrentkenya.com/property-for-rent) website using web scraping techniques. The scraped data is then saved as CSV.

2. ### Data Storage
The scraped data is uploaded to an S3 bucket in AWS. The bucket serves as the storage location for the raw data.

3. ### Data Transformation
The Property Transformation Function is an AWS Lambda function that processes the raw data. It applies necessary transformations and the transformed data is saved to another S3 bucket.

4. ### Schema Inference
AWS Glue Crawler is used to automatically infer the data schema from the transformed data stored in the S3 bucket. The inferred schema is used to create the data catalog.

5. ### Data Catalog
The AWS Glue Data Catalog stores the inferred data schema and metadata. It provides a centralized repository for managing and accessing the structured data.

6. ### Data Querying
AWS Athena is utilized to query the data stored in the AWS Glue Data Catalog. With Athena's SQL-based querying capability, you can easily analyze and explore the data.

7. ### Data Visualization
 To provide a comprehensive view of the rental property listed on the website, I created an interactive Power BI dashboard based on the analyzed data. The dashboard allows users to explore and gain deeper insights into key aspects of the rental market.
 
![Property Viz](https://github.com/MuthoniGathu/rent-end-to-end-data-pipeline/assets/32902183/6fe3a1b4-a2b8-473a-82e8-fe2ba673c82f)

**Key Insights:**

* **_Average Rent Price:_** The average rent price for properties listed in the website is approximately 222,000 Kenyan Shillings (KES).
* **_Average Bedrooms and Bathrooms:_** On average, rental properties listed in the website feature 3 bedrooms and 3 bathrooms, giving an overview of typical property sizes.
* **_Positive Correlation:_** Our analysis reveals a positive correlation between the number of bedrooms, bathrooms, and rent prices. As property size increases, rent prices also tend to rise.
* **_Affordability Perspective:_** It is important to note that while the dataset shows higher rent prices and property sizes, this might not represent the reality for the majority of Kenyans. A significant portion of the population lives on about 100 KES per day, highlighting an affordability gap.

**Implications:**
* The platform may be catering primarily to an affluent segment, limiting appeal to a broader audience.
* The dataset may be skewed towards higher-end neighborhoods, potentially overlooking affordable housing segments.

**Recommendations for BuyRentKenya:**
* **_Diversify Property Listings:_** To be more inclusive, consider featuring a diverse range of property listings, including more affordable housing options from different locations.
* **_Geographical Spread:_** Ensure property listings cover a wide range of locations, catering to diverse housing needs.


