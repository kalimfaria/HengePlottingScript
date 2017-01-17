import random
import numpy
from matplotlib import pyplot
width = 1/1.5
bins = [5,7,9,11,13,15]

x = [4.05,4.9,7.8,10.0, 12.5,15.0]
y = [4.254966667,6.8336,11.10758333,12.80853333,14.23843333,16.81983333]

pyplot.bar(bins, y, width, fill=False,  label='Convergence Time in Seconds', hatch="*")
pyplot.bar(bins, x, width,  fill=False, label='CPU Utilization', hatch="\\\\")#color="blue",

pyplot.legend(loc='upper left')
pyplot.xlabel('Number of topologies')
pyplot.savefig("/Users/fariakalim/exp72/scalability.png", bbox_inches='tight')

# mpl_fig = pyplot.figure()
# ax = mpl_fig.add_subplot(111)
#
# p1 = ax.bar(bins, x, width, color=(0.2588,0.4433,1.0))
# p2 = ax.bar(bins, y, width, color=(1.0,0.5,0.62), bottom=x)
# ax.set_ylabel('Scores')
# ax.set_xlabel('Groups')
# ax.set_title('Scores by group and gender')
#
# ax.set_xticklabels(('3', '5', '7'))
# pyplot.show()