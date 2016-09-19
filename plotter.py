import os

import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

flag = 0
for i in os.listdir("."):
    if i.endswith(".log") :
        f = open(""+i, 'r')
        filename = f.__getattribute__("name").split(".")[0]
        print filename
        topology1_juice = []
        topology2_juice = []
        topology3_juice = []
        topology4_juice = []
        topology1_latency = []
        topology2_latency = []
        topology3_latency = []
        topology4_latency = []
        input_at_source_1 = []
        output_at_sink_1 = []
        input_at_source_2 = []
        output_at_sink_2 = []
        input_at_source_3 = []
        output_at_sink_3 = []
        input_at_source_4 = []
        output_at_sink_4 = []
        time = []
        target = []
        target_operator = []
        victim_operator = []
        victim = []
        rebalance_time = []
        latency_index = 3
        name_index = 0
        juice_index = 2
        input_index = 4
        output_index = 5
        time_index = 6

        for line in f:
                line = line.split("\n")[0]
                one_line = line.split(',')
                if "/var/nimbus/storm" not in one_line[name_index] and len(one_line) > 1:
                    if "production-topology1"  in one_line[name_index]:
                        topology1_juice.append(float(one_line[juice_index]))
                        topology1_latency.append(float(one_line[latency_index]))
                        input_at_source_1.append(float(one_line[input_index]))
                        output_at_sink_1.append(float(one_line[output_index]))
                    elif "production-topology2"  in one_line[name_index]:
                        topology2_juice.append(float(one_line[juice_index]))
                        topology2_latency.append(float(one_line[latency_index]))
                        time.append(float(one_line[time_index]))
                        input_at_source_2.append(float(one_line[input_index]))
                        output_at_sink_2.append(float(one_line[output_index]))
                    elif "production-topology3"  in one_line[name_index]:
                        topology3_juice.append(float(one_line[juice_index]))
                        input_at_source_3.append(float(one_line[input_index]))
                        topology3_latency.append(float(one_line[latency_index]))
                        output_at_sink_3.append(float(one_line[output_index]))
                    elif "production-topology4"  in one_line[name_index]:
                        topology4_juice.append(float(one_line[juice_index]))
                        input_at_source_4.append(float(one_line[input_index]))
                        topology4_latency.append(float(one_line[latency_index]))
                        output_at_sink_4.append(float(one_line[output_index]))
                    elif len(one_line) == 1 and "Running" not in one_line[0] and is_number(one_line[0]):
                        rebalance_time.append(float(one_line[0]))
                elif "/var/nimbus/storm" in one_line[0] :
                    time_for_rebalance = line.split(" ")
                    if "Running" not in line:
                        if flag == 0:
                            target.append(time_for_rebalance[2])
                            target_operator.append(time_for_rebalance[4])
                            flag = 1
                        else:
                            victim.append(time_for_rebalance[2])
                            victim_operator.append(time_for_rebalance[4])
                            flag = 0
                elif len(one_line) == 1 and is_number(one_line[0]):
                    rebalance_time.append(float(one_line[0]))


        val = time[0]
        for i in range(0, len(time)):
            time[i] = (time[i] - val)/1000
        for i in range(0, len(rebalance_time)):
            rebalance_time[i] = (rebalance_time[i] - val)/1000
        min_length = len(time)
        if min_length > len(topology1_juice):
            min_length = len(topology1_juice)
        if min_length > len(topology2_juice):
            min_length = len(topology2_juice)
        if min_length > len(topology3_juice):
            min_length = len(topology3_juice)
        if min_length > len(topology4_juice):
            min_length = len(topology4_juice)
        if min_length > len(topology1_latency):
            min_length = len(topology1_latency)
        if min_length > len(topology2_latency):
            min_length = len(topology2_latency)
        if min_length > len(topology3_latency):
            min_length = len(topology3_latency)
        if min_length > len(topology4_latency):
            min_length = len(topology4_latency)

        time = time[0:min_length]
        topology1_juice = topology1_juice [0:min_length]
        topology2_juice = topology2_juice [0:min_length]
        topology3_juice = topology3_juice [0:min_length]
        topology4_juice = topology4_juice [0:min_length]

        topology1_latency = topology1_latency [0:min_length]
        topology2_latency = topology2_latency [0:min_length]
        topology3_latency = topology3_latency [0:min_length]
        topology4_latency = topology4_latency [0:min_length]

        input_at_source_1 = input_at_source_1[0:min_length]
        output_at_sink_1 = output_at_sink_1[0:min_length]
        input_at_source_2 = input_at_source_2[0:min_length]
        output_at_sink_2 = output_at_sink_2[0:min_length]
        input_at_source_3 = input_at_source_3[0:min_length]
        output_at_sink_3 = output_at_sink_3[0:min_length]
        input_at_source_4 = input_at_source_4[0:min_length]
        output_at_sink_4 = output_at_sink_4[0:min_length]

        fig, ax = plt.subplots()
        ax.scatter(time, topology1_juice, edgecolors ="blue", label="T1 SLO=1", marker ="D", facecolors='none', s=40,)
        ax.scatter(time, topology2_juice, edgecolors ="green", label="T2 SLO=0.2", marker =">", facecolors='none', s=40,)
        ax.scatter(time, topology3_juice, edgecolors ="red", label="T3 SLO=1", marker="h", facecolors='none', s=40, )
        ax.scatter(time, topology4_juice, edgecolors ="darkorange", label="T4 SLO=0.4", marker="s", facecolors='none', s=40,)

        ax2 = ax.twinx()
        ax2.scatter(time, topology1_latency, edgecolors ="black", label="T1 Latency", marker ="*", facecolors='none', s=40,)
        ax2.scatter(time, topology2_latency, edgecolors ="pink", label="T2 Latency", marker ="<", facecolors='none', s=40,)
        ax2.scatter(time, topology3_latency, edgecolors ="purple", label="T3 Latency", marker="D", facecolors='none', s=40, )
        ax2.scatter(time, topology4_latency, edgecolors ="yellow", label="T4 Latency", marker="+", facecolors='none', s=40,)

        ax.set_xlabel('Time/S', fontsize=10)
        ax.set_ylabel('Juice', fontsize=10)
        ax2.set_ylabel('Latency/S', fontsize=10)
        ax.grid(True)
        fig.tight_layout()

        plt.vlines(x=600, ymax=5 , ymin=-1, label="Ten Minute Mark", colors='blue')

        #linestyles = [ '--' , '--' , 'solid', 'dotted']
        linestyles = [ '--' , '--', '--', '--']
        for j in range(0, len(rebalance_time)):
            la = target[j] + " " + target_operator[j] + " " + victim[j] + " " + victim_operator[j]
            ax.vlines(x=rebalance_time[j], ymax=5 , ymin=-1,  colors='black', linestyle=linestyles[j%4]) #label=la,label="rebalance "+str(j+1),label="rebalance "+str(j+1),
        #ax.legend(loc=9, bbox_to_anchor=(0.5, -0.1), ncol=5,prop={'size':10})
        #ax2.legend(loc=10, bbox_to_anchor=(0.5, -0.1), ncol=5,prop={'size':10})


        lines, labels = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax2.legend(lines + lines2, labels + labels2, loc=9, bbox_to_anchor=(0.5, -0.1), ncol=5,prop={'size':10})

        plt.xlim(-10,1900)
        ax.set_ylim(-0.01,1.1)
        ax2.set_ylim(10,100)


      #  axins = zoomed_inset_axes(ax,  2.5, loc=1)
      #  axins.scatter(time, topology1_juice, edgecolors ="blue", label="T1", marker ="D", facecolors='none', s=40, )
      #  axins.scatter(time, topology2_juice, edgecolors ="green", label="T2", marker =">", facecolors='none', s=40, )
      #  axins.scatter(time, topology3_juice, edgecolors ="red", label="T3", marker="h", facecolors='none', s=40, )
      #  axins.scatter(time, topology4_juice, edgecolors ="darkorange", label="T4", marker="s", facecolors='none', s=40, )
      #  axins.vlines(x=600, ymax=5 , ymin=-1, label="Ten Minute Mark", colors='blue')

      #  for j in range(0, len(rebalance_time)):
      #      la = target[j] + " " + target_operator[j] + " " + victim[j] + " " + victim_operator[j]
      #      axins.vlines(x=rebalance_time[j], ymax=5 , ymin=-1,  colors='black', linestyle=linestyles[j%4]) #label=la,label="rebalance " + str(j+1),


      #  x1, x2, y1, y2 = 590, 1300, 0.8, 1.2 # specify the limits
      #  axins.set_xlim(x1, x2) # apply the x-limits
      #  axins.set_ylim(y1, y2) # apply the y-limits
      #  mark_inset(ax, axins, loc1=3, loc2=4, fc="none", ec="0.5")


        plt.savefig(filename+'.png', bbox_inches='tight')

        fig, ax = plt.subplots()
        ax.scatter(time, input_at_source_1, edgecolors = "chocolate", label= "T1 input", facecolor='none', marker = "D", s=40)
        ax.scatter(time, output_at_sink_1, edgecolors = "black", label= "T1 output" ,facecolor='none', marker = "+", s=40)
        ax.scatter(time, input_at_source_2, edgecolors = "red", label= "T2 input",facecolor='none', marker = ">", s=40)
        ax.scatter(time, output_at_sink_2, edgecolors = "blue", label= "T2 output" ,facecolor='none', marker = "<",s=40)
        ax.scatter(time, input_at_source_3, edgecolors = "teal", label= "T3 input", facecolor='none', marker = "x",s=40)
        ax.scatter(time, output_at_sink_3, edgecolors = "green", label= "T3 output", facecolor='none', marker = "h", s=40)
        ax.scatter(time, input_at_source_4, edgecolors = "purple", label= "T4 input", facecolor='none',marker = "v" , s=40)
        ax.scatter(time, output_at_sink_4, edgecolors = "magenta", label= "T4 output" , facecolor='none', marker = "s", s=40)


        for j in range(0, len(rebalance_time)):
            la = target[j] + " " + target_operator[j] + " " + victim[j] + " " + victim_operator[j]
            ax.vlines(x=rebalance_time[j], ymax=5000 , ymin=-1,  colors='black', linestyle=linestyles[j%4]) #label=la,label="rebalance " + str(j+1),

        ax.set_xlabel('Time/S', fontsize=10)
        ax.set_ylabel('Number of Tuples', fontsize=10)



        ax.grid(True)
        fig.tight_layout()
        plt.vlines(x=600, ymax=5000 , ymin=-1, label="Ten Minute Mark", colors='blue')
        plt.legend(loc=9, bbox_to_anchor=(0.5, -0.1), ncol=5,prop={'size':10})
        plt.xlim(-10,1900)
        plt.ylim(-1,5000)
        plt.savefig(filename+"+tuples"+'.png', bbox_inches='tight')