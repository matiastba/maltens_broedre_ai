from turtledemo.chaos import plot

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_csv(filename):
    data_frame = pd.read_csv(filename, sep=';', encoding='unicode_escape', error_bad_lines=False)
    return data_frame


def avg_vs_estimate(data):
    estimate = data['Godt og vel'].tolist() # Godt og vel score
    avg = data['PrÃ¦cis'].tolist()          # Rigtigt gennemsnit

    estimate = [float(x) for x in estimate]
    avg = [float(x) for x in avg]

    plt.figure()
    plt.plot(estimate)
    plt.plot(avg)
    plt.legend(('Godt og vel', 'Gennemsnit'))
    plt.grid()
    plt.show()


def histograms(ratings, name):
    return plt.hist(ratings)


def plot_brother_avgs(data):
    brothers = data.columns.array[2:16]
    avg_brothers = [np.mean(data[brother]) for brother in brothers]

    plt.figure()
    y_pos = np.arange(len(brothers))
    indices = np.argsort(avg_brothers)
    plt.bar(y_pos, np.array(avg_brothers)[indices.astype(int)], align='center', alpha=0.5)
    plt.xticks(y_pos, np.array(brothers)[indices.astype(int)])
    plt.grid()
    plt.show()


def brother_distribution(data):
    brothers = data.columns.array[2:16]
    f, ax = plt.subplots(4, 4)
    plot_num_first = 0
    plot_num_second = 0

    for idx, brother in enumerate(brothers):
        plot_num_second = idx % 4

        ratings = data[brother]
        ax[plot_num_first, plot_num_second].hist(ratings)
        ax[plot_num_first, plot_num_second].set_xlim([0, 6.5])
        ax[plot_num_first, plot_num_second].legend((brother,))

        if plot_num_second == 3:
            plot_num_first += 1


if __name__ == '__main__':
    filepath = 'logens_karakterer_v2.csv'
    data = read_csv(filepath)
    brother_distribution(data)
    plot_brother_avgs(data)
    avg_vs_estimate(data)


