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


flag = 0
desc_string = " "
for i in os.listdir("/Users/fariakalim/exp24/"):
    if  i.endswith("etp-chosen-component-top2.log") : #i.endswith("capacity.log") or
        print i
        f = open("/Users/fariakalim/exp24/"+i, 'r')
        filename = f.__getattribute__("name").split(".")[0]
        print filename
        topology1_bolt_aggregate = []
        topology1_spout = []
        topology1_bolt_transform = []
        topology1_bolt_output_sink = []
        topology1_bolt_join = []
        topology1_bolt_filter = []
        topology1_bolt_filter_2 = []


        time = []
        time_marker = 0
        time_markers = []

        chosen_topology1_bolt_aggregate = []
        chosen_topology1_spout = []
        chosen_topology1_bolt_transform = []
        chosen_topology1_bolt_output_sink = []
        chosen_topology1_bolt_join = []
        chosen_topology1_bolt_filter = []
        chosen_topology1_bolt_filter_2 = []

        time_topology1_bolt_aggregate = []
        time_topology1_spout = []
        time_topology1_bolt_transform = []
        time_topology1_bolt_output_sink = []
        time_topology1_bolt_join = []
        time_topology1_bolt_filter = []
        time_topology1_bolt_filter_2 = []


        name_index = 0
        operator_index = 1
        capacity_index = 2
        time_index = 3

        component_index = 6
        component_etp_index = 7

        for line in f:
                line = line.split("\n")[0]

                one_line = line.split(' ')
                if len(one_line) == 4:
                    if "spout_head"  in one_line[operator_index]:
                        if "production-topology2-" in one_line[name_index]:
                            topology1_spout.append(float(one_line[capacity_index]))
                    elif "bolt_aggregate"  in one_line[operator_index]:
                        if "production-topology2-" in one_line[name_index]:
                            time.append(float(one_line[time_index]))
                            time_marker = float(one_line[time_index])
                            topology1_bolt_aggregate.append(float(one_line[capacity_index]))
                    elif "bolt_transform"  in one_line[operator_index]:
                        if "production-topology2-" in one_line[name_index]:
                            topology1_bolt_transform.append(float(one_line[capacity_index]))
                    elif "bolt_output_sink"  in one_line[operator_index]:
                        if "production-topology2-" in one_line[name_index]:
                            topology1_bolt_output_sink.append(float(one_line[capacity_index]))
                    elif "bolt_join"  in one_line[operator_index]:
                        if "production-topology2-" in one_line[name_index]:
                            topology1_bolt_join.append(float(one_line[capacity_index]))
                    elif "bolt_filter_2"  in one_line[operator_index]:
                        if "production-topology2-" in one_line[name_index]:
                            topology1_bolt_filter_2.append(float(one_line[capacity_index]))
                    elif "bolt_filter"  in one_line[operator_index]:
                        if "production-topology2-" in one_line[name_index]:
                            topology1_bolt_filter.append(float(one_line[capacity_index]))
                else:
                    if float(one_line[component_etp_index]) == 1.0:
                        #time_markers.append(time_marker)
                        #component_etp.append(float(one_line[component_etp_index]))
                        if "spout_head"  in one_line[component_index]:
                            chosen_topology1_spout.append(float(one_line[component_etp_index]))
                            time_topology1_spout.append(time_marker)

                        elif "bolt_aggregate"  in one_line[component_index]:
                            chosen_topology1_bolt_aggregate.append(float(one_line[component_etp_index]))
                            time_topology1_bolt_aggregate.append(time_marker)

                        elif "bolt_transform"  in one_line[component_index]:
                            chosen_topology1_bolt_transform.append(float(one_line[component_etp_index]))
                            time_topology1_bolt_transform.append(time_marker)

                        elif "bolt_output_sink"  in one_line[component_index]:

                            chosen_topology1_bolt_output_sink.append(float(one_line[component_etp_index]))
                            time_topology1_bolt_output_sink.append(time_marker)

                        elif "bolt_join"  in one_line[component_index]:
                            chosen_topology1_bolt_join.append(float(one_line[component_etp_index]))
                            time_topology1_bolt_join.append(time_marker)

                        elif "bolt_filter_2"  in one_line[component_index]:
                            chosen_topology1_bolt_filter_2.append(float(one_line[component_etp_index]))
                            time_topology1_bolt_filter_2.append(time_marker)

                        elif "bolt_filter"  in one_line[component_index]:
                            chosen_topology1_bolt_filter.append(float(one_line[component_etp_index]))
                            time_topology1_bolt_filter.append(time_marker)




        min_length = len(time)
        if min_length > len(topology1_bolt_aggregate):
            min_length = len(topology1_bolt_aggregate)
        if min_length > len(topology1_spout):
            min_length = len(topology1_spout)
        if min_length > len(topology1_bolt_transform):
            min_length = len(topology1_bolt_transform)
        if min_length > len(topology1_bolt_output_sink):
            min_length = len(topology1_bolt_output_sink)
        if min_length > len(topology1_bolt_join):
            min_length = len(topology1_bolt_join)
        if min_length > len(topology1_bolt_filter):
            min_length = len(topology1_bolt_filter)
        if min_length > len(topology1_bolt_filter_2):
            min_length = len(topology1_bolt_filter_2)



        time = time[0:min_length]
        topology1_bolt_aggregate = topology1_bolt_aggregate[0:min_length]
        topology1_spout = topology1_spout[0:min_length]
        topology1_bolt_transform = topology1_bolt_transform[0:min_length]
        topology1_bolt_output_sink = topology1_bolt_output_sink[0:min_length]
        topology1_bolt_join = topology1_bolt_join[0:min_length]
        topology1_bolt_filter = topology1_bolt_filter[0:min_length]
        topology1_bolt_filter_2 = topology1_bolt_filter_2[0:min_length]


        val = time[0]
        for i in range(0, len(time)):
            time[i] = (time[i] - val)/1000

        for i in range(0, len(time_topology1_bolt_aggregate)):
            time_topology1_bolt_aggregate[i] = (time_topology1_bolt_aggregate[i] - val)/1000

        for i in range(0, len(time_topology1_spout)):
            time_topology1_spout[i] = (time_topology1_spout[i] - val)/1000

        for i in range(0, len(time_topology1_bolt_transform)):
            time_topology1_bolt_transform[i] = (time_topology1_bolt_transform[i] - val)/1000

        for i in range(0, len(time_topology1_bolt_output_sink)):
            time_topology1_bolt_output_sink[i] = (time_topology1_bolt_output_sink[i] - val)/1000

        for i in range(0, len(time_topology1_bolt_filter_2)):
            time_topology1_bolt_filter_2[i] = (time_topology1_bolt_filter_2[i] - val)/1000

        for i in range(0, len(time_topology1_bolt_join)):
            time_topology1_bolt_join[i] = (time_topology1_bolt_join[i] - val)/1000

        for i in range(0, len(time_topology1_bolt_filter)):
            time_topology1_bolt_filter[i] = (time_topology1_bolt_filter[i] - val)/1000


        # D > s
        fig, ax = plt.subplots()
       # print topology1_bolt_aggregate
       # print time
        ax.scatter(time, topology1_bolt_aggregate, edgecolors ="blue", label="T2 Latency SLO=50 bolt_aggregate", marker ="s", facecolors='none', s=10,)

        ax.set_xlabel('Time/S', fontsize=10)
        ax.set_ylabel('ETP', fontsize=10)

        ax.grid(True)
        fig.tight_layout()

        lines, labels = ax.get_legend_handles_labels()
        ax.legend(lines, labels, loc=9, bbox_to_anchor=(0.5, -0.1), ncol=2,prop={'size':10})

        plt.xlim(0,11000)
        ax.set_ylim(-0.1, 1.1)

        plt.savefig(filename+'-aggregate-topology2.png', bbox_inches='tight')

        fig, ax = plt.subplots()
        ax.scatter(time, topology1_spout, edgecolors ="green", label="T2 spout", marker ="s", facecolors='none', s=10,)

        ax.set_xlabel('Time/S', fontsize=10)
        ax.set_ylabel('ETP', fontsize=10)

        ax.grid(True)
        fig.tight_layout()

        lines, labels = ax.get_legend_handles_labels()
        ax.legend(lines, labels, loc=9, bbox_to_anchor=(0.5, -0.1), ncol=2,prop={'size':10})

        plt.xlim(0,11000)
        ax.set_ylim(0.0, 1.1)

        plt.savefig(filename+'-spout-topology2.png', bbox_inches='tight')

        fig, ax = plt.subplots()
        ax.scatter(time, topology1_bolt_transform, edgecolors ="darkorange", label="T2 bolt_transform", marker="s", facecolors='none', s=10,)

        ax.set_xlabel('Time/S', fontsize=10)
        ax.set_ylabel('ETP', fontsize=10)

        ax.grid(True)
        fig.tight_layout()

        lines, labels = ax.get_legend_handles_labels()
        ax.legend(lines, labels, loc=9, bbox_to_anchor=(0.5, -0.1), ncol=2,prop={'size':10})

        plt.xlim(0,11000)
        ax.set_ylim(0.0, 1.1)

        plt.savefig(filename+'-transform-topology2.png', bbox_inches='tight')

        fig, ax = plt.subplots()
        ax.scatter(time, topology1_bolt_output_sink, edgecolors ="darkorange", label="T2 bolt_output_sink", marker="s", facecolors='none', s=10,)

        ax.set_xlabel('Time/S', fontsize=10)
        ax.set_ylabel('ETP', fontsize=10)

        ax.grid(True)
        fig.tight_layout()

        lines, labels = ax.get_legend_handles_labels()
        ax.legend(lines, labels, loc=9, bbox_to_anchor=(0.5, -0.1), ncol=2,prop={'size':10})

        plt.xlim(0,11000)
        ax.set_ylim(0.0, 1.1)

        plt.savefig(filename+'-output-topology2.png', bbox_inches='tight')

        fig, ax = plt.subplots()
        ax.scatter(time, topology1_bolt_join, edgecolors ="pink", label="T2 bolt_join", marker="s", facecolors='none', s=10,)

        ax.set_xlabel('Time/S', fontsize=10)
        ax.set_ylabel('ETP', fontsize=10)

        ax.grid(True)
        fig.tight_layout()

        lines, labels = ax.get_legend_handles_labels()
        ax.legend(lines, labels, loc=9, bbox_to_anchor=(0.5, -0.1), ncol=2,prop={'size':10})

        plt.xlim(0,11000)
        ax.set_ylim(0.0, 1.1)

        plt.savefig(filename+'-join-topology2.png', bbox_inches='tight')

        fig, ax = plt.subplots()
        ax.scatter(time, topology1_bolt_filter, edgecolors ="yellow", label="T2 bolt_filter", marker="s", facecolors='none', s=10,)

        ax.set_xlabel('Time/S', fontsize=10)
        ax.set_ylabel('ETP', fontsize=10)

        ax.grid(True)
        fig.tight_layout()

        lines, labels = ax.get_legend_handles_labels()
        ax.legend(lines, labels, loc=9, bbox_to_anchor=(0.5, -0.1), ncol=2,prop={'size':10})

        plt.xlim(0,11000)
        ax.set_ylim(0.0, 1.1)

        plt.savefig(filename+'-filter-topology2.png', bbox_inches='tight')

        fig, ax = plt.subplots()
        ax.scatter(time, topology1_bolt_filter_2, edgecolors ="black", label="T2 bolt_filter_2", marker="s", facecolors='none', s=10,)

        ax.set_xlabel('Time/S', fontsize=10)
        ax.set_ylabel('ETP', fontsize=10)

        ax.grid(True)
        fig.tight_layout()

        lines, labels = ax.get_legend_handles_labels()
        ax.legend(lines, labels, loc=9, bbox_to_anchor=(0.5, -0.1), ncol=2,prop={'size':10})

        plt.xlim(0,11000)
        ax.set_ylim(0.0, 1.1)

        plt.savefig(filename+'-filter2-topology2.png', bbox_inches='tight')

        fig, ax = plt.subplots()

     #   for j in range(0, len(time_markers)):
     #       if (time_markers[j] >=0 and time_markers[j] <= 11000):
     #           la = component[j]
     #           ax.vlines(x=time_markers[j], ymax=component_etp[j] , ymin=-1,  colors='b', linestyle= 'solid', label=la)


      #  ax.scatter(time_markers, component_etp, edgecolors ="black", label="Bolts Chosen", marker="s", facecolors='none', s=10,)
       # ax.scatter(time_topology1_bolt_aggregate, chosen_topology1_bolt_aggregate, edgecolors ="black", label="bolt_aggregate", marker="s", facecolors='none', s=10,)
       # ax.scatter(time_topology1_bolt_transform, chosen_topology1_bolt_transform, edgecolors ="blue", label="bolt_transform", marker="s", facecolors='none', s=10,)
       # ax.scatter(time_topology1_bolt_output_sink, chosen_topology1_bolt_output_sink, edgecolors ="green", label="bolt_output_sink", marker="s", facecolors='none', s=10,)
       # ax.scatter(time_topology1_bolt_filter_2, chosen_topology1_bolt_filter_2, edgecolors ="red", label="bolt_filter_2", marker="s", facecolors='none', s=10,)
       # ax.scatter(time_topology1_bolt_filter, chosen_topology1_bolt_filter, edgecolors ="yellow", label="bolt_filter", marker="s", facecolors='none', s=10,)
       # ax.scatter(time_topology1_bolt_join, chosen_topology1_bolt_join, edgecolors ="pink", label="bolt_join", marker="s", facecolors='none', s=10,)
        ax.scatter(time_topology1_spout, chosen_topology1_spout, edgecolors ="blue", label="spout", marker="s", facecolors='none', s=10,)

        ax.set_xlabel('Time/S', fontsize=10)
        ax.set_ylabel('ETP', fontsize=10)

        ax.grid(True)
        fig.tight_layout()

        lines, labels = ax.get_legend_handles_labels()
        ax.legend(lines, labels, loc=9, bbox_to_anchor=(0.5, -0.1), ncol=2,prop={'size':10})

        plt.xlim(0,11000)
        ax.set_ylim(-1.0, 2.0)

        plt.savefig(filename+'-etp-chosen-comp-bolt-spout.png', bbox_inches='tight')

