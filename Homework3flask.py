# FE 595: Python for Finance
# Homework 3
# Abraham Jimenez-Berlanga
# CWID 10444147


# Required Libraries (Request to use GET REST API and RE)
from requests import get
# I tried to install RE2, but it needed VB and my company laptop was restringing some DLLs
import re as re
# Import flask
from flask import Flask

# definition of the REST API
app = Flask(__name__)


@app.route('/homework3', methods=['GET'])
# Function to access 'https://theyfightcrime.org' and extract the characters for Male and Female
# the function has an input variable to define how many characters are going to be retrieved

def get_fight():
    # Define two list, one for Male and another for Female. they will contain the jobs one
    # the html is cleaned
    male_list = []
    female_list = []
    # loop to retrieve as many characters as requested
    for i in range(50):
        get_request = get('https://theyfightcrime.org/')
        # move the html to page variable
        page = get_request.text
        # using RE we extract the portion in which the role is stored
        # the pattern for the extract is based on the one showed in the class on 2/21
        maleandfemale = re.search('<P>(.+) They fight crime!</P>', page)
        sentence = maleandfemale.group(0)
        # first we extract the male character. As the point is sometime missing, the left limite of the
        # extract is defined by the She's -as suggested in class-
        male_search = re.search("He's (.+) She's", sentence)
        male = male_search.group(0)
        # When storing in the list, we remove the last 6 positions " She's"
        male_list.append(male[0:len(male) - 6])
        # As mentioned before, sometimes the . is lost, so the limit is defined by " They"
        female_search = re.search("She's (.+) They", sentence)
        female = female_search.group(0)
        # As did with the male, we remove the 5 last positions " They"
        female_list.append(female[0:len(female) - 5])

    with open('male.csv', 'w') as csvFile:
        csvFile.write("\n".join(male_list))
    with open('female.csv', 'w') as csvFile:
        csvFile.write("\n".join(female_list))

    return female_list, male_list


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
