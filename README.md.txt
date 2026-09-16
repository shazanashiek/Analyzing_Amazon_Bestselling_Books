# Analyzing Best Selling Amazon Books

A data analysis project exploring Amazon's bestselling books dataset using Python and pandas.

## What This Project Does

This project cleans and analyzes a dataset of Amazon bestsellers to answer two main questions:

- Which genres have the highest average reader ratings?
- Which authors appear most frequently on the bestsellers list?

## Tools Used

- **pandas** — data cleaning and analysis
- **matplotlib** — data visualization

## Process

1. **Data Cleaning**
   - Removed duplicate entries
   - Renamed columns for clarity (e.g. "Name" to "Title")
   - Converted the Price column to the correct data type

2. **Analysis**
   - Calculated average rating grouped by genre
   - Counted the number of bestseller appearances per author

3. **Visualization**
   - Bar chart showing average rating by genre
   - Horizontal bar chart showing the top 10 most frequent bestselling authors

## Files

- `Analyze_Top_Selling_Amazon_Books_with_Pandas.py` — main analysis script
- `bestsellers.csv` — source dataset
- `avg_rating_by_genre.png` — chart of average rating by genre
- `top10_authors_barh.png` — chart of top 10 authors by bestseller count
- `avg_rate_by_genre.csv` — exported ratings data
- `top10_authors.csv` — exported top authors data

## How to Run

1. Make sure you have pandas and matplotlib installed:
   ```
   pip install pandas matplotlib
   ```
2. Run the script:
   ```
   python "Analyze_Top_Selling_Amazon_Books_with_Pandas.py"