import pandas as pd
import matplotlib.pyplot as pl
df= pd.read_csv('bestsellers.csv')
#explore the dataset
print(df.head())
print(df.shape)
print(df.columns)
print(df.describe())

#cleaning data:
    #1) removing duplicates
df.drop_duplicates(inplace=True)
    #2) renaming columns for clearer understanding
df.rename(columns={"Name":"Title",
          "Year":"Publication Year",
          "User Rating":"Rating"}, inplace=True)
    #3) changing column datatype to a more suitable one
df["Price"]=df["Price"].astype(float)

#performing data analysis:
    #1)finding the average rating of books grouped by genre
avg_rate_by_genre= df.groupby("Genre")["Rating"].mean()
print(avg_rate_by_genre)
        #plotting average rating by genre
avg_rate_by_genre.plot(kind='bar', color="green")
pl.title("Average Rating by Genre")
pl.xlabel("Genre")
pl.ylabel("Average Rating")
pl.xticks(rotation=45)
pl.tight_layout()
pl.savefig("avg_rating_by_genre.png")
pl.show()


    #2)finding which authors have the most books on best sellers list.
author_counts=df['Author'].value_counts()
print(author_counts)
        #plotting most popular authors
top_authors=author_counts.head(10)
pl.figure(figsize=(10,6))
pl.barh(top_authors.index, top_authors.values, color="skyblue")
pl.title("Top 10 Authors by Number of Bestsellers in Amazon")
pl.xlabel("Number of Bestsellers")
pl.ylabel("Author")
pl.gca().invert_yaxis()
pl.tight_layout()
pl.savefig("top10_authors_barh.png")
pl.show()

#Exporting analysis findings
avg_rate_by_genre.to_csv("avg_rate_by_genre.csv")
author_counts.head(10).to_csv("top10_authors.csv")
