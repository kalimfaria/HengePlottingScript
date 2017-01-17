import os

import matplotlib.pyplot as plt
import numpy
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def movingaverage(interval, window_size):
    window = numpy.ones(int(window_size))/float(window_size)
    return numpy.convolve(interval, window, 'same')

def reject_outliers(data, m):
    u = numpy.mean(data)
    s = numpy.std(data)
    filtered = []
    for e in data:
        if (u - m * s < e < u + m * s):
            filtered.append(e)
        else:
            print "Does not apply"
            filtered.append(u)
    return filtered

flag = 0
desc_string = " "
for i in os.listdir("/Users/fariakalim/exp103/"):
    if i.endswith("util.log") :
        print i
        f = open("/Users/fariakalim/exp103/"+i, 'r')
        filename = f.__getattribute__("name").split(".")[0]
        print filename
        node1_util = []
        node2_util = []
        node3_util = []
        node4_util = []
        node5_util = []

        node1_user = []
        node2_user = []
        node3_user = []
        node4_user = []
        node5_user = []

        node1_system = []
        node2_system = []
        node3_system = []
        node4_system = []
        node5_system = []

        node1_wait = []
        node2_wait = []
        node3_wait = []
        node4_wait = []
        node5_wait = []

        node1_idle = []
        node2_idle = []
        node3_idle = []
        node4_idle = []
        node5_idle = []

        node1_five = []
        node2_five = []
        node3_five = []
        node4_five = []
        node5_five = []

        node1_mem = []
        node2_mem = []
        node3_mem = []
        node4_mem = []
        node5_mem = []

        time = []
        #(recentLoad + " " + minLoad + " " + " " + fiveMinsLoad + " " + freeMem + " " + usedMemory + " " + usedMemPercent + " " +  user +  " "  + system + " " + nice + " " + wait + " " + idle + " "  + time);

        node_index = 0
        util = 1
        five_mins_util = 4
        time_index = 13#8
        user_index = 8
        system_index =9
        wait_index = 11
        idle_index = 12
        mem_index = 7


        for line in f:
                line = line.split("\n")[0]
                one_line = line.split(' ')

                if len(one_line) is not 14:
                    if "pc484.emulab.net"  in one_line[node_index]:
                        node1_util.append(float(one_line[util]))
                    elif "pc508.emulab.net"  in one_line[node_index]:
                        node2_util.append(float(one_line[util]))
                        time.append(float(one_line[time_index]))
                    elif "pc512.emulab.net"  in one_line[node_index]:
                        node3_util.append(float(one_line[util]))
                    elif "pc440.emulab.net"  in one_line[node_index]:
                        node4_util.append(float(one_line[util]))
                    elif "pc429.emulab.net"  in one_line[node_index]:
                        node5_util.append(float(one_line[util]))
                else:
                    if "node1"  in one_line[node_index]:
                        node1_util.append(float(one_line[util]))
                        node1_mem.append(float(one_line[mem_index]))
                        node1_five.append(float(one_line[five_mins_util]))
                        node1_user.append(float(one_line[user_index]))
                        node1_system.append(float(one_line[system_index]))
                        node1_wait.append(float(one_line[wait_index]))
                        node1_idle.append(float(one_line[idle_index]))
                    elif "node2"  in one_line[node_index]:
                        node2_util.append(float(one_line[util]))
                        node2_user.append(float(one_line[user_index]))
                        node2_mem.append(float(one_line[mem_index]))
                        node2_five.append(float(one_line[five_mins_util]))
                        node2_idle.append(float(one_line[idle_index]))
                        node2_system.append(float(one_line[system_index]))
                        node2_wait.append(float(one_line[wait_index]))
                        time.append(float(one_line[time_index]))
                    elif "node3"  in one_line[node_index]:
                        node3_util.append(float(one_line[util]))
                        node3_user.append(float(one_line[user_index]))
                        node3_idle.append(float(one_line[idle_index]))
                        node3_five.append(float(one_line[five_mins_util]))
                        node3_mem.append(float(one_line[mem_index]))
                        node3_system.append(float(one_line[system_index]))
                        node3_wait.append(float(one_line[wait_index]))
                    elif "node4"  in one_line[node_index]:
                        node4_util.append(float(one_line[util]))
                        node4_user.append(float(one_line[user_index]))
                        node4_idle.append(float(one_line[idle_index]))
                        node4_five.append(float(one_line[five_mins_util]))
                        node4_mem.append(float(one_line[mem_index]))
                        node4_system.append(float(one_line[system_index]))
                        node4_wait.append(float(one_line[wait_index]))
                    elif "node5"  in one_line[node_index]:
                        node5_util.append(float(one_line[util]))
                        node5_idle.append(float(one_line[idle_index]))
                        node5_five.append(float(one_line[five_mins_util]))
                        node5_user.append(float(one_line[user_index]))
                        node5_system.append(float(one_line[system_index]))
                        node5_wait.append(float(one_line[wait_index]))
                        node5_mem.append(float(one_line[mem_index]))


        print time


        val = time[0]
        for i in range(0, len(time)):
            time[i] = (time[i] - val)/1000

        #rebalance_line = (1479208637012 - val)/1000
        #print rebalance_line



        min_length = len(time)

        if min_length > len(node1_util):
            min_length = len(node1_util)
        if min_length > len(node2_util):
            min_length = len(node2_util)
        if min_length > len(node3_util):
            min_length = len(node3_util)
        if min_length > len(node4_util):
            min_length = len(node4_util)
        if min_length > len(node5_util):
            min_length = len(node5_util)

        if min_length > len(node1_user):
            min_length = len(node1_user)
        if min_length > len(node2_user):
            min_length = len(node2_user)
        if min_length > len(node3_user):
            min_length = len(node3_user)
        if min_length > len(node4_user):
            min_length = len(node4_user)
        if min_length > len(node5_user):
            min_length = len(node5_user)

        if min_length > len(node1_system):
            min_length = len(node1_system)
        if min_length > len(node2_system):
            min_length = len(node2_system)
        if min_length > len(node3_system):
            min_length = len(node3_system)
        if min_length > len(node4_system):
            min_length = len(node4_system)
        if min_length > len(node5_system):
            min_length = len(node5_system)

        if min_length > len(node1_wait):
            min_length = len(node1_wait)
        if min_length > len(node2_wait):
            min_length = len(node2_wait)
        if min_length > len(node3_wait):
            min_length = len(node3_wait)
        if min_length > len(node4_wait):
            min_length = len(node4_wait)
        if min_length > len(node5_wait):
            min_length = len(node5_wait)

        time = time[0:min_length]
        node1_util = node1_util [0:min_length]
        node2_util = node2_util [0:min_length]
        node3_util = node3_util [0:min_length]
        node4_util = node4_util [0:min_length]
        node5_util = node5_util [0:min_length]

        node1_user = node1_user [0:min_length]
        node2_user = node2_user [0:min_length]
        node3_user = node3_user [0:min_length]
        node4_user = node4_user [0:min_length]
        node5_user = node5_user [0:min_length]

        node1_wait = node1_wait [0:min_length]
        node2_wait = node2_wait [0:min_length]
        node3_wait = node3_wait [0:min_length]
        node4_wait = node4_wait [0:min_length]
        node5_wait = node5_wait [0:min_length]

        node1_system = node1_system [0:min_length]
        node2_system = node2_system [0:min_length]
        node3_system = node3_system [0:min_length]
        node4_system = node4_system [0:min_length]
        node5_system = node5_system [0:min_length]

        node1_idle = node1_idle [0:min_length]
        node2_idle = node2_idle [0:min_length]
        node3_idle = node3_idle [0:min_length]
        node4_idle = node4_idle [0:min_length]
        node5_idle = node5_idle [0:min_length]

        node1_five = node1_five [0:min_length]
        node2_five = node2_five [0:min_length]
        node3_five = node3_five [0:min_length]
        node4_five = node4_five [0:min_length]
        node5_five = node5_five [0:min_length]

        node1_mem = node1_mem [0:min_length]
        node2_mem = node2_mem [0:min_length]
        node3_mem = node3_mem [0:min_length]
        node4_mem = node4_mem [0:min_length]
        node5_mem = node5_mem [0:min_length]

        x_start = 900
        x_end = 3500

        fig, ax = plt.subplots()
