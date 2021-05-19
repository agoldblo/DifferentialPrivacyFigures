import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score
from matplotlib.ticker import PercentFormatter
import os
import matplotlib.patches as mpatches



path = r'/Users/ari/Documents/PGP/Differential Privacy/Global Analysis/epsilon = 12.2/systematic vs. random'
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
    for i in range_of_levels:
        level = levels[i]
        df = data[data["Level"] == level]
        df = df[(df.totVAP > 0) & (df.totVAPDP > 0)]
        #if i == "Block":
            #df = df[(df.totVAP >= 0) | (df.totVAPDP == 0)]
        x = df[census_col]
        y = df[dp_col]
        res = y - x
        res_perc = res / df[total_col] * 100
        abs_residuals = abs(res_perc)
        #indices = abs_residuals > 0
        #x = x[indices]
        #abs_residuals = abs_residuals[indices]
        #plt.scatter(np.log(x), abs_residuals, alpha = 0.5)
        x_vals.append(np.average(x))
        y_vals.append(np.average(abs_residuals))
    
    plt.scatter(np.log(x_vals), np.log(y_vals))
    z = np.polyfit(np.log(x_vals), np.log(y_vals), 1)
    p = np.poly1d(z)
    rsquare = r2_score(np.log(y_vals), p(np.log(x_vals)))
    plt.plot(np.log(x_vals),p(np.log(x_vals)),"r")
    print(z[1])
    plt.annotate("y = {:.2f}x + {:.2f}\nR^2 = {:.5f}".format(z[0], z[1], rsquare), (min(np.log(x_vals)), min(np.log(y_vals))))
    plt.xlabel("Log(Number of People)")
    plt.ylabel("Log(Average Absolute % Error)")
    plt.title("% Error in total VAP")
    plt.savefig("avg % error plot log.png", bbox_inches='tight')
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

make_histogram("totVAP", "totVAPDP", "totVAP", "all")


