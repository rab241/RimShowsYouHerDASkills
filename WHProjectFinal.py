
import pandas as pd
import numpy as np
df = pd.read_csv("./Downloads/world-happiness-report-2021.csv")
#easier naming convension
df.rename(columns = lambda x: x.strip().lower().replace(" ", "_"), inplace=True)

df.head()
df.describe()
#since all columns have same number of rows, no need to deal with missing rows/uneven columns


#In the data, the countries within each region have average ladder scores measuring each country's happiness
#It would be easy to rank by ladder score and decide to go to happiest country; however, the ladder score is made up of several factors.
#As a single traveller and woman, I take being free and having social support as an essential. Generally leads to safety in being able to depend on others and do as I please.

#With my southern hospitality, I love the generosity and welcoming feel of people within a new country.
#Social support, generosity, and freedom to make life choices factors are weighted into the ladder score. 
#I want to see countries who prioritize such factors
df2 = df[(df["social_support"]>=0.80) & (df["freedom_to_make_life_choices"]) & (df["generosity"]>=0.15) ]
df2
#since 9 countries in 4 seperate regions come out with initial priorities, I want to know the best country to go to within each region. 


#The best is the higher ladder score and smallest std dev of ladder score, if the larger ladder score has a larger std dev, then actually pick the one with next largest
df2.groupby(["regional_indicator" ,"country_name"]).agg(min_stldsc = pd.NamedAgg(column = "standard_error_of_ladder_score", aggfunc = 'min'), max_ladsc = pd.NamedAgg(column = "ladder_score", aggfunc = 'max'))
#Specific country for each region: Kosovo for Central and Eastern Europe, Turkmenistan for CIS, Australia for North America and ANZ, Indonesia for Southeast Asia, and Iceland for Western Europe


#To gain more insight into the extra attributes, use box and whisker plots, and horizontal bar plots
import matplotlib.pyplot as plt
#I like the number of choices in a region that I might decide to go to one and have a road trip
df_country_region = df2.groupby("regional_indicator").country_name.count()
df_country_region.plot(kind='bar',figsize=(10,10))
plt.title("Number of Countries within regions")
plt.xlabel("Regions")
plt.ylabel("Number of Countries")
#Because Western Europe has the most regions I can explore, I would go to Western Europe

    
# To be sure, I want to check if Western Europe's ladder score is top three mean score
region_ladder_mean = df2.groupby("regional_indicator").ladder_score.mean()
region_ladder_mean
region_ladder_mean.plot(kind="bar",figsize=(10,10))
plt.title("Average Happiness Score per Region")
plt.xlabel("Regions")
plt.ylabel("Mean Happiness Score")

#Western Europe is not only the top three but also number one! 
#Officially, I will travel to Western Europe and start in Iceland 


    




