"""
The dataset we will be using contains information about movies on Netflix, which
you can find here.
https://drive.google.com/fileDo/d/1uCj7tPp1i60EFHJ85gnmLyc3BgmNbfHQ/view?usp=sharing

Questions we want to investigate:
Is a movie’s IMBd score positively correlated with its Hidden Gem score? Or do ratings for the same movies
diverge significantly between platforms?
Which languages do contents mainly originate from and how many movies originate from each
language?
How has the proportion of different view ratings (e.g. R-rated, PG-13, PG, etc.) changed through time?

"""

import matplotlib.pyplot as plt
import csv
import numpy as np


# Part 1: Hidden Gem vs IMDb score


def ratings(file_name):
    """
    Takes data file and returns the hidden gem and imdb scores of each movie

    :param file_name: (str) name of csv file
    :return: (tuple) a tuple of two dictionaries: the first is the Hidden Gem score per movie, the second the IMDb score
    """
    with open(file_name, newline='') as csvfile:
        file_reader = csv.reader(csvfile, delimiter=',', quotechar="\"")
        next(file_reader)  # skips header

        hid_gem = {}
        imdb = {}

        rows = list(file_reader)  # creates list of rows of file where each row is a list of its entries

        # loops through each movie
        for row in rows:

            # skips rows with missing data, finds hidden gem (5th column) and imdb score (12th column) for each movie
            if row[5] != "" and row[12] != "":
                hid_gem[row[0]] = float(row[5])
                imdb[row[0]] = float(row[12])

        return hid_gem, imdb


def correlation(tup):
    """
    Calculates the Pearson correlation coefficient between hidden gem and imdb scores

    :param tup: (tuple) a tuple containing two dictionaries (hidden gem and imdb scores)
    :return: (int) Pearson correlation value between the values of the two dictionaries
    """
    dict1, dict2 = tup  # unpack tuple
    lst1 = []
    lst2 = []

    # creates list with values from first dictionary (hidden gem)
    for value in dict1.values():
        lst1.append(value)

    # creates list with values from second dictionary (hidden gem)
    for value in dict2.values():
        lst2.append(value)

    # calculates correlation coefficient with numpy
    x = np.array(lst1)
    y = np.array(lst2)
    r = np.corrcoef(x, y)

    return r[0, 1]


def plot_ratings(tup):
    """
    Plots scatterplot comparing imdb vs hidden gem scores

    :param tup: (tuple) the tuple of two dictionaries returned by the ratings function
    :return None: (None Type)
    """
    dict1, dict2 = tup  # unpack tuple

    x = []
    y = []

    # loops through first dictionary keys (movies)
    for key in dict1.keys():

        # finds same key (movie) in second dictionary and appends value
        if key in dict2.keys():
            x.append(dict1[key])
            y.append(dict2[key])

    # plot scatterplot
    plt.plot(x, y, "mx")

    plt.xlabel("Hidden Gem score")
    plt.ylabel("IMDb score")
    plt.title("Comparison between Hidden Gem and IMDb scores")

    plt.show()


# Part 2: Languages of production

def lang_collector(file_name):
    """
    Takes data file and counts the number of movies produced in each language

    :param file_name: (str) name of csv file
    :return: (dict) a dictionary representing the number of movies produced in each language (15 most common)
    """
    with open(file_name, newline='') as csvfile:
        lang_reader = csv.reader(csvfile, delimiter=',', quotechar="\"")
        next(lang_reader)  # skips header

        lang_occ = {}
        counter = 0

        # loops through row in file
        for row in lang_reader:

            # checks if row is not an empty list
            if row:
                row_list = row[3].split(",")  # splits the "Languages" entry into a list of each individual language

                # loops through each language
                for lang in row_list:
                    lang = lang.strip()  # strips away whitespaces

                    # checks for missing data
                    if lang != "":

                        # checks each language appears once as a key
                        if lang not in lang_occ.keys():

                            # counts the number of movies made in each language for the 15 most common languages
                            if counter <= 15:
                                lang_occ[lang] = 1
                                counter += 1
                        else:
                            lang_occ[lang] += 1

        sorted_data = sorted(lang_occ.items(), key=lambda item: item[1],
                             reverse=True)  # sorts (key, value) tuples in decreasing order

        sorted_dict = {}

        # puts sorted tuples as keys and values into new sorted dictionary
        for lang, occ in sorted_data:
            sorted_dict[lang] = occ

        return sorted_dict


def lang_perc(file_name, dct):
    """
    Calculates the percentage of movies produced in each language among total content

    :param file_name: (str) name of csv file
    :param dct: (dct) dictionary returned by the lang_collector function
    :return: (list) list of percentages corresponding to each language
    """
    with open(file_name, newline='') as csvfile:
        lang_reader = csv.reader(csvfile, delimiter=',', quotechar="\"")
        next(lang_reader)  # skips header

        rows = list(lang_reader)  # creates list of rows where each row is a list of its entries

        percent = []

        # loops through the values of dct
        for num in dct.values():
            perc = num / len(rows) * 100  # calculates percentage of movies of this language out of total movies
            perc = round(perc, 2)  # rounds to 2 decimals after point
            percent.append(perc)

        return percent


