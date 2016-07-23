## Simple Linear Regression
import random

import matplotlib.pyplot as plt
import numpy as np
import sklearn
import csv

def generate_random():
    x = []
    for i in xrange(0, 20):
        x.append(random.random())
    y = []
    for v in x:
        y.append(v + random.random() / 2)
    return np.array(x), np.array(y)

# def generate_random():
#     x, y = make_regression(n_samples=100, n_features=1, n_informative=1,
#                            random_state=0, noise=35)
#     return x, y


# def get_interest_rate_home_price():
#     interest_rates = [10.30,
#                       10.30,
#                       10.10,
#                       9.30,
#                       8.40,
#                       7.30,
#                       8.40,
#                       7.90,
#                       7.60,
#                       7.60,
#                       6.90,
#                       7.40,
#                       8.10,
#                       7.00,
#                       6.50,
#                       5.80]
#
#     median_home_price = [183800,
#                          183200,
#                          174900,
#                          173500,
#                          172900,
#                          173200,
#                          173200,
#                          169700,
#                          174500,
#                          177900,
#                          188100,
#                          203200,
#                          230200,
#                          258200,
#                          309800,
#                          329800]
#
#     return np.array(interest_rates), np.array(median_home_price)

# def get_age_health_data():
#     x = []
#     y = []
#     with open('AgeHealth.csv') as csvfile:
#         reader = csv.reader(csvfile, delimiter=',')
#         for row in reader:
#             if 'age' in row:
#                 continue
#             else:
#                 x.append(int(row[0]))
#                 y.append(int(row[1]))
#     return np.array(x), np.array(y)

def create_scatter_plot(x, y, slope, intercept):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # ax.set_title('Mortgage interest rates and home prices')
    # ax.set_xlabel('interest rate(%)')
    # ax.set_ylabel('median home price($)')
    ax.plot(x, y, '.')
    ax.plot(x, slope * x + intercept, '-')
    plt.interactive(True)
    plt.show(block=True)
    print "Completed"

def get_mean(values):
    return np.mean(values, axis=0)

def get_standard_deviation(values):
    return np.std(values, axis=0)

def get_correlation(x, y):
    return np.corrcoef(x, y)[0][1]

def linear_regression(x, y):
    mean_x = get_mean(x)
    mean_y = get_mean(y)
    dev_x = get_standard_deviation(x)
    dev_y = get_standard_deviation(y)
    corr = get_correlation(x, y)

    slope = corr * (dev_y / dev_x)
    intercept = mean_y - (slope * mean_x)

    return slope, intercept

def main():
    try:
        x, y = generate_random()
        # x, y = get_interest_rate_home_price()
        # x, y = get_age_health_data()
        # plotting the line
        slope, intercept = linear_regression(x, y)
        create_scatter_plot(x, y, slope, intercept)
    except Exception as e:
        print e

if __name__ == "__main__":
    main()
