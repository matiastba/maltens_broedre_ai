import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def read_csv(filename):
    data_frame = pd.read_csv(filename, sep=';', encoding='unicode_escape', error_bad_lines=False)
    return data_frame


def godt_mod_virkelighed(data):
    godt_og_vel = data['Godt og vel'].tolist()
    exact = data['PrÃ¦cis'].tolist()

    godt_og_vel = [float(x) for x in godt_og_vel]
    exact = [float(x) for x in exact]

    plt.figure()
    plt.plot(godt_og_vel)
    plt.plot(exact)
    plt.legend(('Godt og vel', 'Præcis'))
    plt.grid()
    plt.show()


def histograms(ratings, name):
    return plt.hist(ratings)


def broder_fordeling(data):
    broedre = data.columns.array[2:16]
    print(len(broedre))
    f, ax = plt.subplots(4, 4)
    plot_num_first = 0
    plot_num_second = 0
    for idx, bror in enumerate(broedre):
        plot_num_second = idx % 4

        ratings = data[bror]
        ax[plot_num_first, plot_num_second].hist(ratings)
        ax[plot_num_first, plot_num_second].set_xlim([0, 6.5])
        ax[plot_num_first, plot_num_second].legend((bror,))

        if plot_num_second == 3:
            plot_num_first += 1


if __name__ == '__main__':
    filepath = 'logens_karakterer_v2.csv'
    data = read_csv(filepath)
    broder_fordeling(data)
    godt_mod_virkelighed(data)


