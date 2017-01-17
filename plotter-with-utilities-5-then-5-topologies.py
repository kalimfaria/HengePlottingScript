import os

import matplotlib.pyplot as plt
import numpy


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def movingaverage(interval, window_size):
    window = numpy.ones(int(window_size)) / float(window_size)
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
for i in os.listdir("/Users/fariakalim/exp113/"):
    if i.endswith("output.log"):
        f = open("/Users/fariakalim/exp113/" + i, 'r')
        filename = f.__getattribute__("name").split(".")[0]

        topology1_juice = []
        topology2_juice = []
        topology3_juice = []
        topology4_juice = []
        topology5_juice = []
        topology6_juice = []
        topology7_juice = []
        topology8_juice = []
        topology9_juice = []
        topology10_juice = []
        topology11_juice = []
        topology12_juice = []
        topology13_juice = []
        topology14_juice = []
        topology15_juice = []

        topology1_latency = []
        topology2_latency = []
        topology3_latency = []
        topology4_latency = []
        topology5_latency = []
        topology6_latency = []
        topology7_latency = []
        topology8_latency = []
        topology9_latency = []
        topology10_latency = []
        topology11_latency = []
        topology12_latency = []
        topology13_latency = []
        topology14_latency = []
        topology15_latency = []

        topology1_utility = []
        topology2_utility = []
        topology3_utility = []
        topology4_utility = []
        topology5_utility = []
        topology6_utility = []
        topology7_utility = []
        topology8_utility = []
        topology9_utility = []
        topology10_utility = []
        topology11_utility = []
        topology12_utility = []
        topology13_utility = []
        topology14_utility = []
        topology15_utility = []

        topology1_99tail_latency = []
        topology2_99tail_latency = []
        topology3_99tail_latency = []
        topology4_99tail_latency = []
        topology5_99tail_latency = []
        topology6_99tail_latency = []
        topology7_99tail_latency = []
        topology8_99tail_latency = []
        topology9_99tail_latency = []
        topology10_99tail_latency = []
        topology11_99tail_latency = []
        topology12_99tail_latency = []
        topology13_99tail_latency = []
        topology14_99tail_latency = []
        topology15_99tail_latency = []

        topology1_75tail_latency = []
        topology2_75tail_latency = []
        topology3_75tail_latency = []
        topology4_75tail_latency = []
        topology5_75tail_latency = []
        topology6_75tail_latency = []
        topology7_75tail_latency = []
        topology8_75tail_latency = []
        topology9_75tail_latency = []
        topology10_75tail_latency = []
        topology11_75tail_latency = []
        topology12_75tail_latency = []
        topology13_75tail_latency = []
        topology14_75tail_latency = []
        topology15_75tail_latency = []

        topology1_50tail_latency = []
        topology2_50tail_latency = []
        topology3_50tail_latency = []
        topology4_50tail_latency = []
        topology5_50tail_latency = []
        topology6_50tail_latency = []
        topology7_50tail_latency = []
        topology8_50tail_latency = []
        topology9_50tail_latency = []
        topology10_50tail_latency = []
        topology11_50tail_latency = []
        topology12_50tail_latency = []
        topology13_50tail_latency = []
        topology14_50tail_latency = []
        topology15_50tail_latency = []

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
        input_at_source_7 = []
        output_at_sink_7 = []
        input_at_source_8 = []
        output_at_sink_8 = []
        input_at_source_9 = []
        output_at_sink_9 = []
        input_at_source_10 = []
        output_at_sink_10 = []
        input_at_source_11 = []
        output_at_sink_11 = []
        input_at_source_12 = []
        output_at_sink_12 = []
        input_at_source_13 = []
        output_at_sink_13 = []
        input_at_source_14 = []
        output_at_sink_14 = []
        input_at_source_15 = []
        output_at_sink_15 = []

        time = []
        target = []
        target_operator = []
        victim_operator = []
        victim = []
        rebalance_time = []
        rebalance_desc = []

        name_index = 0
        juice_index = 1
        latency_index = 3
        current_utility_index = 4
        specified_utility_index = 5
        tail99__latency_index = 6
        tail75__latency_index = 7
        tail50__latency_index = 8

        input_index = 9
        output_index = 10
        time_index = 11

        for line in f:
            line = line.split("\n")[0]
            one_line = line.split(',')
            if "/var/nimbus/storm" not in one_line[name_index] and len(one_line) > 1:
                if "production-topology1-" in one_line[name_index]:
                    topology1_juice.append(float(one_line[juice_index]))
                    topology1_utility.append(float(one_line[current_utility_index]))
                    topology1_latency.append(float(one_line[latency_index]))
                    input_at_source_1.append(float(one_line[input_index]))
                    output_at_sink_1.append(float(one_line[output_index]))
                    topology1_99tail_latency.append(float(one_line[tail99__latency_index]))
                    topology1_75tail_latency.append(float(one_line[tail75__latency_index]))
                    topology1_50tail_latency.append(float(one_line[tail50__latency_index]))
                elif "production-topology2-" in one_line[name_index]:
                    topology2_juice.append(float(one_line[juice_index]))
                    topology2_latency.append(float(one_line[latency_index]))
                    topology2_utility.append(float(one_line[current_utility_index]))
                    input_at_source_2.append(float(one_line[input_index]))
                    output_at_sink_2.append(float(one_line[output_index]))
                    topology2_99tail_latency.append(float(one_line[tail99__latency_index]))
                    topology2_75tail_latency.append(float(one_line[tail75__latency_index]))
                    topology2_50tail_latency.append(float(one_line[tail50__latency_index]))
                elif "production-topology3-" in one_line[name_index]:
                    time.append(float(one_line[time_index]))
                    topology3_juice.append(float(one_line[juice_index]))
                    input_at_source_3.append(float(one_line[input_index]))
                    topology3_latency.append(float(one_line[latency_index]))
                    topology3_utility.append(float(one_line[current_utility_index]))
                    output_at_sink_3.append(float(one_line[output_index]))
                    topology3_99tail_latency.append(float(one_line[tail99__latency_index]))
                    topology3_75tail_latency.append(float(one_line[tail75__latency_index]))
                    topology3_50tail_latency.append(float(one_line[tail50__latency_index]))
                elif "production-topology4" in one_line[name_index]:
                    topology4_juice.append(float(one_line[juice_index]))
                    topology4_99tail_latency.append(float(one_line[tail99__latency_index]))
                    topology4_75tail_latency.append(float(one_line[tail75__latency_index]))
                    topology4_50tail_latency.append(float(one_line[tail50__latency_index]))
                    topology4_utility.append(float(one_line[current_utility_index]))
                    input_at_source_4.append(float(one_line[input_index]))
                    topology4_latency.append(float(one_line[latency_index]))
                    output_at_sink_4.append(float(one_line[output_index]))
                elif "production-topology5" in one_line[name_index]:
                    topology5_juice.append(float(one_line[juice_index]))
                    topology5_utility.append(float(one_line[current_utility_index]))
                    input_at_source_5.append(float(one_line[input_index]))
                    topology5_99tail_latency.append(float(one_line[tail99__latency_index]))
                    topology5_75tail_latency.append(float(one_line[tail75__latency_index]))
                    topology5_50tail_latency.append(float(one_line[tail50__latency_index]))
                    topology5_latency.append(float(one_line[latency_index]))
                    output_at_sink_5.append(float(one_line[output_index]))
                elif "production-topology6" in one_line[name_index]:
                    topology6_juice.append(float(one_line[juice_index]))
                    topology6_utility.append(float(one_line[current_utility_index]))
                    input_at_source_6.append(float(one_line[input_index]))
                    topology6_latency.append(float(one_line[latency_index]))
                    output_at_sink_6.append(float(one_line[output_index]))
                    topology6_99tail_latency.append(float(one_line[tail99__latency_index]))
                    topology6_75tail_latency.append(float(one_line[tail75__latency_index]))
                    topology6_50tail_latency.append(float(one_line[tail50__latency_index]))
                elif "production-topology7" in one_line[name_index]:
                    topology7_juice.append(float(one_line[juice_index]))
                    topology7_utility.append(float(one_line[current_utility_index]))
                    input_at_source_7.append(float(one_line[input_index]))
                    topology7_99tail_latency.append(float(one_line[tail99__latency_index]))
                    topology7_75tail_latency.append(float(one_line[tail75__latency_index]))
                    topology7_50tail_latency.append(float(one_line[tail50__latency_index]))
                    topology7_latency.append(float(one_line[latency_index]))
                    output_at_sink_7.append(float(one_line[output_index]))
                elif "production-topology8" in one_line[name_index]:
                    topology8_juice.append(float(one_line[juice_index]))
                    topology8_utility.append(float(one_line[current_utility_index]))
                    input_at_source_8.append(float(one_line[input_index]))
                    topology8_latency.append(float(one_line[latency_index]))
                    output_at_sink_8.append(float(one_line[output_index]))
                    topology8_99tail_latency.append(float(one_line[tail99__latency_index]))
                    topology8_75tail_latency.append(float(one_line[tail75__latency_index]))
                    topology8_50tail_latency.append(float(one_line[tail50__latency_index]))
                elif "production-topology9" in one_line[name_index]:
                    topology9_juice.append(float(one_line[juice_index]))
                    topology9_utility.append(float(one_line[current_utility_index]))
                    input_at_source_9.append(float(one_line[input_index]))
                    topology9_latency.append(float(one_line[latency_index]))
                    output_at_sink_9.append(float(one_line[output_index]))
                    topology9_99tail_latency.append(float(one_line[tail99__latency_index]))
                    topology9_75tail_latency.append(float(one_line[tail75__latency_index]))
                    topology9_50tail_latency.append(float(one_line[tail50__latency_index]))
                elif "production-topology10-" in one_line[name_index]:
                    topology10_juice.append(float(one_line[juice_index]))
                    topology10_utility.append(float(one_line[current_utility_index]))
                    topology10_99tail_latency.append(float(one_line[tail99__latency_index]))
                    topology10_75tail_latency.append(float(one_line[tail75__latency_index]))
                    topology10_50tail_latency.append(float(one_line[tail50__latency_index]))
                    input_at_source_10.append(float(one_line[input_index]))
                    topology10_latency.append(float(one_line[latency_index]))
                    output_at_sink_10.append(float(one_line[output_index]))
                elif "production-topology11-" in one_line[name_index]:
                    topology11_juice.append(float(one_line[juice_index]))
                    topology11_utility.append(float(one_line[current_utility_index]))
                    topology11_99tail_latency.append(float(one_line[tail99__latency_index]))
                    topology11_75tail_latency.append(float(one_line[tail75__latency_index]))
                    topology11_50tail_latency.append(float(one_line[tail50__latency_index]))
                    input_at_source_11.append(float(one_line[input_index]))
                    topology11_latency.append(float(one_line[latency_index]))
                    output_at_sink_11.append(float(one_line[output_index]))
                elif "production-topology12-" in one_line[name_index]:
                    topology12_juice.append(float(one_line[juice_index]))
                    topology12_utility.append(float(one_line[current_utility_index]))
                    topology12_99tail_latency.append(float(one_line[tail99__latency_index]))
                    topology12_75tail_latency.append(float(one_line[tail75__latency_index]))
                    topology12_50tail_latency.append(float(one_line[tail50__latency_index]))
                    input_at_source_12.append(float(one_line[input_index]))
                    topology12_latency.append(float(one_line[latency_index]))
                    output_at_sink_12.append(float(one_line[output_index]))
                elif "production-topology13-" in one_line[name_index]:
                    topology13_juice.append(float(one_line[juice_index]))
                    topology13_utility.append(float(one_line[current_utility_index]))
                    topology13_99tail_latency.append(float(one_line[tail99__latency_index]))
                    topology13_75tail_latency.append(float(one_line[tail75__latency_index]))
                    topology13_50tail_latency.append(float(one_line[tail50__latency_index]))
                    input_at_source_13.append(float(one_line[input_index]))
                    topology13_latency.append(float(one_line[latency_index]))
                    output_at_sink_13.append(float(one_line[output_index]))
                elif "production-topology14-" in one_line[name_index]:
                    topology14_juice.append(float(one_line[juice_index]))
                    topology14_utility.append(float(one_line[current_utility_index]))
                    topology14_99tail_latency.append(float(one_line[tail99__latency_index]))
                    topology14_75tail_latency.append(float(one_line[tail75__latency_index]))
                    topology14_50tail_latency.append(float(one_line[tail50__latency_index]))
                    input_at_source_14.append(float(one_line[input_index]))
                    topology14_latency.append(float(one_line[latency_index]))
                    output_at_sink_14.append(float(one_line[output_index]))
                elif "production-topology15-" in one_line[name_index]:
                    topology15_juice.append(float(one_line[juice_index]))
                    topology15_utility.append(float(one_line[current_utility_index]))
                    topology15_99tail_latency.append(float(one_line[tail99__latency_index]))
                    topology15_75tail_latency.append(float(one_line[tail75__latency_index]))
                    topology15_50tail_latency.append(float(one_line[tail50__latency_index]))
                    input_at_source_15.append(float(one_line[input_index]))
                    topology15_latency.append(float(one_line[latency_index]))
                    output_at_sink_15.append(float(one_line[output_index]))
                elif len(one_line) == 1 and "Running" not in one_line[0] and is_number(one_line[0]):
                    rebalance_time.append(float(one_line[0]))
            elif "/var/nimbus/storm" in one_line[0]:
                time_for_rebalance = line.split(" ")
                if "-n" not in line:
                    if flag == 0:
                        string = ""

                        if time_for_rebalance[2] == "production-topology10":
                            string = "T10"
                        elif time_for_rebalance[2] == "production-topology11":
                            string = "T11"
                        elif time_for_rebalance[2] == "production-topology2":
                            string = "T2"
                        elif time_for_rebalance[2] == "production-topology3":
                            string = "T3"
                        elif time_for_rebalance[2] == "production-topology12":
                            string = "T12"
                        elif time_for_rebalance[2] == "production-topology13":
                            string = "T13"
                        elif time_for_rebalance[2] == "production-topology14":
                            string = "T14"
                        elif time_for_rebalance[2] == "production-topology15":
                            string = "T15"
                        elif time_for_rebalance[2] == "production-topology4":
                            string = "T4"
                        elif time_for_rebalance[2] == "production-topology5":
                            string = "T5"
                        elif time_for_rebalance[2] == "production-topology6":
                            string = "T6"
                        elif time_for_rebalance[2] == "production-topology7":
                            string = "T7"
                        elif time_for_rebalance[2] == "production-topology8":
                            string = "T8"
                        elif time_for_rebalance[2] == "production-topology9":
                            string = "T9"
                        elif time_for_rebalance[2] == "production-topology1":
                            string = "T1"
                        else:
                            string = time_for_rebalance[2]

                        # if (len(time_for_rebalance) > 6): # TODO -- GET RID OF IT
                        str = string + " " + time_for_rebalance[6]
                        # rebalance_desc.append(string + " "+ time_for_rebalance[6]) # should give topology name space num workers
                        i = 7
                        while len(time_for_rebalance) > i:
                            str = str + " " + time_for_rebalance[i]  # should give topology name space num workers
                            i = i + 1
                        rebalance_desc.append(str)

                        # desc_string = " ".join((time_for_rebalance[2] , time_for_rebalance[6]))

                        # rebalance_desc.append(desc_string) # get rid of this if you have multiple rebalances
                        #       flag = 1
                        #   else:
                        #       temp = " ".join((time_for_rebalance[2], time_for_rebalance[6]))
                        #       desc_string = " ".join((desc_string,temp))
                        #       rebalance_desc.append(desc_string)
                        #       desc_string = " "
                        #       flag = 0
                else:
                    if time_for_rebalance[2] == "production-topology10":
                        rebalance_desc.append("T10")
                    elif time_for_rebalance[2] == "production-topology11":
                        rebalance_desc.append("T11")
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
                    elif time_for_rebalance[2] == "production-topology7":
                        rebalance_desc.append("T7")
                    elif time_for_rebalance[2] == "production-topology8":
                        rebalance_desc.append("T8")
                    elif time_for_rebalance[2] == "production-topology9":
                        rebalance_desc.append("T9")
                    elif time_for_rebalance[2] == "production-topology12":
                        rebalance_desc.append("T12")
                    elif time_for_rebalance[2] == "production-topology13":
                        rebalance_desc.append("T13")
                    elif time_for_rebalance[2] == "production-topology14":
                        rebalance_desc.append("T14")
                    elif time_for_rebalance[2] == "production-topology15":
                        rebalance_desc.append("T15")
                    elif time_for_rebalance[2] == "production-topology1":
                        rebalance_desc.append("T1")
                    else:
                        rebalance_desc.append(time_for_rebalance[2])
                    rebalance_desc.append(" " + time_for_rebalance[4])  # should give topology name space num workers
            elif len(one_line) == 1 and is_number(one_line[0]):
                rebalance_time.append(float(one_line[0]))

        val = time[0]
        for i in range(0, len(time)):
            time[i] = (time[i] - val) / 1000
        for i in range(0, len(rebalance_time)):
            rebalance_time[i] = (rebalance_time[i] - val) / 1000

        min_length = len(time)


        if min_length > len(topology1_juice):
            min_length = len(topology1_juice)
        if min_length > len(topology2_juice):
            min_length = len(topology2_juice)
        if min_length > len(topology3_juice):
            min_length = len(topology3_juice)
        if min_length > len(topology4_juice):
            min_length = len(topology4_juice)
        if min_length > len(topology5_juice):
            min_length = len(topology5_juice)

        if min_length > len(topology1_latency):
            min_length = len(topology1_latency)
        if min_length > len(topology2_latency):
            min_length = len(topology2_latency)
        if min_length > len(topology3_latency):
            min_length = len(topology3_latency)
        if min_length > len(topology4_latency):
            min_length = len(topology4_latency)
        if min_length > len(topology5_latency):
            min_length = len(topology5_latency)

        if min_length > len(topology1_utility):
            min_length = len(topology1_utility)
        if min_length > len(topology2_utility):
            min_length = len(topology2_utility)
        if min_length > len(topology3_utility):
            min_length = len(topology3_utility)
        if min_length > len(topology4_utility):
            min_length = len(topology4_utility)
        if min_length > len(topology5_utility):
            min_length = len(topology5_utility)

        time = time[0:min_length]
        topology1_juice = topology1_juice[0:min_length]
        topology2_juice = topology2_juice[0:min_length]
        topology3_juice = topology3_juice[0:min_length]
        topology4_juice = topology4_juice[0:min_length]
        topology5_juice = topology5_juice[0:min_length]

        topology1_latency = topology1_latency[0:min_length]
        topology2_latency = topology2_latency[0:min_length]
        topology3_latency = topology3_latency[0:min_length]
        topology4_latency = topology4_latency[0:min_length]
        topology5_latency = topology5_latency[0:min_length]

        topology1_utility = topology1_utility[0:min_length]
        topology2_utility = topology2_utility[0:min_length]
        topology3_utility = topology3_utility[0:min_length]
        topology4_utility = topology4_utility[0:min_length]
        topology5_utility = topology5_utility[0:min_length]

        topology1_99tail_latency = topology1_99tail_latency[0:min_length]
        topology2_99tail_latency = topology2_99tail_latency[0:min_length]
        topology3_99tail_latency = topology3_99tail_latency[0:min_length]
        topology4_99tail_latency = topology4_99tail_latency[0:min_length]
        topology5_99tail_latency = topology5_99tail_latency[0:min_length]

        topology1_75tail_latency = topology1_75tail_latency[0:min_length]
        topology2_75tail_latency = topology2_75tail_latency[0:min_length]
        topology3_75tail_latency = topology3_75tail_latency[0:min_length]
        topology4_75tail_latency = topology4_75tail_latency[0:min_length]
        topology5_75tail_latency = topology5_75tail_latency[0:min_length]

        topology1_50tail_latency = topology1_50tail_latency[0:min_length]
        topology2_50tail_latency = topology2_50tail_latency[0:min_length]
        topology3_50tail_latency = topology3_50tail_latency[0:min_length]
        topology4_50tail_latency = topology4_50tail_latency[0:min_length]
        topology5_50tail_latency = topology5_50tail_latency[0:min_length]

        min_length1 = len(topology6_juice)
        print "min_length1", min_length1, len(topology7_juice), len(topology8_juice)
        if min_length1 > len(topology7_juice):
            min_length1 = len(topology7_juice)
        if min_length1 > len(topology8_juice):
            min_length1 = len(topology8_juice)
        if min_length1 > len(topology9_juice):
            min_length1 = len(topology9_juice)
        if min_length1 > len(topology10_juice):
            min_length1 = len(topology10_juice)


        if min_length1 > len(topology6_latency):
            min_length1 = len(topology6_latency)
        if min_length1 > len(topology7_latency):
            min_length1 = len(topology7_latency)
        if min_length1 > len(topology8_latency):
            min_length1 = len(topology8_latency)
        if min_length1 > len(topology9_latency):
            min_length1 = len(topology9_latency)
        if min_length1 > len(topology10_latency):
            min_length1 = len(topology10_latency)


        if min_length1 > len(topology6_utility):
            min_length1 = len(topology6_utility)
        if min_length1 > len(topology7_utility):
            min_length1 = len(topology7_utility)
        if min_length1 > len(topology8_utility):
            min_length1 = len(topology8_utility)
        if min_length1 > len(topology9_utility):
            min_length1 = len(topology9_utility)
        if min_length1 > len(topology10_utility):
            min_length1 = len(topology10_utility)


        topology6_juice = topology6_juice[0:min_length1]
        topology7_juice = topology7_juice[0:min_length1]
        topology8_juice = topology8_juice[0:min_length1]
        topology9_juice = topology9_juice[0:min_length1]
        topology10_juice = topology10_juice[0:min_length1]

        topology6_latency = topology6_latency[0:min_length1]
        topology7_latency = topology7_latency[0:min_length1]
        topology8_latency = topology8_latency[0:min_length1]
        topology9_latency = topology9_latency[0:min_length1]
        topology10_latency = topology10_latency[0:min_length1]

        topology6_utility = topology6_utility[0:min_length1]
        topology7_utility = topology7_utility[0:min_length1]
        topology8_utility = topology8_utility[0:min_length1]
        topology9_utility = topology9_utility[0:min_length1]
        topology10_utility = topology10_utility[0:min_length1]

        topology6_99tail_latency = topology6_99tail_latency[0:min_length1]
        topology7_99tail_latency = topology7_99tail_latency[0:min_length1]
        topology8_99tail_latency = topology8_99tail_latency[0:min_length1]
        topology9_99tail_latency = topology9_99tail_latency[0:min_length1]
        topology10_99tail_latency = topology10_99tail_latency[0:min_length1]

        topology6_75tail_latency = topology6_75tail_latency[0:min_length1]
        topology8_75tail_latency = topology8_75tail_latency[0:min_length1]
        topology7_75tail_latency = topology7_75tail_latency[0:min_length1]
        topology9_75tail_latency = topology9_75tail_latency[0:min_length1]
        topology10_75tail_latency = topology10_75tail_latency[0:min_length1]


        topology6_50tail_latency = topology6_50tail_latency[0:min_length1]
        topology7_50tail_latency = topology7_50tail_latency[0:min_length1]
        topology8_50tail_latency = topology8_50tail_latency[0:min_length1]
        topology9_50tail_latency = topology9_50tail_latency[0:min_length1]
        topology10_50tail_latency = topology10_50tail_latency[0:min_length1]

        diff = min_length - min_length1
        for x in xrange(0,diff):
            topology6_juice.insert(0,0)
            topology7_juice.insert(0,0)
            topology8_juice.insert(0,0)
            topology9_juice.insert(0,0)
            topology10_juice.insert(0,0)

            topology6_latency.insert(0,0)
            topology7_latency.insert(0,0)
            topology8_latency.insert(0,0)
            topology9_latency.insert(0,0)
            topology10_latency.insert(0,0)


            topology6_utility.insert(0,0)
            topology7_utility.insert(0,0)
            topology8_utility.insert(0,0)
            topology9_utility.insert(0,0)
            topology10_utility.insert(0,0)


            topology6_99tail_latency.insert(0,0)
            topology7_99tail_latency.insert(0,0)
            topology8_99tail_latency.insert(0,0)
            topology9_99tail_latency.insert(0,0)
            topology10_99tail_latency.insert(0,0)


            topology6_75tail_latency.insert(0,0)
            topology7_75tail_latency.insert(0,0)
            topology8_75tail_latency.insert(0,0)
            topology9_75tail_latency.insert(0,0)
            topology10_75tail_latency.insert(0,0)

            topology6_50tail_latency.insert(0,0)
            topology7_50tail_latency.insert(0,0)
            topology8_50tail_latency.insert(0,0)
            topology9_50tail_latency.insert(0,0)
            topology10_50tail_latency.insert(0,0)


        min_length2 = len(topology11_juice)
        if min_length2 > len(topology12_juice):
            min_length2 = len(topology12_juice)
        if min_length2 > len(topology13_juice):
            min_length2 = len(topology13_juice)
        if min_length2 > len(topology14_juice):
            min_length2 = len(topology14_juice)
        if min_length2 > len(topology15_juice):
            min_length2 = len(topology15_juice)


        if min_length2 > len(topology11_latency):
            min_length2 = len(topology11_latency)
        if min_length2 > len(topology12_latency):
            min_length2 = len(topology12_latency)
        if min_length2 > len(topology13_latency):
            min_length2 = len(topology13_latency)
        if min_length2 > len(topology14_latency):
            min_length2 = len(topology14_latency)
        if min_length2 > len(topology15_latency):
            min_length2 = len(topology15_latency)

        if min_length2 > len(topology11_utility):
            min_length2 = len(topology11_utility)
        if min_length2 > len(topology12_utility):
            min_length2 = len(topology12_utility)
        if min_length2 > len(topology13_utility):
            min_length2 = len(topology13_utility)
        if min_length2 > len(topology14_utility):
            min_length2 = len(topology14_utility)
        if min_length2 > len(topology15_utility):
            min_length2 = len(topology15_utility)

        topology11_utility = topology11_utility[0:min_length2]
        topology12_utility = topology12_utility[0:min_length2]
        topology13_utility = topology13_utility[0:min_length2]
        topology14_utility = topology14_utility[0:min_length2]
        topology15_utility = topology15_utility[0:min_length2]

        topology11_juice = topology11_juice[0:min_length2]
        topology12_juice = topology12_juice[0:min_length2]
        topology13_juice = topology13_juice[0:min_length2]
        topology14_juice = topology14_juice[0:min_length2]
        topology15_juice = topology15_juice[0:min_length2]

        topology11_latency = topology11_latency[0:min_length2]
        topology12_latency = topology12_latency[0:min_length2]
        topology13_latency = topology13_latency[0:min_length2]
        topology14_latency = topology14_latency[0:min_length2]
        topology15_latency = topology15_latency[0:min_length2]

        topology11_99tail_latency = topology11_99tail_latency[0:min_length2]
        topology12_99tail_latency = topology12_99tail_latency[0:min_length2]
        topology13_99tail_latency = topology13_99tail_latency[0:min_length2]
        topology14_99tail_latency = topology14_99tail_latency[0:min_length2]
        topology15_99tail_latency = topology15_99tail_latency[0:min_length2]

        topology11_75tail_latency = topology11_75tail_latency[0:min_length2]
        topology12_75tail_latency = topology12_75tail_latency[0:min_length2]
        topology13_75tail_latency = topology13_75tail_latency[0:min_length2]
        topology14_75tail_latency = topology14_75tail_latency[0:min_length2]
        topology15_75tail_latency = topology15_75tail_latency[0:min_length2]

        topology11_50tail_latency = topology11_50tail_latency[0:min_length2]
        topology12_50tail_latency = topology12_50tail_latency[0:min_length2]
        topology13_50tail_latency = topology13_50tail_latency[0:min_length2]
        topology14_50tail_latency = topology14_50tail_latency[0:min_length2]
        topology15_50tail_latency = topology15_50tail_latency[0:min_length2]

        diff = min_length - min_length2
        for x in xrange(0,diff):
            topology11_juice.insert(0,0)
            topology12_juice.insert(0,0)
            topology13_juice.insert(0,0)
            topology14_juice.insert(0,0)
            topology15_juice.insert(0,0)

            topology11_latency.insert(0,0)
            topology12_latency.insert(0,0)
            topology13_latency.insert(0,0)
            topology14_latency.insert(0,0)
            topology15_latency.insert(0,0)


            topology11_utility.insert(0,0)
            topology12_utility.insert(0,0)
            topology13_utility.insert(0,0)
            topology14_utility.insert(0,0)
            topology15_utility.insert(0,0)


            topology11_99tail_latency.insert(0,0)
            topology12_99tail_latency.insert(0,0)
            topology13_99tail_latency.insert(0,0)
            topology14_99tail_latency.insert(0,0)
            topology15_99tail_latency.insert(0,0)

            topology11_75tail_latency.insert(0,0)
            topology12_75tail_latency.insert(0,0)
            topology13_75tail_latency.insert(0,0)
            topology14_75tail_latency.insert(0,0)
            topology14_75tail_latency.insert(0,0)

            topology11_50tail_latency.insert(0,0)
            topology12_50tail_latency.insert(0,0)
            topology13_50tail_latency.insert(0,0)
            topology14_50tail_latency.insert(0,0)
            topology15_50tail_latency.insert(0,0)

        input_at_source_1 = input_at_source_1[0:min_length]
        output_at_sink_1 = output_at_sink_1[0:min_length]
        input_at_source_2 = input_at_source_2[0:min_length]
        output_at_sink_2 = output_at_sink_2[0:min_length]
        input_at_source_3 = input_at_source_3[0:min_length]
        output_at_sink_3 = output_at_sink_3[0:min_length]
        input_at_source_4 = input_at_source_4[0:min_length]
        output_at_sink_4 = output_at_sink_4[0:min_length]
        input_at_source_5 = input_at_source_5[0:min_length]
        output_at_sink_5 = output_at_sink_5[0:min_length]

        input_at_source_6 = input_at_source_6[0:min_length]
        output_at_sink_6 = output_at_sink_6[0:min_length]
        input_at_source_7 = input_at_source_7[0:min_length]
        output_at_sink_7 = output_at_sink_7[0:min_length]
        input_at_source_8 = input_at_source_8[0:min_length]
        output_at_sink_8 = output_at_sink_8[0:min_length]
        input_at_source_9 = input_at_source_9[0:min_length]
        output_at_sink_9 = output_at_sink_9[0:min_length]
        input_at_source_10 = input_at_source_10[0:min_length]
        output_at_sink_10 = output_at_sink_10[0:min_length]

        input_at_source_11 = input_at_source_11[0:min_length]
        output_at_sink_11 = output_at_sink_11[0:min_length]
        input_at_source_12 = input_at_source_12[0:min_length]
        output_at_sink_12 = output_at_sink_12[0:min_length]
        input_at_source_13 = input_at_source_13[0:min_length]
        output_at_sink_13 = output_at_sink_13[0:min_length]
        input_at_source_14 = input_at_source_14[0:min_length]
        output_at_sink_14 = output_at_sink_14[0:min_length]
        input_at_source_15 = input_at_source_15[0:min_length]
        output_at_sink_15 = output_at_sink_15[0:min_length]

        fig, ax = plt.subplots()

        print topology1_juice
        print topology2_juice
        print topology3_juice
        print topology4_juice
        print topology5_juice
        print topology6_juice
        print topology7_juice
        print topology8_juice
        print topology9_juice
        print topology10_juice

        ax2 = ax.twinx()

        #    ax2.scatter(time, movingaverage(topology1_latency,10), edgecolors ="green", label="T1 Latency", marker ="*", facecolors='none', s=40,)
        #    ax2.scatter(time, movingaverage(topology1_99tail_latency,10), edgecolors ="blue", label="T1 99 percentile tail latency", marker ="<", facecolors='none', s=40, )
        #    ax2.scatter(time, movingaverage(topology1_75tail_latency,10), edgecolors ="red", label="T1 75 percentile tail latency", marker ="<", facecolors='none', s=40, )

        ax2.scatter(time, topology1_latency, edgecolors="green", label="T1 Latency", marker="*", facecolors='none',s=40, )
        ax2.scatter(time, topology2_latency, edgecolors="#1f78b4", label="T2 Latency", marker="<", facecolors='none',s=40, )
        ax2.scatter(time, topology3_latency, edgecolors="#b2df8a", label="T3 Latency", marker="D", facecolors='none',s=40, )
        ax2.scatter(time, topology4_latency, edgecolors="#33a02c", label="T4 Latency", marker="+", facecolors='none',s=40, )
        ax2.scatter(time, topology5_latency, edgecolors="#fb9a99", label="T5 Latency", marker="<", facecolors='none',s=40, )

        ax2.scatter(time, topology6_latency, edgecolors="#e31a1c", label="T6 Latency", marker="D", facecolors='none',s=40, )
        ax2.scatter(time, topology7_latency, edgecolors="#fdbf6f", label="T7 Latency", marker="+", facecolors='none',s=40, )
        ax2.scatter(time, topology8_latency, edgecolors="#ff7f00", label="T8 Latency", marker="*", facecolors='none',s=40, )
        ax2.scatter(time, topology9_latency, edgecolors="#cab2d6", label="T9 Latency", marker="h", facecolors='none',s=40, )
        ax2.scatter(time, topology10_latency, edgecolors="#ffff99", label="T10 Latency", marker="h", facecolors='none',s=40, )
        #
        ax2.scatter(time, topology11_latency, edgecolors="#123A1F", label="T11 Latency", marker="h", facecolors='none',s=40, )
        ax2.scatter(time, topology12_latency, edgecolors="#AAAB2C", label="T12 Latency", marker="h", facecolors='none',s=40, )
        ax2.scatter(time, topology13_latency, edgecolors="#ABC123", label="T13 Latency", marker="h", facecolors='none',s=40, )
        ax2.scatter(time, topology14_latency, edgecolors="#886A1F", label="T14 Latency", marker="h", facecolors='none',s=40, )
        ax2.scatter(time, topology15_latency, edgecolors="#999999", label="T15 Latency", marker="h", facecolors='none',s=40, )

        # ax2.scatter(time, topology1_99tail_latency, edgecolors ="green", label="T1 Latency", marker ="*", facecolors='none', s=40,)
        # ax2.scatter(time, topology2_99tail_latency, edgecolors ="#1f78b4", label="T2 Latency", marker ="<", facecolors='none', s=40,)
        # ax2.scatter(time, topology3_99tail_latency, edgecolors ="#b2df8a", label="T3 Latency", marker="D", facecolors='none', s=40, )
        # ax2.scatter(time, topology4_99tail_latency, edgecolors ="#33a02c", label="T4 Latency", marker="+", facecolors='none', s=40,)
        # ax2.scatter(time, topology5_99tail_latency, edgecolors ="#fb9a99", label="T5 Latency", marker ="<", facecolors='none', s=40,)

        # ax2.scatter(time, topology6_99tail_latency, edgecolors ="#e31a1c", label="T6 Latency", marker="D", facecolors='none', s=40, )
        # ax2.scatter(time, topology7_99tail_latency, edgecolors ="#fdbf6f", label="T7 Latency", marker="+", facecolors='none', s=40,)
        # ax2.scatter(time, topology8_99tail_latency, edgecolors ="#ff7f00", label="T8 Latency", marker ="*", facecolors='none', s=40,)
        # ax2.scatter(time, topology9_99tail_latency, edgecolors ="#cab2d6", label="T9 Latency", marker="h", facecolors='none', s=40, )
        # ax2.scatter(time, topology10_99tail_latency, edgecolors ="#ffff99", label="T10 Latency", marker="h", facecolors='none', s=40,)
        # ax2.scatter(time, topology11_99tail_latency, edgecolors ="#cab2d6", label="T11 Latency", marker="h", facecolors='none', s=40, )
        # ax2.scatter(time, topology12_99tail_latency, edgecolors ="#ffff99", label="T12 Latency", marker="h", facecolors='none', s=40,)
        # ax2.scatter(time, topology13_99tail_latency, edgecolors ="#cab2d6", label="T13 Latency", marker="h", facecolors='none', s=40, )
        # ax2.scatter(time, topology14_99tail_latency, edgecolors ="#ffff99", label="T12 Latency", marker="h", facecolors='none', s=40,)
        # ax2.scatter(time, topology15_99tail_latency, edgecolors ="#cab2d6", label="T13 Latency", marker="h", facecolors='none', s=40,

        ax.set_xlabel('Time/s', fontsize=10)
        #   ax.set_ylabel('Juice', fontsize=10)
        ax2.set_ylabel('Latency/ms', fontsize=10)

        ax.grid(True)
        fig.tight_layout()
        clrs = ["b", "g", "r", "c", "m", "y", "k"]
        # clrs = ["k", "k", "k", "k", "k", "k", "k"]
        linestyles = ['--', '-.', 'solid', 'dotted']
        print "Rebalance time", rebalance_time
        print "Rebalance desc", rebalance_desc
        for j in range(0, len(rebalance_time)):
            # if (rebalance_time[j] >= 20000 and rebalance_time[j] <= 30000):# and ("T2" in rebalance_desc[j]):
            print rebalance_time[j]
            la = rebalance_desc[j]
            ax.vlines(x=rebalance_time[j], ymax=6, ymin=-1, colors=clrs[j % 7], linestyle='solid', label=la)


        lines, labels = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(lines + lines2, labels + labels2, loc=9, bbox_to_anchor=(0.5, -0.1), ncol=2,
                   prop={'size': 10})  # , label=la,)#linestyles[j%4]

        ax.set_ylim(0, 1.1)
        ax2.set_ylim(0, 100)
        #plt.xlim(0, 15000)
        plt.savefig(filename + '-latencies.png', bbox_inches='tight')

        fig, ax = plt.subplots()
        ax.scatter(time, movingaverage(topology1_juice, 10), edgecolors="blue", label="T1 Juice", marker="D", facecolors='none', s=40, )
        ax.scatter(time, movingaverage(topology2_juice, 10), edgecolors="green", label="T2 Juice Latency-SLO=70 Utility=35", marker=">", facecolors='none', s=40, )
        ax.scatter(time, movingaverage(topology3_juice, 10), edgecolors="red", label="T3 Juice Latency-SLO=70 Utility=35", marker="h",facecolors='none', s=40, )
        ax.scatter(time, movingaverage(topology4_juice, 10), edgecolors="c", label="T4 Juice Latency-SLO=70 Utility=35", marker="s",facecolors='none', s=40, )
        ax.scatter(time, movingaverage(topology5_juice, 10), edgecolors="m", label="T5 Juice Latency-SLO=50 Utility=35", marker=">",facecolors='none', s=40, )

        ax.scatter(time, topology6_juice, edgecolors="black", label="T6 Juice SLO=1 Utility=5", marker="h",facecolors='none', s=40, )
        ax.scatter(time, topology7_juice, edgecolors="darkorange", label="T7 Juice SLO=1 Utility=5", marker="s",facecolors='none', s=40, )
        ax.scatter(time, topology8_juice, edgecolors="#456648", label="T8 Latency SLO=50 Utility=35", marker=">",facecolors='none', s=40, )
        ax.scatter(time, topology9_juice, edgecolors="y", label="T9 Juice SLO=1 Utility=5", marker="h",facecolors='none', s=40, )
        ax.scatter(time, topology10_juice, edgecolors="#886F4C", label="T10 Juice SLO=1 Utility=5", marker="s",facecolors='none', s=40, )

        ax.scatter(time, topology11_juice, edgecolors="#123A1F", label="T11 Juice SLO=1 Utility=5", marker="s",facecolors='none', s=40, )
        ax.scatter(time, topology12_juice, edgecolors="#AAAB2C", label="T12 Juice SLO=1 Utility=5", marker="h",facecolors='none', s=40, )
        ax.scatter(time, topology13_juice, edgecolors="#ABC123", label="T13 Juice SLO=1 Utility=5", marker="s",facecolors='none', s=40, )
        ax.scatter(time, topology14_juice, edgecolors="#886A1F", label="T14 Juice SLO=1 Utility=5", marker="h",facecolors='none', s=40, )
        ax.scatter(time, topology15_juice, edgecolors="#999999", label="T15 Juice SLO=1 Utility=5", marker="s",facecolors='none', s=40)

        ax.set_xlabel('Time/s', fontsize=10)
        ax2.set_ylabel('Juice/ms', fontsize=10)

        ax.grid(True)
        fig.tight_layout()

        # plt.vlines(x=600, ymax=1000 , ymin=0, label="Ten Minute Mark", colors='blue')

        clrs = ["b", "g", "r", "c", "m", "y", "k"]
        # clrs = ["k", "k", "k", "k", "k", "k", "k"]
        linestyles = ['--', '-.', 'solid', 'dotted']
        for j in range(0, len(rebalance_time)):
            # if ("T1" in rebalance_desc[j] and not "T10" in rebalance_desc[j]) or "T2" in rebalance_desc[j]:
            la = rebalance_desc[j]
            ax.vlines(x=rebalance_time[j], ymax=500, ymin=-1, colors=clrs[j % 7], linestyle='solid', label=la)

        lines, labels = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(lines + lines2, labels + labels2, loc=9, bbox_to_anchor=(0.5, -0.1), ncol=2,
                  prop={'size': 10})  # , label=la,)#linestyles[j%4]

        # ax2.set_yscale('log')
        plt.xlim(0,10000)
        ax.set_ylim(0, 1.1)
        ax2.set_ylim(40, 100)
        # ax2.set_ylim(0,200)
        # ax2.set_ylim(-10000,800000)
        #plt.xlim(0, 10000)
        plt.savefig(filename + '-juice.png', bbox_inches='tight')
        # plotting utilities

        fig, ax = plt.subplots()
        ax.scatter(time, topology1_utility, edgecolors="green", label="T1 Utility", marker="D", facecolors='none',s=40, )
        ax.scatter(time, topology2_utility, edgecolors="yellow", label="T2 ", marker=">", facecolors='none', s=40, )
        ax.scatter(time, topology3_utility, edgecolors="red", label="T3", marker="h", facecolors='none', s=40, )
        ax.scatter(time, topology4_utility, edgecolors="darkorange", label="T4", marker="s", facecolors='none', s=40, )
        ax.scatter(time, topology5_utility, edgecolors="blue", label="T5", marker=">", facecolors='none', s=40, )

        ax.scatter(time, topology6_utility, edgecolors="purple", label="T6", marker="h", facecolors='none', s=40, )
        ax.scatter(time, topology7_utility, edgecolors="pink", label="T7", marker="s", facecolors='none', s=40, )
        ax.scatter(time, topology8_utility, edgecolors="grey", label="T8", marker=">", facecolors='none', s=40, )
        ax.scatter(time, topology9_utility, edgecolors="purple", label="T9", marker="h", facecolors='none', s=40, )
        ax.scatter(time, topology10_utility, edgecolors="pink", label="T10", marker="s", facecolors='none', s=40, )

        ax.scatter(time, topology11_utility, edgecolors="#123A1F", label="T11", marker="s", facecolors='none', s=40, )
        ax.scatter(time, topology12_utility, edgecolors="#AAAB2C",label="T12", marker="s", facecolors='none', s=40, )
        ax.scatter(time, topology13_utility, edgecolors="#ABC123", label="T13", marker="s", facecolors='none', s=40, )
        ax.scatter(time, topology14_utility, edgecolors="#886A1F", label="T14", marker="s", facecolors='none', s=40, )
        ax.scatter(time, topology15_utility, edgecolors="#999999", label="T15", marker="s", facecolors='none', s=40, )

        ax.set_xlabel('Time/S', fontsize=10)
        ax.set_ylabel('Utility', fontsize=10)
        ax.grid(True)
        fig.tight_layout()

        xlim_start = 0
        xlim_end = 10500
        linestyles = ['--', '-.', 'solid', 'dotted']
        for j in range(0, len(rebalance_time)):
            if (rebalance_time[j] >= xlim_start and rebalance_time[j] <= xlim_end):
                la = rebalance_desc[j]
                ax.vlines(x=rebalance_time[j], ymax=600, ymin=-1, colors=clrs[j % 7], linestyle='solid',
                          label=la, )  # linestyles[j%4]

        sum = []
        temp_time = []
        for j in range(0, len(time)):
            temp_time.append(time[j])
            sum.append(topology1_utility[j]
                       + topology2_utility[j]
                       + topology3_utility[j]
                       + topology4_utility[j]
                       + topology5_utility[j]
                       + topology6_utility[j]
                       + topology7_utility[j]
                       + topology8_utility[j]
                       + topology9_utility[j]
                       + topology10_utility[j]
                       + topology11_utility[j]
                       + topology12_utility[j]
                       + topology13_utility[j]
                       + topology14_utility[j]
                       + topology15_utility[j]
                       )


        ax.scatter(temp_time, movingaverage(sum,10), edgecolors="red", label="Sum", marker="h", facecolors='r', s=80, )
        lines, labels = ax.get_legend_handles_labels()
        ax.legend(lines, labels, loc=9, bbox_to_anchor=(0.5, -0.1), ncol=2, prop={'size': 10})
        plt.xlim(xlim_start, xlim_end)
        ax.set_ylim(0, 526)
        plt.savefig(filename + '-utilities.png', bbox_inches='tight')
        # plotting input and output tuples
        fig, ax = plt.subplots()


        ax.scatter(time, input_at_source_1, edgecolors="green", label="T1 input", facecolor='none', marker="D", s=40)
     #   ax.scatter(time, output_at_sink_1, edgecolors="blue", label="T1 output", facecolor='none', marker="D", s=40)


        ax.scatter(time, input_at_source_2, edgecolors="pink", label="T2 input", facecolor='none', marker="D", s=40)
        # ax.scatter(time, output_at_sink_12, edgecolors="yellow", label="T12 output", facecolor='none', marker="D", s=40)


        ax.scatter(time, input_at_source_3, edgecolors="green", label="T3 input", facecolor='none', marker=">", s=40)
       # ax.scatter(time, output_at_sink_3, edgecolors="blue", label="T3 output", facecolor='none', marker=">", s=40)
        ax.scatter(time, input_at_source_5, edgecolors = "yellow", label= "T5 input", facecolor='none', marker = "D", s=40)
        #   ax.scatter(time, input_at_source_3, edgecolors = "teal", label= "T3 input", facecolor='none', marker = "x",s=40)
        ax.scatter(time, input_at_source_4, edgecolors = "b", label= "T4 input", facecolor='none', marker = "x",s=40)
        #   ax.scatter(time, input_at_source_5, edgecolors = "m", label= "T5 input", facecolor='none', marker = "x",s=40)
        # ax.scatter(time, input_at_source_6, edgecolors = "r", label= "T6 input", facecolor='none', marker = "h", s=40)
        # ax.scatter(time, input_at_source_7, edgecolors = "purple", label= "T7 input", facecolor='none',marker = "v" , s=40)
        # ax.scatter(time, input_at_source_8, edgecolors = "brown", label= "T8 input", facecolor='none',marker = "v" , s=40)
        # ax.scatter(time, input_at_source_9, edgecolors = "yellow", label= "T9 input", facecolor='none',marker = "v" , s=40)
        # ax.scatter(time, input_at_source_10, edgecolors = "black", label= "T10 input", facecolor='none',marker = "v" , s=40)
        #
        # ax.scatter(time, output_at_sink_1, edgecolors = "blue", label= "T1 output" ,facecolor='none', marker = "+", s=40)
        # ax.scatter(time, output_at_sink_2, edgecolors = "blue", label= "T2 output" ,facecolor='none', marker = "<",s=40)
        # ax.scatter(time, output_at_sink_3, edgecolors = "green", label= "T3 output", facecolor='none', marker = "h", s=40)
        # ax.scatter(time, output_at_sink_4, edgecolors = "y", label= "T4 output", facecolor='none', marker = "h", s=40)
        # ax.scatter(time, output_at_sink_5, edgecolors = "orange", label= "T5 output", facecolor='none', marker = "h", s=40)ax.scatter(time, input_at_source_6, edgecolors = "g", label= "T6 input", facecolor='none', marker = "x",s=40)
        # ax.scatter(time, output_at_sink_6, edgecolors = "r", label= "T6 output", facecolor='none', marker = "h", s=40)
        # ax.scatter(time, output_at_sink_7, edgecolors = "magenta", label= "T7 output" , facecolor='none', marker = "s", s=40)
        for j in range(0, len(rebalance_time)):
            #if rebalance_desc[j] < 4000:

            la = rebalance_desc[j]  # target[j] + " " + target_operator[j] + " " + victim[j] + " " + victim_operator[j]
            ax.vlines(x=rebalance_time[j], ymax=200000, ymin=-1, colors='black', linestyle=linestyles[j % 4],
                      label=la, )  # label=la,label="rebalance " + str(j+1),

        ax.set_xlabel('Time/S', fontsize=10)
        ax.set_ylabel('Number of Tuples', fontsize=10)

        ax.grid(True)
        fig.tight_layout()
        # plt.vlines(x=600, ymax=5000 , ymin=-1, label="Ten Minute Mark", colors='blue')
        plt.legend(loc=9, bbox_to_anchor=(0.5, -0.1), ncol=2, prop={'size': 10})
        plt.xlim(0,5500)
        #plt.ylim(0, 200000)
        plt.ylim(0, 12000)
        plt.savefig(filename + "+tuples" + '.png', bbox_inches='tight')
