import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score
from matplotlib.ticker import PercentFormatter
import os
import matplotlib.patches as mpatches



path = r'/Users/ari/Documents/PGP/Differential Privacy/Global Analysis/epsilon = 12.2/systematic vs. random/each group'
os.chdir(path)
data = pd.read_excel(r'/Users/ari/Documents/PGP/Differential Privacy/Epsilon12.2ALL.xlsx')


def make_histogram(census_col, dp_col, total_col, race_eth):
    range_of_levels = range(0, 5)
    levels = ["Block", "Small County", "School", "Legislative", "Congress"]
    fig, ax = plt.subplots()
    plt.rcParams.update({'font.size': 16})
    #ax.yaxis.set_major_formatter(PercentFormatter())
    x_vals = []
    y_vals = []
    x_stdev = []
    y_stdev = []
    for i in range_of_levels:
        level = levels[i]
        df = data[data["Level"] == level]
        df = df[df.totVAP > 0]
        x = df[census_col]
        y = df[dp_col]
        res = y - x
        res_perc = res / df[total_col] * 100
        abs_residuals = abs(res_perc)
        indices_abs = (abs_residuals > 0)
        indices_x = (x > 0)
        indices = np.logical_and(indices_abs, indices_x)
        x = x[indices]
        abs_residuals = abs_residuals[indices]
        #print(len(x))
        #print(abs_residuals)
        #plt.scatter(np.log(x), abs_residuals, alpha = 0.5)
        x_vals.append(np.average(np.log(x)))
        y_vals.append(np.average(np.log(abs_residuals)))
        x_stdev.append(np.std(np.log(x)))
        y_stdev.append(np.std(np.log(abs_residuals)))
    
    ax.errorbar(x_vals, y_vals, xerr = x_stdev, yerr = y_stdev, fmt='o')
    z = np.polyfit(x_vals, y_vals, 1)
    p = np.poly1d(z)
    rsquare = r2_score(y_vals, p(x_vals))
    plt.plot(x_vals,p(x_vals),"gray")
    plt.annotate("y = {:.2f} - {:.2f}x \nR^2 = {:.5f}".format(z[1], -z[0], rsquare), (min(x_vals), min(y_vals)))
    max_y = max(y_vals)
    systematic = np.poly1d([0, max_y])
    plt.plot(x_vals, systematic(x_vals),"k")
    plt.annotate("Systematic Errors", (4, 2.75))
    min_x = min(x_vals)
    random = np.poly1d([-0.5, max_y + 0.5*min_x])
    plt.plot(x_vals, random(x_vals), "k")
    plt.annotate("Random Errors", (5, 0.75))
    plt.xlabel("Log({})".format(race_eth))
    plt.ylabel("Log(Absolute % Error)")
    plt.title("% Error in {}".format(race_eth))
    #plt.savefig("avg % error plot log-log nvap.png", bbox_inches='tight')
    plt.show()

#make_histogram("NHbla_alo", "NHbla_aloDP", "tot", "NH Black total pop")
#make_histogram("NHnat_alo", "NHnat_aloDP", "tot", "NH American Indian total pop")
#make_histogram("NHpci_alo", "NHpci_aloDP", "tot", "NH Hawaiian Pac Islander total pop")
#make_histogram("NHasi_alo", "NHasi_aloDP", "tot", "NH Asian total pop")
#make_histogram("NHsor_alo", "NHsor_aloDP", "tot", "NH Some Other Race total pop")
#make_histogram("NH2mo", "NH2moDP", "tot", "NH 2 or more races total pop")

#make_histogram("NHbla_alo_VAP", "NHBVAP_aloDP", "totVAP", "NH Black VAP")
#make_histogram("NHnat_alo_VAP", "NHnatVAP_aloDP", "totVAP", "NH American Indian VAP")
#make_histogram("NHasi_alo_VAP", "NHAVAP_aloDP", "totVAP", "NH Asian VAP")
#make_histogram("NHpci_alo_VAP", "NHpciVAP_aloDP", "totVAP", "NH Hawaiin Pac Islander VAP")
#make_histogram("NHsor_alo_VAP", "NHsorVAP_aloDP", "totVAP", "NH Some Other Race VAP")
#make_histogram("NH2mo_VAP", "NH2moVAPDP", "totVAP", "NH 2 or more races VAP")

#make_histogram("Htot", "HtotDP", "tot", "Hispanic total pop")
#make_histogram("HVAP", "HVAPDP", "totVAP", "Hispanic VAP")

make_histogram("totVAP", "totVAPDP", "totVAP", "totVAP")
make_histogram("NHbla_alo_VAP", "NHBVAP_aloDP", "totVAP", "BVAP")
make_histogram("HVAP", "HVAPDP", "totVAP", "HVAP")
make_histogram("NHasi_alo_VAP", "NHAVAP_aloDP", "totVAP", "AVAP")
make_histogram("NHnat_alo_VAP", "NHnatVAP_aloDP", "totVAP", "NVAP")



