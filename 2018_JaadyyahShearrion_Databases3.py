import pymysql
import random

# Put the correct host IP here.  You will change 172.25.233.107 to whatever the IP is of your partner.
connection = pymysql.connect(host='172.25.233.125', port=3306, user='root', passwd='CRLSisthebest123$', db='world',
                             autocommit=True)

# cursor.execute(sql) runs whatever the variable sql is set to.  Don't delete these 3 lines.
cursor = connection.cursor()
sql = 'ALTER TABLE world.country MODIFY COLUMN Continent varchar(35);'
cursor.execute(sql)

# Zurg's first directive - change things ending in "stan" to end in "zurg".

sql = "SELECT * FROM country WHERE Name LIKE '%stan'" # Fill this in.  Inside the quotation marks, write a query to get all countries ending in "stan"
cursor.execute(sql)  # this runs your query
results = cursor.fetchall()  # This puts your query results into a list.
for row in results:
    original_country = row[1]
    if original_country[-4:] == 'stan':
        zurg_country = original_country[:-4] + 'zurg'
        sql = "UPDATE country set Name = \' " + zurg_country + "\'WHERE Name LIKE\'" + original_country + "\'"
        cursor.execute(sql)
        print(sql)

# Zurg's second directive - get rid of French and replace it with a random language from a list of languages
zurg_languages = ['Zurg', 'English', 'Dothraki', 'Simlish']  # make your list of Zurg's languages HERE! Need 3 more
sql = "SELECT * FROM countrylanguage WHERE language LIKE '%french'"
cursor.execute(sql)  # Runs whatever you put in quotations
print(sql)
results = cursor.fetchall()
print(results)
for row in results:
    original_language = row[1]
    if original_language == 'french' or 'creole french' or 'comorian-french' or 'arabic-french':
        sql = "UPDATE countrylanguage SET language = \' " + zurg_languages[random.randint(0, len(zurg_languages) - 1)] + "\'" + "WHERE language = \'" + original_language + "\'"
        print(sql, end='\n')
        cursor.execute(sql)

# Zurg's third directive - rename the continents from his dictionary of new names.
zurg_dictionary = {'Asia': 'Buzz_sux',
                   'Europe': 'Reach_for_the_sky',
                   'North America': 'Zurg_land',
                   'Africa': 'Zurg_world',
                   'Oceania': 'Hobbitsyum', 'Antarctica': 'too_cold',
                   'South America': 'Zurgs_vacation_home'}

# Your code goes here.  Not going to tell you how to do it.
for continent in zurg_dictionary:
    sql = "UPDATE country set continent = \'" + zurg_dictionary[continent] + " \'WHERE continent = \'" + continent + "\'"
    cursor.execute(sql)
    print(sql)

cursor.close()
connection.close()