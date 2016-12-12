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
    if  i.endswith("capacity.log") : #i.endswith("capacity.log") or
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

        topology2_bolt_aggregate = []
        topology2_spout = []
        topology2_bolt_transform = []
        topology2_bolt_output_sink = []
        topology2_bolt_join = []
        topology2_bolt_filter = []
        topology2_bolt_filter_2 = []

        topology3_bolt_aggregate = []
        topology3_spout = []
        topology3_bolt_transform = []
        topology3_bolt_output_sink = []
        topology3_bolt_join = []
        topology3_bolt_filter = []
        topology3_bolt_filter_2 = []

        topology4_bolt_aggregate = []
        topology4_spout = []
        topology4_bolt_transform = []
        topology4_bolt_output_sink = []
        topology4_bolt_join = []
        topology4_bolt_filter = []
        topology4_bolt_filter_2 = []

        time = []

        name_index = 0
        operator_index = 1
        capacity_index = 2
        time_index = 3

        for line in f:
                line = line.split("\n")[0]

                one_line = line.split(' ')
                if len(one_line) == 4:
                    if "spout_head"  in one_line[operator_index]:
                        if "production-topology1-" in one_line[name_index]:
                            topology1_spout.append(float(one_line[capacity_index]))
                        elif "production-topology2" in one_line[name_index]:
                            topology2_spout.append(float(one_line[capacity_index]))
                        elif "production-topology3" in one_line[name_index]:
                            topology3_spout.append(float(one_line[capacity_index]))
                        elif "production-topology4" in one_line[name_index]:
                            topology4_spout.append(float(one_line[capacity_index]))
                    elif "bolt_aggregate"  in one_line[operator_index]:
                        if "production-topology1-" in one_line[name_index]:
                            time.append(float(one_line[time_index]))
                            topology1_bolt_aggregate.append(float(one_line[capacity_index]))
                        elif "production-topology2" in one_line[name_index]:
                            topology2_bolt_aggregate.append(float(one_line[capacity_index]))
                        elif "production-topology3" in one_line[name_index]:
                            topology3_bolt_aggregate.append(float(one_line[capacity_index]))
                        elif "production-topology4" in one_line[name_index]:
                            topology4_bolt_aggregate.append(float(one_line[capacity_index]))
                    elif "bolt_transform"  in one_line[operator_index]:
                        if "production-topology1-" in one_line[name_index]:
                            topology1_bolt_transform.append(float(one_line[capacity_index]))
                        elif "production-topology2" in one_line[name_index]:
                            topology2_bolt_transform.append(float(one_line[capacity_index]))
                        elif "production-topology3" in one_line[name_index]:
                            topology3_bolt_transform.append(float(one_line[capacity_index]))
                        elif "production-topology4" in one_line[name_index]:
                            topology4_bolt_transform.append(float(one_line[capacity_index]))
                    elif "bolt_output_sink"  in one_line[operator_index]:
                        if "production-topology1-" in one_line[name_index]:
                            topology1_bolt_output_sink.append(float(one_line[capacity_index]))
                        elif "production-topology2" in one_line[name_index]:
                            topology2_bolt_output_sink.append(float(one_line[capacity_index]))
                        elif "production-topology3" in one_line[name_index]:
                            topology3_bolt_output_sink.append(float(one_line[capacity_index]))
                        elif "production-topology4" in one_line[name_index]:
                            topology4_bolt_output_sink.append(float(one_line[capacity_index]))
                    elif "bolt_join"  in one_line[operator_index]:
                        if "production-topology1-" in one_line[name_index]:
                            topology1_bolt_join.append(float(one_line[capacity_index]))
                        elif "production-topology2" in one_line[name_index]:
                            topology2_bolt_join.append(float(one_line[capacity_index]))
                        elif "production-topology3" in one_line[name_index]:
                            topology3_bolt_join.append(float(one_line[capacity_index]))
                        elif "production-topology4" in one_line[name_index]:
                            topology4_bolt_join.append(float(one_line[capacity_index]))
                    elif "bolt_filter_2"  in one_line[operator_index]:
                        if "production-topology1-" in one_line[name_index]:
                            topology1_bolt_filter_2.append(float(one_line[capacity_index]))
                        elif "production-topology2" in one_line[name_index]:
                            topology2_bolt_filter_2.append(float(one_line[capacity_index]))
                        elif "production-topology3" in one_line[name_index]:
                            topology3_bolt_filter_2.append(float(one_line[capacity_index]))
                        elif "production-topology4" in one_line[name_index]:
                            topology4_bolt_filter_2.append(float(one_line[capacity_index]))
                    elif "bolt_filter"  in one_line[operator_index]:
                        if "production-topology1-" in one_line[name_index]:
                            topology1_bolt_filter.append(float(one_line[capacity_index]))
                        elif "production-topology2" in one_line[name_index]:
                            topology2_bolt_filter.append(float(one_line[capacity_index]))
                        elif "production-topology3" in one_line[name_index]:
                            topology3_bolt_filter.append(float(one_line[capacity_index]))
                        elif "production-topology4" in one_line[name_index]:
                            topology4_bolt_filter.append(float(one_line[capacity_index]))


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

        if min_length > len(topology2_bolt_aggregate):
            min_length = len(topology2_bolt_aggregate)
        #if min_length > len(topology2_spout):
        #    min_length = len(topology2_spout)
        if min_length > len(topology2_bolt_transform):
            min_length = len(topology2_bolt_transform)
        if min_length > len(topology2_bolt_output_sink):
            min_length = len(topology2_bolt_output_sink)
        if min_length > len(topology2_bolt_join):
            min_length = len(topology2_bolt_join)
        if min_length > len(topology2_bolt_filter):
            min_length = len(topology2_bolt_filter)
        if min_length > len(topology2_bolt_filter_2):
            min_length = len(topology2_bolt_filter_2)

        if min_length > len(topology3_bolt_aggregate):
            min_length = len(topology3_bolt_aggregate)
        #if min_length > len(topology3_spout):
        #    min_length = len(topology3_spout)
        if min_length > len(topology3_bolt_transform):
            min_length = len(topology3_bolt_transform)
        if min_length > len(topology3_bolt_output_sink):
            min_length = len(topology3_bolt_output_sink)
        if min_length > len(topology3_bolt_join):
            min_length = len(topology3_bolt_join)
        if min_length > len(topology3_bolt_filter):
            min_length = len(topology3_bolt_filter)
        if min_length > len(topology3_bolt_filter_2):
            min_length = len(topology3_bolt_filter_2)

        if min_length > len(topology4_bolt_aggregate):
            min_length = len(topology4_bolt_aggregate)
        #if min_length > len(topology4_spout):
        #    min_length = len(topology4_spout)
        if min_length > len(topology4_bolt_transform):
            min_length = len(topology4_bolt_transform)
        if min_length > len(topology4_bolt_output_sink):
            min_length = len(topology4_bolt_output_sink)
        if min_length > len(topology4_bolt_join):
            min_length = len(topology4_bolt_join)
        if min_length > len(topology4_bolt_filter):
            min_length = len(topology4_bolt_filter)
        if min_length > len(topology4_bolt_filter_2):
            min_length = len(topology4_bolt_filter_2)

        time = time[0:min_length]
        topology1_bolt_aggregate = topology1_bolt_aggregate[0:min_length]
        topology1_spout = topology1_spout[0:min_length]
        topology1_bolt_transform = topology1_bolt_transform[0:min_length]
        topology1_bolt_output_sink = topology1_bolt_output_sink[0:min_length]
        topology1_bolt_join = topology1_bolt_join[0:min_length]
        topology1_bolt_filter = topology1_bolt_filter[0:min_length]
        topology1_bolt_filter_2 = topology1_bolt_filter_2[0:min_length]

  #      topology2_bolt_aggregate = topology2_bolt_aggregate[0:min_length]
  #      topology2_spout = topology2_spout[0:min_length]
  #      topology2_bolt_transform = topology2_bolt_transform[0:min_length]
  #      topology2_bolt_output_sink = topology2_bolt_output_sink[0:min_length]
  #      topology2_bolt_join = topology2_bolt_join[0:min_length]
  #      topology2_bolt_filter = topology2_bolt_filter[0:min_length]
  #      topology2_bolt_filter_2 = topology2_bolt_filter_2[0:min_length]
       #
       #  topology3_bolt_aggregate = topology3_bolt_aggregate[0:min_length]
       # # topology3_spout = topology3_spout[0:min_length]
       #  topology3_bolt_transform = topology3_bolt_transform[0:min_length]
       #  topology3_bolt_output_sink = topology3_bolt_output_sink[0:min_length]
       #  topology3_bolt_join = topology3_bolt_join[0:min_length]
       #  topology3_bolt_filter = topology3_bolt_filter[0:min_length]
       #  topology3_bolt_filter_2 = topology3_bolt_filter_2[0:min_length]
       #
       #  topology4_bolt_aggregate = topology4_bolt_aggregate[0:min_length]
       # # topology4_spout = topology4_spout[0:min_length]
       #  topology4_bolt_transform = topology4_bolt_transform[0:min_length]
       #  topology4_bolt_output_sink = topology4_bolt_output_sink[0:min_length]
       #  topology4_bolt_join = topology4_bolt_join[0:min_length]
       #  topology4_bolt_filter = topology4_bolt_filter[0:min_length]
       #  topology4_bolt_filter_2 = topology4_bolt_filter_2[0:min_length]

        val = time[0]
        for i in range(0, len(time)):
            time[i] = (time[i] - val)/1000
        # D > s
        fig, ax = plt.subplots()
        print topology1_bolt_aggregate
        print time
        ax.scatter(time, topology1_bolt_aggregate, edgecolors ="blue", label="Capacity of congested bolt", marker ="s", facecolors='none', s=10,)

        ax.set_xlabel('Time/S', fontsize=10)
        ax.set_ylabel('Capacity', fontsize=10)

        ax.grid(True)
        fig.tight_layout()

        lines, labels = ax.get_legend_handles_labels()
        ax.legend(lines, labels, loc=9, bbox_to_anchor=(0.5, -0.1), ncol=2,prop={'size':10})

        plt.xlim(0,23000)
        ax.set_ylim(0, 1.5)

        plt.savefig(filename+'-aggregate-topology1-capacity.png', bbox_inches='tight')

        fig, ax = plt.subplots()
        ax.scatter(time, topology1_bolt_filter_2, edgecolors ="black", label="Capacity of congested bolt", marker="s", facecolors='none', s=10,)

        ax.set_xlabel('Time/S', fontsize=10)
        ax.set_ylabel('Capacity', fontsize=10)

        ax.grid(True)
        fig.tight_layout()

        lines, labels = ax.get_legend_handles_labels()
        ax.legend(lines, labels, loc=9, bbox_to_anchor=(0.5, -0.1), ncol=2,prop={'size':10})

        plt.xlim(0,11000)
        ax.set_ylim(-1.0, 3.0)

        plt.savefig(filename+'-filter2-topology1-capacity.png', bbox_inches='tight')


      #   fig, ax = plt.subplots()
      #   ax.scatter(time, topology2_spout, edgecolors ="green", label="T2 spout", marker ="s", facecolors='none', s=10,)
      #
      #   ax.set_xlabel('Time/S', fontsize=10)
      #   ax.set_ylabel('Capacity', fontsize=10)
      #
      #   ax.grid(True)
      #   fig.tight_layout()
      #
      #   lines, labels = ax.get_legend_handles_labels()
      #   ax.legend(lines, labels, loc=9, bbox_to_anchor=(0.5, -0.1), ncol=2,prop={'size':10})
      #
      #   plt.xlim(0,11000)
      #   ax.set_ylim(-1.0, 2.0)
      #
      #   plt.savefig(filename+'-spout-topology2-capacity.png', bbox_inches='tight')
      #
      #   fig, ax = plt.subplots()
      #   ax.scatter(time, topology2_bolt_transform, edgecolors ="darkorange", label="T2 bolt_transform", marker="s", facecolors='none', s=10,)
      #
      #   ax.set_xlabel('Time/S', fontsize=10)
      #   ax.set_ylabel('Capacity', fontsize=10)
      #
      #   ax.grid(True)
      #   fig.tight_layout()
      #
      #   lines, labels = ax.get_legend_handles_labels()
      #   ax.legend(lines, labels, loc=9, bbox_to_anchor=(0.5, -0.1), ncol=2,prop={'size':10})
      #
      #   plt.xlim(0,11000)
      #   ax.set_ylim(-1.0, 2.0)
      #
      #   plt.savefig(filename+'-transform-topology2-capacity.png', bbox_inches='tight')
      #
      #   fig, ax = plt.subplots()
      #   ax.scatter(time, topology2_bolt_output_sink, edgecolors ="darkorange", label="T2 bolt_output_sink", marker="s", facecolors='none', s=10,)
      #
      #   ax.set_xlabel('Time/S', fontsize=10)
      #   ax.set_ylabel('Capacity', fontsize=10)
      #
      #   ax.grid(True)
      #   fig.tight_layout()
      #
      #   lines, labels = ax.get_legend_handles_labels()
      #   ax.legend(lines, labels, loc=9, bbox_to_anchor=(0.5, -0.1), ncol=2,prop={'size':10})
      #
      #   plt.xlim(0,11000)
      #   ax.set_ylim(-1.0, 2.0)
      #
      #   plt.savefig(filename+'-output-topology2-capacity.png', bbox_inches='tight')
      #
      #   fig, ax = plt.subplots()
      #   ax.scatter(time, topology2_bolt_join, edgecolors ="pink", label="T2 bolt_join", marker="s", facecolors='none', s=10,)
      #
      #   ax.set_xlabel('Time/S', fontsize=10)
      #   ax.set_ylabel('Capacity', fontsize=10)
      #
      #   ax.grid(True)
      #   fig.tight_layout()
      #
      #   lines, labels = ax.get_legend_handles_labels()
      #   ax.legend(lines, labels, loc=9, bbox_to_anchor=(0.5, -0.1), ncol=2,prop={'size':10})
      #
      #   plt.xlim(0,11000)
      #   ax.set_ylim(-1.0, 2.0)
      #
      #   plt.savefig(filename+'-join-topology2-capacity.png', bbox_inches='tight')
      #
      #   fig, ax = plt.subplots()
      #   ax.scatter(time, topology2_bolt_filter, edgecolors ="yellow", label="T2 bolt_filter", marker="s", facecolors='none', s=10,)
      #
      #   ax.set_xlabel('Time/S', fontsize=10)
      #   ax.set_ylabel('Capacity', fontsize=10)
      #
      #   ax.grid(True)
      #   fig.tight_layout()
      #
      #   lines, labels = ax.get_legend_handles_labels()
      #   ax.legend(lines, labels, loc=9, bbox_to_anchor=(0.5, -0.1), ncol=2,prop={'size':10})
      #
      #   plt.xlim(0,11000)
      #   ax.set_ylim(-1.0, 2.0)
      #
      #   plt.savefig(filename+'-filter-topology2-capacity.png', bbox_inches='tight')
      #
      #   fig, ax = plt.subplots()
      #   ax.scatter(time, topology2_bolt_filter_2, edgecolors ="black", label="T2 bolt_filter_2", marker="s", facecolors='none', s=10,)
      #
      #   ax.set_xlabel('Time/S', fontsize=10)
      #   ax.set_ylabel('Capacity', fontsize=10)
      #
      #   ax.grid(True)
      #   fig.tight_layout()
      #
      #   lines, labels = ax.get_legend_handles_labels()
      #   ax.legend(lines, labels, loc=9, bbox_to_anchor=(0.5, -0.1), ncol=2,prop={'size':10})
      #
      #   plt.xlim(0,11000)
      # #  ax.set_ylim(-1.0, 3.0)
      #
      #   plt.savefig(filename+'-filter2-topology2-capacity.png', bbox_inches='tight')

        # fig, ax = plt.subplots()
        # ax.scatter(time, topology2_bolt_aggregate, edgecolors ="blue", label="T2 Latency SLO=50 bolt_aggregate", marker ="D", facecolors='none', s=40,)
        # #ax.scatter(time, topology2_spout, edgecolors ="green", label="T2 spout", marker ="D", facecolors='none', s=40,)
        # ax.scatter(time, topology2_bolt_transform, edgecolors ="red", label="T2 bolt_transform", marker="D", facecolors='none', s=40, )
        # ax.scatter(time, topology2_bolt_output_sink, edgecolors ="darkorange", label="T2 bolt_output_sink", marker="D", facecolors='none', s=40,)
        # ax.scatter(time, topology2_bolt_join, edgecolors ="pink", label="T2 bolt_join", marker="D", facecolors='none', s=40,)
        # ax.scatter(time, topology2_bolt_filter, edgecolors ="yellow", label="T2 bolt_filter", marker="D", facecolors='none', s=40,)
        # ax.scatter(time, topology2_bolt_filter_2, edgecolors ="black", label="T2 bolt_filter_2", marker="D", facecolors='none', s=40,)
        #
        # ax.set_xlabel('Time/S', fontsize=10)
        # ax.set_ylabel('ETP', fontsize=10)
        #
        # ax.grid(True)
        # fig.tight_layout()
        #
        # lines, labels = ax.get_legend_handles_labels()
        # ax.legend(lines, labels, loc=9, bbox_to_anchor=(0.5, -0.1), ncol=2,prop={'size':10})
        #
        # plt.xlim(0,50000)
        # ax.set_ylim(0.0, 1.1)
        #
        # plt.savefig(filename+'topology2.png', bbox_inches='tight')
        #
        # fig, ax = plt.subplots()
        # ax.scatter(time, topology3_bolt_aggregate, edgecolors ="blue", label="T3 Juice = 1 bolt_aggregate", marker =">", facecolors='none', s=40,)
        # #ax.scatter(time, topology3_spout, edgecolors ="green", label="T3 spout", marker =">", facecolors='none', s=40,)
        # ax.scatter(time, topology3_bolt_transform, edgecolors ="red", label="T3 bolt_transform", marker=">", facecolors='none', s=40, )
        # ax.scatter(time, topology3_bolt_output_sink, edgecolors ="darkorange", label="T3 bolt_output_sink", marker=">", facecolors='none', s=40,)
        # ax.scatter(time, topology3_bolt_join, edgecolors ="pink", label="T3 bolt_join" , marker=">", facecolors='none', s=40,)
        # ax.scatter(time, topology3_bolt_filter, edgecolors ="yellow", label="T3 bolt_filter", marker=">", facecolors='none', s=40,)
        # ax.scatter(time, topology3_bolt_filter_2, edgecolors ="black", label="T3 bolt_filter_2", marker=">", facecolors='none', s=40,)
        #
        # ax.set_xlabel('Time/S', fontsize=10)
        # ax.set_ylabel('ETP', fontsize=10)
        #
        # ax.grid(True)
        # fig.tight_layout()
        #
        # lines, labels = ax.get_legend_handles_labels()
        # ax.legend(lines, labels, loc=9, bbox_to_anchor=(0.5, -0.1), ncol=2,prop={'size':10})
        #
        # plt.xlim(0,30000)
        # ax.set_ylim(0.0, 1.1)
        #
        # plt.savefig(filename+'topology3.png', bbox_inches='tight')
        #
        # fig, ax = plt.subplots()
        # ax.scatter(time, topology4_bolt_aggregate, edgecolors ="blue", label="T4 Juice = 1 bolt_aggregate", marker ="+", facecolors='none', s=40,)
        # #ax.scatter(time, topology4_spout, edgecolors ="green", label="T4 spout", marker ="+", facecolors='none', s=40,)
        # ax.scatter(time, topology4_bolt_transform, edgecolors ="red", label="T4 bolt_transform", marker="+", facecolors='none', s=40, )
        # ax.scatter(time, topology4_bolt_output_sink, edgecolors ="darkorange", label="T4 bolt_output_sink", marker="+", facecolors='none', s=40,)
        # ax.scatter(time, topology4_bolt_join, edgecolors ="pink", label="T4 bolt_join", marker="+", facecolors='none', s=40,)
        # ax.scatter(time, topology4_bolt_filter, edgecolors ="yellow", label="T4 bolt_filter", marker="+", facecolors='none', s=40,)
        # ax.scatter(time, topology4_bolt_filter_2, edgecolors ="black", label="T4 bolt_filter_2", marker="+", facecolors='none', s=40,)
        #
        #
        #
        # ax.set_xlabel('Time/S', fontsize=10)
        # ax.set_ylabel('ETP', fontsize=10)
        #
        # ax.grid(True)
        # fig.tight_layout()
        #
        # lines, labels = ax.get_legend_handles_labels()
        # ax.legend(lines, labels, loc=9, bbox_to_anchor=(0.5, -0.1), ncol=2,prop={'size':10})
        #
        # plt.xlim(0,30000)
        # ax.set_ylim(0.0, 1.1)
        #
        # plt.savefig(filename+'topology4.png', bbox_inches='tight')