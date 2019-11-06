
import matplotlib
import quandl

quandl.ApiConfig.api_key = '-5fhUZzPrkRw8nvzrCqE'

# This prints out the . BLSE/CEU9000000010 dataset, the second column (.1).
# If you want the second column, then do this BLSE/CEU9000000010.2
# If you want the stock price of Amazon, 2nd column, do this WIKI/AMZ
# Change the dates as necessary.
# Don't change the auth token
data = quandl.get(['CITYPOP/CITY_CAMBRIDGEMAUSA', 'CITYPOP/CITY_BOSTONMAUSA'], authtoken='-5fhUZzPrkRw8nvzrCqE',
                               trim_start="1990-04-01", trim_end="2016-07-01")


# Name your columns something useful here.  These will be in the legend.
data.columns = ["Population of Cambridge (Thousands)", "Population of Boston (Thousands)"]

# Here are some debugging things.  You should comment or delete when done
print(data)  # prints all of the data
print(type(data))  # Shows that it's a  Pandas dataframe

# This plots the data (but won't actually show until you do a matplotlib.pyplot.show)
data.plot.line()


# The y label and title.  You should edit these.
matplotlib.pyplot.ylabel("Population (thousands)")
matplotlib.pyplot.title('Population Comparison')

# Set the y axis limits
matplotlib.pyplot.ylim((50000, 700000))


# How to write text and draw arrows https://matplotlib.org/users/annotations_guide.html#plotting-guide-annotation

# This puts plain text with no arrows.  xy is where the text is.
# An annotation is part of the assignment.  It should give a story of what is going on in the graph
matplotlib.pyplot.annotate("interesting expansion of two major cites", xy=('2000-04-01', 300000))

# Prints out the plot
matplotlib.pyplot.show()