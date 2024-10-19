from finalproject import *
import numpy as np


def correlation_tester():
    """
    Run a series of tests for correlation
    :return (boolean): were all tests successful
    """
    # general correlation test
    x = {1: 10, 2: 11, 3: 12, 4: 13, 5: 14, 6: 15, 7: 16, 8: 17, 9: 18, 10: 19}
    y = {1: 2, 2: 1, 3: 4, 4: 5, 5: 8, 6: 12, 7: 18, 8: 25, 9: 96, 10: 48}
    tup = x, y
    assert correlation(tup) == 0.7586402890911867

    a = {1: 1, 2: 3, 3: 4, 4: 5, 5: 5, 6: 6, 7: 7, 8: 10, 9: 11, 10: 12, 11: 15, 12: 20, 13: 25, 14: 28, 15: 30, 16: 35}

    b = {1: 20000, 2: 30000, 3: 40000, 4: 45000, 5: 55000, 6: 60000, 7: 80000, 8: 100000, 9: 130000, 10: 150000, 11: 200000, 12: 230000, 13: 250000, 14: 300000,
         15: 350000, 16: 400000}
    tup2 = a, b
    assert correlation(tup2) == 0.9929845761480398

    # perfect correlation test
    c = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}
    d = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}
    tup3 = c, d
    assert correlation(tup3) > 0.99

    return True


def ratings_tester():
    """
    Run a series of tests for ratings
    :return (boolean): were all tests successful
    """
    assert ratings("test.csv") == (
    {'Lets Fight Ghost': 4.3, 'HOW TO BUILD A GIRL': 7.0, 'Centigrade': 6.4, 'ANNE+': 7.7, 'Moxie': 8.1,
     'The Con-Heartist': 8.6, 'Gleboka woda': 8.7, 'Instynkt': 6.9, 'Only a Mother': 8.3},
    {'Lets Fight Ghost': 7.9, 'HOW TO BUILD A GIRL': 5.8, 'Centigrade': 4.3, 'ANNE+': 6.5, 'Moxie': 6.3,
     'The Con-Heartist': 7.4, 'Gleboka woda': 7.5, 'Instynkt': 3.9, 'Only a Mother': 6.7})
    assert type(ratings("test.csv")) == tuple

    return True


def lang_collector_tester():
    """
    Run a series of tests for lang_collector
    :return (boolean): were all tests successful
    """
    assert lang_collector("test.csv") == (
    {'English': 3, 'Swedish': 2, 'Polish': 2, 'Spanish': 1, 'Turkish': 1, 'Thai': 1})
    assert type(lang_collector("test.csv")) == dict

    return True


def lang_perc_tester():
    """
    Run a series of tests for lang_perc
    :return (boolean): were all tests successful
    """
    assert lang_perc("test.csv", lang_collector("test.csv")) == [33.33, 22.22, 22.22, 11.11, 11.11, 11.11]
    assert type(lang_perc("test.csv", lang_collector("test.csv"))) == list

    return True


def view_rate_tester():
    """
    Run a series of tests for view_rate
    :return (boolean): were all tests successful
    """
    assert view_rate("netflix-data-vf.csv") == {'R': [873, 215, 210, 199, 223, 323, 53],
                                                'Unrated': [33, 16, 9, 9, 15, 29, 6],
                                                'PG-13': [693, 139, 123, 126, 122, 145, 25],
                                                'PG': [299, 57, 55, 62, 55, 112, 17],
                                                'TV-14': [159, 83, 98, 142, 131, 151, 34],
                                                'TV-MA': [128, 92, 152, 249, 216, 269, 30],
                                                'TV-Y7': [39, 17, 19, 18, 18, 15, 4],
                                                'Not Rated': [310, 145, 166, 215, 201, 228, 55],
                                                'Approved': [5, 0, 0, 0, 4, 7, 6], 'G': [53, 18, 4, 10, 11, 29, 1],
                                                'TV-G': [26, 9, 11, 9, 16, 51, 3], 'Passed': [1, 1, 2, 1, 0, 10, 2],
                                                'TV-Y': [61, 13, 16, 13, 19, 21, 3],
                                                'TV-PG': [79, 34, 37, 55, 57, 67, 2], 'GP': [0, 0, 1, 0, 0, 2, 1],
                                                'MA-17': [0, 0, 0, 0, 0, 1, 0], 'TV-Y7-FV': [9, 0, 4, 6, 6, 8, 0],
                                                'UNRATED': [0, 0, 0, 0, 0, 1, 0], 'M/PG': [0, 0, 0, 0, 0, 1, 0],
                                                'X': [0, 0, 0, 1, 1, 2, 0], 'U': [0, 0, 0, 0, 0, 1, 0],
                                                'M': [0, 0, 0, 0, 1, 0, 0], 'E10+': [1, 0, 0, 1, 0, 0, 0],
                                                'AL': [0, 0, 0, 0, 1, 0, 0], 'NC-17': [6, 0, 3, 0, 0, 0, 0],
                                                'TV-13': [0, 0, 1, 0, 0, 0, 0], 'NOT RATED': [1, 0, 1, 0, 0, 0, 0],
                                                'E': [1, 0, 0, 0, 0, 0, 0]}
    assert type(view_rate("test.csv")) == dict

    return True


def main():
    """
    For testing purpose
    """
    # Part 1 Testing
    print("testing correlation ... ")
    print("PASS" if correlation_tester() else "FAIL")

    print("")
    print("testing ratings ... ")
    print("PASS" if ratings_tester() else "FAIL")

    print("")
    print("testing lang_collector ... ")
    print("PASS" if lang_collector_tester() else "FAIL")

    print("")
    print("testing lang_perc ... ")
    print("PASS" if lang_perc_tester() else "FAIL")

    print("")
    print("testing view_rate ... ")
    print("PASS" if view_rate_tester() else "FAIL")


if __name__ == "__main__":
    main()
