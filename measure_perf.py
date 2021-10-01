import numpy as np
from counter import Counter
from countminsketch import CountMinSketch, CountMinSketchMinUpdate
import matplotlib.pyplot as plt 

no_of_inserts = []
count_min_error_list = []
count_min_update_error_list = []


def get_error(count1,count2,keylist):
    error = 0
    for key in keylist:
        specific_error = abs(count1[key]-count2[key])
        print("key: {} Correct Value: {} Got: {} Error: {}".format(key,count1[key],count2[key],specific_error))
        #error = error + specific_error
        error = max(error,specific_error)
    return error 
    #return error/len(keylist)

def run_test():
    no_of_keys = 100
    no_of_insert = 1000000000
    measure_step = 100
    m = 10
    d = 5
    keylist = list(range(0,no_of_keys))
    prob = np.array([1 for i in range(0,no_of_keys)])
    prob = np.array([1/i for i in range(1,no_of_keys+1)])
    prob = prob / np.sum(prob)
    hash_counter = Counter()
    count_min = CountMinSketch(m,d)
    count_min_update = CountMinSketchMinUpdate(m,d)
    for i in range(no_of_insert):
        sel_key = np.random.choice(keylist,1,p=prob)
        hash_counter.add(sel_key[0])
        count_min.add(sel_key[0])
        count_min_update.add(sel_key[0])
        if (i % measure_step) == 0:
            no_of_inserts.append(i+1)
            count_min_error_list.append(get_error(hash_counter,count_min,keylist))
            count_min_update_error_list.append(get_error(hash_counter,count_min_update,keylist))
    fig = plt.figure()
    plt.title("Comparision of the error of CountMinSketch and CountMinUpdate")
    plt.xlabel("no of inserts")
    plt.ylabel("error")
    plt.plot(no_of_inserts,count_min_error_list,label="CountMinSketch")
    plt.plot(no_of_inserts,count_min_update_error_list,label="CountMinUpdate")
    plt.legend()
    plt.savefig("plot.png")


run_test()