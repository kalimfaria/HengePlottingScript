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
for i in os.listdir("/Users/fariakalim/exp17/"):
    if i.endswith("outputlog2") :
        print i
        f = open("/Users/fariakalim/exp17/"+i, 'r')
        filename = f.__getattribute__("name").split(".")[0]
        print filename
        topology1_time = []
        topology2_time = []
        topology3_time = []
        topology4_time = []
        topology5_time = []
        topology6_time = []

        topology1_latency = []
        topology2_latency = []
        topology3_latency = []
        topology4_latency = []
        topology5_latency = []
        topology6_latency = []

        topology1_juice = []
        topology2_juice = []
        topology3_juice = []
        topology4_juice = []
        topology5_juice = []
        topology6_juice = []


        topology1_utility = []
        topology2_utility = []
        topology3_utility = []
        topology4_utility = []
        topology5_utility = []
        topology6_utility = []



        reduced_topology = []
        num_workers = []
        input_at_source_1 = []
        output_at_sink_1 = []
        input_at_source_2 = []
        output_at_sink_2 = []
        input_at_source_3 = []
        output_at_sink_3 = []
        input_at_source_4 = []
        output_at_sink_4 = []
        input_at_source_5 = []
        output_at_sink_5 = []
        input_at_source_6 = []
        output_at_sink_6 = []



        target = []
        target_operator = []
        victim_operator = []
        victim = []
        rebalance_time = []
        rebalance_desc = []

        #sample
        #production-topology1-1-1477935100,0.22572376766944544,0.38325094771997914,878356.75,0.0019923567502612123,35.0,1780,360,1477936921086
        #production-topology3-3-1477935114,1.799076289207868,1.2240119850930646,0.0,5.0,5.0,480,240,1477936921087

        latency_index = 3
        current_utility_index = 4
        specified_utility_index = 5

        name_index = 0
        juice_index = 2
        input_index = 6
        output_index = 7
        time_index = 8

        for line in f:
                line = line.split("\n")[0]
                one_line = line.split(',')
                if "/var/nimbus/storm" not in one_line[name_index] and len(one_line) > 1:
                    if "production-topology1"  in one_line[name_index]:
                        topology1_time.append(float(one_line[time_index]))
                        topology1_juice.append(float(one_line[juice_index]))
                        topology1_utility.append(float(one_line[current_utility_index]))
                        topology1_latency.append(float(one_line[latency_index]))
                        input_at_source_1.append(float(one_line[input_index]))
                        output_at_sink_1.append(float(one_line[output_index]))
                    elif "production-topology2"  in one_line[name_index]:
                        topology2_latency.append(float(one_line[latency_index]))
                        topology2_juice.append(float(one_line[juice_index]))
                        topology2_utility.append(float(one_line[current_utility_index]))
                        topology2_time.append(float(one_line[time_index]))
                        input_at_source_2.append(float(one_line[input_index]))
                        output_at_sink_2.append(float(one_line[output_index]))
                    elif "production-topology3"  in one_line[name_index]:
                        topology3_time.append(float(one_line[time_index]))
                        input_at_source_3.append(float(one_line[input_index]))
                        topology3_latency.append(float(one_line[latency_index]))
                        topology3_juice.append(float(one_line[juice_index]))
                        topology3_utility.append(float(one_line[current_utility_index]))
                        output_at_sink_3.append(float(one_line[output_index]))
                    elif "production-topology4"  in one_line[name_index]:
                        topology4_juice.append(float(one_line[juice_index]))
                        topology4_time.append(float(one_line[time_index]))
                        topology4_utility.append(float(one_line[current_utility_index]))
                        input_at_source_4.append(float(one_line[input_index]))
                        topology4_latency.append(float(one_line[latency_index]))
                        output_at_sink_4.append(float(one_line[output_index]))
                    elif "production-topology5"  in one_line[name_index]:
                        topology5_juice.append(float(one_line[juice_index]))
                        topology5_time.append(float(one_line[time_index]))
                        topology5_utility.append(float(one_line[current_utility_index]))
                        input_at_source_5.append(float(one_line[input_index]))
                        topology5_latency.append(float(one_line[latency_index]))
                        output_at_sink_5.append(float(one_line[output_index]))
                    elif "production-topology6"  in one_line[name_index]:
                        topology6_juice.append(float(one_line[juice_index]))
                        topology6_time.append(float(one_line[time_index]))
                        topology6_utility.append(float(one_line[current_utility_index]))
                        input_at_source_6.append(float(one_line[input_index]))
                        topology6_latency.append(float(one_line[latency_index]))
                        output_at_sink_6.append(float(one_line[output_index]))

                    elif len(one_line) == 1 and "Running" not in one_line[0] and is_number(one_line[0]):
                        rebalance_time.append(float(one_line[0]))
                elif "/var/nimbus/storm" in one_line[0] :
                    time_for_rebalance = line.split(" ")
                    if "-n" not in line:
                        if flag == 0:
                            string = ""
                            print time_for_rebalance[2]
                            if time_for_rebalance[2] == "production-topology1":
                                string = "T1"
                            elif time_for_rebalance[2] == "production-topology2":
                                string = "T2"
                            elif time_for_rebalance[2] == "production-topology3":
                                string = "T3"
                            elif time_for_rebalance[2] == "production-topology4":
                                string = "T4"
                            elif time_for_rebalance[2] == "production-topology5":
                                string = "T5"
                            elif time_for_rebalance[2] == "production-topology6":
                                string = "T6"
                            else:
                                string = time_for_rebalance[2]
                            str = string + " " + time_for_rebalance[6]
                            #rebalance_desc.append(string + " "+ time_for_rebalance[6]) # should give topology name space num workers
                            i = 7
                            while len(time_for_rebalance) > i:
                                str = str + " "+ time_for_rebalance[i] # should give topology name space num workers
                                i = i + 1
                            rebalance_desc.append(str)

                            #desc_string = " ".join((time_for_rebalance[2] , time_for_rebalance[6]))

                            #rebalance_desc.append(desc_string) # get rid of this if you have multiple rebalances
                     #       flag = 1
                     #   else:
                     #       temp = " ".join((time_for_rebalance[2], time_for_rebalance[6]))
                     #       desc_string = " ".join((desc_string,temp))
                     #       rebalance_desc.append(desc_string)
                     #       desc_string = " "
                     #       flag = 0
                    else:
                        print time_for_rebalance[2]
                        if time_for_rebalance[2] == "production-topology1":
                            rebalance_desc.append("T1")
                        elif time_for_rebalance[2] == "production-topology2":
                            rebalance_desc.append("T2")
                        elif time_for_rebalance[2] == "production-topology3":
                            rebalance_desc.append("T3")
                        elif time_for_rebalance[2] == "production-topology4":
                            rebalance_desc.append("T4")
                        elif time_for_rebalance[2] == "production-topology5":
                            rebalance_desc.append("T5")
                        elif time_for_rebalance[2] == "production-topology6":
                            rebalance_desc.append("T6")
                        else:
                            rebalance_desc.append(time_for_rebalance[2])
                        rebalance_desc.append(" "+ time_for_rebalance[4]) # should give topology name space num workers
                elif len(one_line) == 1 and is_number(one_line[0]):
                    rebalance_time.append(float(one_line[0]))






        fig, ax = plt.subplots()

        ax.scatter(topology6_time, topology6_juice, edgecolors ="black", label="T6 Juice", marker ="*", facecolors='none', s=40,)
        ax.scatter(topology6_time, topology6_utility, edgecolors ="red", label="T6 Utility", marker ="*", facecolors='none', s=40,)
        ax.scatter(topology2_time, topology2_juice, edgecolors ="pink", label="T2 Juice", marker ="<", facecolors='none', s=40,)
        ax.scatter(topology3_time, topology3_juice, edgecolors ="purple", label="T3 Juice", marker="D", facecolors='none', s=40, )
        ax.scatter(topology4_time, topology4_juice, edgecolors ="yellow", label="T4 Juice", marker="+", facecolors='none', s=40,)
        ax.scatter(topology5_time, topology5_juice, edgecolors ="r", label="T5 Juice", marker ="<", facecolors='none', s=40,)
        ax.scatter(topology6_time, topology6_juice, edgecolors ="c", label="T6 Juice", marker="D", facecolors='none', s=40, )

        ax.set_xlabel('Time/S', fontsize=10)
        ax.set_ylabel('Latency/S', fontsize=10)

        ax.grid(True)
        fig.tight_layout()


        print topology1_time
        plt.legend(loc=9, bbox_to_anchor=(0.5, -0.1), ncol=2,prop={'size':10})
        #plt.xlim(1479274679063.0,1479298791275.0)
        #ax.set_ylim(0.5, 1.5)


        plt.savefig(filename+'.png', bbox_inches='tight')