def plot_lang(data):
    """
    Plots bar graph of the number of movies produced per language for the top 15 languages

    :param data: (dict) dictionary returned by lang_collector function
    :return None: (None Type)
    """
    x = data.keys()  # languages on x-axis
    y = data.values()  # number of movies on y-axis

    bar_width = .5
    plt.xticks(fontsize=10)
    plt.bar(x, y, bar_width)

    # get percentage taken by the number of movies in each language
    percent_list = lang_perc("netflix-data-vf.csv", lang_collector("netflix-data-vf.csv"))

    # creates list with position of each percentage annotation
    annotate_cord_list = [("English", 8.14e+03), ("Japanese", 1797), ("Spanish", 1291), ("French", 1.17e+03),
                          ("German", 7.8e+02), ("Hindi", 6.2e+02), ("Mandarin", 5.9e+02), ("Italian", 561),
                          ("Cantonese", 3.7e+02), ("Thai", 2.8e+02), ("Polish", 2.3e+02), ("Swedish", 2.4e+02),
                          ("Turkish", 2.3e+02), ("Norwegian", 1.3e+02), ("Sanskrit", 36), ("Scanian", 12)]

    # annotates each percentage on top of language bar
    for i in range(len(annotate_cord_list)):
        label, y_val = annotate_cord_list[i]
        plt.annotate('{}%'.format(round(percent_list[i], 2)), xy=(i, y_val), xytext=(i, y_val + 50), ha='center',
                     fontsize=8)

    plt.xlabel("Language of production", fontsize=16)
    plt.ylabel("Number of movies", fontsize=16)
    plt.title("Number of movies produced in each language (15 most common)", fontsize=20)

    plt.show()


# Part 3: Distribution of viewing rates in time

def view_rate(file_name):
    """
    Takes data file and creates a nested dictionary representing the number of movies in each year of each view rating

    :param file_name: (str) name of our csv file
    :return: (dict) nested dictionary with view ratings as keys and inner dictionaries as values; inner dictionaries
    have years as keys and the number of movies with that rating in that year as values
    """
    with open(file_name, newline='') as csvfile:
        file_reader = csv.reader(csvfile, delimiter=',', quotechar="\"")
        next(file_reader)

        # creates list of years as x-axis
        years = ["2015", "2016", "2017", "2018", "2019", "2020", "2021"]

        view_ratings = []
        rows = list(file_reader)  # creates list of rows where each row is a list of its entries

        # loops through every row to get view rating (11th column)
        for row in rows:
            rating = row[11]

            # appends every unique view rating to a list
            if rating not in view_ratings and rating != "":
                view_ratings.append(rating)

        # nested dictionary to hold rating counts per year for each rating
        rate_dict = {}

        # loop through each view rating to create dictionary keys
        for rating in view_ratings:
            rate_dict[rating] = {}

            # loops through each year so that each value of the outer dictionary is a dictionary with year as keys
            for year in years:
                rate_dict[rating][year] = 0  # initializes values

        # loops through each row to collect number of movies per year in each view rating
        for row in rows:

            date = row[19]
            year = date[:4]  # gets year by slicing first 4 characters in column "Netflix Release Date"
            rating = row[11]  # gets view rating

            # accumulates number of movies with that rating and released that year to get values of inner dictionary
            if rating in rate_dict.keys() and year in rate_dict[rating].keys():
                rate_dict[rating][year] += 1

        # creates dict containing a list of the values of rate_dict for each rating to fit stacked bar graph format
        rate_counts = {}

        # loops through each view rating for dictionary keys
        for rating in view_ratings:
            rate_list = []

            # loops through each year to retrieve value from rate_dict
            for year in years:
                rate_list.append(rate_dict[rating][year])
            rate_counts[rating] = rate_list

        return rate_counts


def view_plot(data):
    """
    Plots stacked bar graph of view ratings distribution from 2015 to 2021

    :param data: (dict) nested dictionary returned by view_rate
    :return None: (None Type)
    """
    years = ["2015", "2016", "2017", "2018", "2019", "2020", "2021"]

    # plots stacked bar graph using numpy documentation
    width = 0.4

    fig, ax = plt.subplots()
    bottom = np.zeros(len(years))

    for rating in data:
        data[rating] = np.array(data[rating])  # puts in plottable numpy format

    # segments each year's bar into numbers per view rating
    for rating, rate_counts in data.items():
        p = ax.bar(years, rate_counts, width, label=rating, bottom=bottom)
        bottom += rate_counts

    ax.set_title("Distribution of movies view ratings per year")
    ax.legend(loc="upper right")

    plt.xlabel("Netflix release year")
    plt.ylabel("Number of movies")

    plt.show()


def main():
    """
    Generates 3 graphs from our Netflix Movies csv file using the functions above to answer our questions.
    """
    # Part 1: hidden gem vs imdb: plotting and correlation calculation
    tup_rate = ratings("netflix-data-vf.csv")
    plot_ratings(tup_rate)
    print("Pearson's correlation coefficient between Hidden Gem and IMDb: ", correlation(tup_rate))

    # Part 2: languages plotting
    plot_lang(lang_collector("netflix-data-vf.csv"))

    # Part 3: view ratings in time plotting
    view_plot(view_rate("netflix-data-vf.csv"))


if __name__ == '__main__':
    main()
