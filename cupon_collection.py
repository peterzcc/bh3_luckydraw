import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

def lucky_daw(prob,criteria):
    current_hist = np.zeros_like(prob)
    num_draws = 0
    finished = False
    while not finished:
        this_draw = np.random.multinomial(1,prob)
        current_hist += this_draw
        num_draws += 1
        if criteria(current_hist):
            finished = True
    duplicated_items = np.sum((current_hist-1)*(current_hist > 1))
    max_duplicated_items = np.max(current_hist-1)
    return current_hist, num_draws, duplicated_items, max_duplicated_items


def main():
    up_probs = np.array([2.479,*([1.24]*3),*([0.413]*6),*[0.310]*12])/(4.958+7.437)
    idx_up_weapon = [0]
    id_up_stigmata = list(range(1,4))
    id_down_weapon = list(range(4,10))
    id_down_stigmata = list(range(10,22))
    def criteria_suit(x):
        return x[1] > 0 and x[2] > 0 and x[3] > 0
    num_users = 1000000
    user_draw_nums = []
    user_duplicated_items = []
    user_max_duplicated_items = []
    for u in range(num_users):
        _,this_num_draws,this_user_duplicated_item, max_duplicate = \
            lucky_daw(up_probs,criteria=criteria_suit)
        user_draw_nums.append(this_num_draws)
        user_duplicated_items.append(this_user_duplicated_item)
        user_max_duplicated_items.append(max_duplicate)
    target_metric = np.array(user_draw_nums).astype(np.int32)
    y,bins = np.histogram(target_metric,bins=target_metric.max()-target_metric.min())
    x = bins[:-1]
    cum_y_distribution = np.cumsum(y).astype(np.float32)/num_users
    plt.figure(1)
    plt.plot(x,cum_y_distribution)
    print(tabulate([x[0:30].astype(int), np.around(cum_y_distribution[0:30], decimals=4)]))
    print("median of num. of draws: {}".format(np.median(user_draw_nums)))
    plt.figure(2)
    plt.hist(target_metric,bins=target_metric.max()-target_metric.min())
    plt.show()
    return

if __name__ == '__main__':
    main()