#        rebalance_time = [1480135733742,1480136036967,1480136036972,1480136036976,1480136054203,1480136366397,1480136674565,1480136982197,1480137292227,1480137602281,1480137911717,1480138220429,1480138531297,1480138842837,1480139153309,1480139463590,1480139775539,1480140086927,1480140398892,1480140711130,1480141022350,1480141336109,1480141648305,1480141962259,1480142274761,1480142586231,1480142899515,1480143211947,1480143525507,1480143838967,1480144152417,1480144466410,1480144781333,1480145095588,1480145410621,1480145725700,1480146041850,1480146357653,1480146673371,1480146988095,1480147301069,1480147615454,1480147931757,1480148248410,1480148563545,1480148878423,1480149194454,1480149511278,1480149827236,1480150143907,1480150458920,1480150775596,1480151091705,1480151408465,1480151726681,1480152043112,1480152344327,1480152662772,1480152964400,1480153265536,1480153567059,1480153885089,1480154203224,1480154817923,1480156061475,1480156677651,1480156979289,1480159803553]

#        for i in range(0, len(rebalance_time)):
 #           rebalance_time[i] = (rebalance_time[i] - val)/1000

#        clrs = ["k", "k", "k", "k", "k", "k", "k"]
#        linestyles = [ '--' , '-.' , 'solid', 'dotted']
 #        for j in range(0, len(rebalance_time)):
 #            #if j%7 == 0:
 # #           if rebalance_time[j] > 17200 and rebalance_time[j] <= 17400:
 #      #      if ("T1" in rebalance_desc[j]):#and (rebalance_time[j] > 11000 and rebalance_time[j] <= 55000)
 #
 #            ax.vlines(x=rebalance_time[j], ymax=8 , ymin=-1,  colors=clrs[j%7], linestyle= 'solid')#linestyles[j%4]

        ax.scatter(time, node1_util, edgecolors ="black", label="Node 1 Load", marker ="*", facecolors='none', s=40,)
        ax.scatter(time, node2_util, edgecolors ="pink", label="Node 2 Load", marker ="<", facecolors='none', s=40,)
        ax.scatter(time, node3_util, edgecolors ="purple", label="Node 3 Load", marker="D", facecolors='none', s=40, )
        ax.scatter(time, node4_util, edgecolors ="yellow", label="Node 4 Load", marker="+", facecolors='none', s=40,)
        ax.scatter(time, node5_util, edgecolors ="r", label="Node 5 Load", marker ="<", facecolors='none', s=40,)

        ax.set_xlabel('Time/S', fontsize=10)
        ax.set_ylabel('Load', fontsize=10)

        plt.xlim(x_start,x_end)
        #plt.xlim(16150,30000)
        plt.ylim(0,6)
        plt.legend(loc=9, bbox_to_anchor=(0.5, -0.1), ncol=2,prop={'size':10})

        ax.grid(True)
        fig.tight_layout()
        plt.savefig(filename+"-util.png", bbox_inches='tight')

        fig, ax = plt.subplots()

        ax.scatter(time, node1_user, edgecolors ="black", label="Node 1 User", marker ="*", facecolors='none', s=40,)
        ax.scatter(time, node2_user, edgecolors ="pink", label="Node 2 User", marker ="<", facecolors='none', s=40,)
        ax.scatter(time, node3_user, edgecolors ="purple", label="Node 3 User", marker="D", facecolors='none', s=40, )
        ax.scatter(time, node4_user, edgecolors ="yellow", label="Node 4 User", marker="+", facecolors='none', s=40,)
        ax.scatter(time, node5_user, edgecolors ="r", label="Node 5 User", marker ="<", facecolors='none', s=40,)

        plt.xlim(x_start,x_end)
        #plt.xlim(0,60000)
       # plt.ylim(0,8)
        ax.set_xlabel('Time/S', fontsize=10)
        ax.set_ylabel('CPU Util', fontsize=10)

        plt.legend(loc=9, bbox_to_anchor=(0.5, -0.1), ncol=2,prop={'size':10})

        ax.grid(True)
        fig.tight_layout()
        plt.savefig(filename+"-user.png", bbox_inches='tight')

        fig, ax = plt.subplots()

        ax.scatter(time, node1_wait, edgecolors ="black", label="Node 1 Wait", marker ="*", facecolors='none', s=40,)
        ax.scatter(time, node2_wait, edgecolors ="pink", label="Node 2 Wait", marker ="<", facecolors='none', s=40,)
        ax.scatter(time, node3_wait, edgecolors ="purple", label="Node 3 Wait", marker="D", facecolors='none', s=40, )
        ax.scatter(time, node4_wait, edgecolors ="yellow", label="Node 4 Wait", marker="+", facecolors='none', s=40,)
        ax.scatter(time, node5_wait, edgecolors ="r", label="Node 5 Wait", marker ="<", facecolors='none', s=40,)

        plt.xlim(x_start,x_end)
        #plt.xlim(0,60000)
        plt.ylim(0,0.15)
        ax.set_xlabel('Time/S', fontsize=10)
        ax.set_ylabel('CPU Util', fontsize=10)
        plt.legend(loc=9, bbox_to_anchor=(0.5, -0.1), ncol=2,prop={'size':10})

        ax.grid(True)
        fig.tight_layout()
        plt.savefig(filename+"-wait.png", bbox_inches='tight')

        fig, ax = plt.subplots()

        ax.scatter(time, node1_system, edgecolors ="black", label="Node 1 System", marker ="*", facecolors='none', s=40,)
        ax.scatter(time, node2_system, edgecolors ="pink", label="Node 2 System", marker ="<", facecolors='none', s=40,)
        ax.scatter(time, node3_system, edgecolors ="purple", label="Node 3 System", marker="D", facecolors='none', s=40, )
        ax.scatter(time, node4_system, edgecolors ="yellow", label="Node 4 System", marker="+", facecolors='none', s=40,)
        ax.scatter(time, node5_system, edgecolors ="r", label="Node 5 System", marker ="<", facecolors='none', s=40,)

        plt.xlim(x_start,x_end)
        #plt.xlim(0,60000)
       # plt.ylim(0,8)
        ax.set_xlabel('Time/S', fontsize=10)
        ax.set_ylabel('CPU Util', fontsize=10)
        plt.legend(loc=9, bbox_to_anchor=(0.5, -0.1), ncol=2,prop={'size':10})

        ax.grid(True)
        fig.tight_layout()
        plt.savefig(filename+"-system.png", bbox_inches='tight')


        fig, ax = plt.subplots()

        print time
        print node1_idle
        print len(time)
        print len(node1_idle)
        print min_length

        ax.scatter(time, node1_idle, edgecolors ="black", label="Node 1 Idle", marker ="*", facecolors='none', s=40,)
        ax.scatter(time, node2_idle, edgecolors ="pink", label="Node 2 Idle", marker ="<", facecolors='none', s=40,)
        ax.scatter(time, node3_idle, edgecolors ="purple", label="Node 3 Idle", marker="D", facecolors='none', s=40, )
        ax.scatter(time, node4_idle, edgecolors ="yellow", label="Node 4 Idle", marker="+", facecolors='none', s=40,)
        ax.scatter(time, node5_idle, edgecolors ="r", label="Node 5 Idle", marker ="<", facecolors='none', s=40,)

        plt.xlim(x_start,x_end)
        #plt.xlim(0,60000)
       # plt.ylim(0,8)
        ax.set_xlabel('Time/S', fontsize=10)
        ax.set_ylabel('CPU Util', fontsize=10)
        plt.legend(loc=9, bbox_to_anchor=(0.5, -0.1), ncol=2,prop={'size':10})

        ax.grid(True)
        fig.tight_layout()
        plt.savefig(filename+"-idle.png", bbox_inches='tight')


