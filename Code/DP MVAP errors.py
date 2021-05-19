import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score
from matplotlib.ticker import PercentFormatter
import os
import matplotlib.patches as mpatches



path = r'/Users/ari/Documents/PGP/Differential Privacy/Global Analysis/epsilon = 12.2/colors/Will edits'
os.chdir(path)
data = pd.read_excel(r'/Users/ari/Documents/PGP/Differential Privacy/Epsilon12.2ALL.xlsx')


def make_histogram(census_col, dp_col, total_col, race_eth):
    levels = range(1, 16)
    fig, ax = plt.subplots()
    plt.rcParams.update({'font.size': 16})
    ax.yaxis.set_major_formatter(PercentFormatter())
    #plt.ylim([-limit - st_dev, limit + st_dev])
    plt.ylim([-1.05, 1.05])
    for i in levels:
        df = data[data["Example"] == i]
        x = df[census_col]
        y = df[dp_col]
        res = y - x
        res_perc = res / df[total_col] * 100
        if (i <= 2):
            plt.plot(x, res_perc, 'ro', alpha = 0.5)
        elif (i == 5 or i == 11 or i == 15):
            plt.plot(x, res_perc, 'bo', alpha = 0.5) 
        elif (i == 3 or i == 7 or i == 8 or i == 10 or i == 14):
            plt.plot(x, res_perc, 'go', alpha = 0.5)
        else:
            plt.plot(x, res_perc, 'ko', alpha = 0.5)

    plt.xlabel("{} in 2010 Census".format(race_eth))
    #plt.ylabel("Census Bureau's Relative distance measure".format(race_eth))
    #plt.title("{} deviations".format(race_eth))
    plt.savefig("% residual colors {}.png".format(race_eth), bbox_inches='tight')
    plt.show()

make_histogram("NHbla_alo", "NHbla_aloDP", "tot", "NH Black total pop")
make_histogram("NHnat_alo", "NHnat_aloDP", "tot", "NH American Indian total pop")
make_histogram("NHpci_alo", "NHpci_aloDP", "tot", "NH Hawaiian Pac Islander total pop")
make_histogram("NHasi_alo", "NHasi_aloDP", "tot", "NH Asian total pop")
make_histogram("NHsor_alo", "NHsor_aloDP", "tot", "NH Some Other Race total pop")
make_histogram("NH2mo", "NH2moDP", "tot", "NH 2 or more races total pop")

make_histogram("NHbla_alo_VAP", "NHBVAP_aloDP", "totVAP", "NH Black VAP")
make_histogram("NHnat_alo_VAP", "NHnatVAP_aloDP", "totVAP", "NH American Indian VAP")
make_histogram("NHasi_alo_VAP", "NHAVAP_aloDP", "totVAP", "NH Asian VAP")
make_histogram("NHpci_alo_VAP", "NHpciVAP_aloDP", "totVAP", "NH Hawaiin Pac Islander VAP")
make_histogram("NHsor_alo_VAP", "NHsorVAP_aloDP", "totVAP", "NH Some Other Race VAP")
make_histogram("NH2mo_VAP", "NH2moVAPDP", "totVAP", "NH 2 or more races VAP")

make_histogram("Htot", "HtotDP", "tot", "Hispanic total pop")
make_histogram("HVAP", "HVAPDP", "totVAP", "Hispanic VAP")