#        ax.vlines(x=rebalance_line, ymax=60 , ymin=-1,  colors='blue', linestyle= 'solid', label="Reduced Topology 7",)#linestyles[j%4]

        #ax2.scatter(time, topology7_latency, edgecolors ="m", label="T7 Latency", marker="+", facecolors='none', s=40,)

        fig, ax = plt.subplots()

        ax.scatter(time, node1_five, edgecolors ="black", label="Node 1 Five Mins Load", marker ="*", facecolors='none', s=40,)
        ax.scatter(time, node2_five, edgecolors ="pink", label="Node 2 Five Mins Load", marker ="<", facecolors='none', s=40,)
        ax.scatter(time, node3_five, edgecolors ="purple", label="Node 3 Five Mins Load", marker="D", facecolors='none', s=40, )
        ax.scatter(time, node4_five, edgecolors ="yellow", label="Node 4 Five Mins Load", marker="+", facecolors='none', s=40,)
        ax.scatter(time, node5_five, edgecolors ="r", label="Node 5 Five Mins Load", marker ="<", facecolors='none', s=40,)

        #plt.xlim(x_start,x_end)
        plt.xlim(16150,20000)
        plt.ylim(3.9,6)
        ax.set_xlabel('Time/S', fontsize=10)
        ax.set_ylabel('CPU Util', fontsize=10)

        plt.legend(loc=9, bbox_to_anchor=(0.5, -0.1), ncol=2,prop={'size':10})

        ax.grid(True)
        fig.tight_layout()
        plt.savefig(filename+"-five-mins.png", bbox_inches='tight')


        fig, ax = plt.subplots()

        ax.scatter(time, node1_mem, edgecolors ="black", label="Node 1 Memory Percentage", marker ="*", facecolors='none', s=40,)
        ax.scatter(time, node2_mem, edgecolors ="pink", label="Node 2 Percentage", marker ="<", facecolors='none', s=40,)
        ax.scatter(time, node3_mem, edgecolors ="purple", label="Node 3 Percentage", marker="D", facecolors='none', s=40, )
        ax.scatter(time, node4_mem, edgecolors ="yellow", label="Node 4 Percentage", marker="+", facecolors='none', s=40,)
        ax.scatter(time, node5_mem, edgecolors ="r", label="Node 5 Percentage", marker ="<", facecolors='none', s=40,)

        plt.xlim(x_start,x_end)
        #plt.xlim(0,60000)
       # plt.ylim(0,8)
        ax.set_xlabel('Time/S', fontsize=10)
        ax.set_ylabel('CPU Util', fontsize=10)

        plt.legend(loc=9, bbox_to_anchor=(0.5, -0.1), ncol=2,prop={'size':10})

        ax.grid(True)
        fig.tight_layout()
        plt.savefig(filename+"-mem.png", bbox_inches='tight')