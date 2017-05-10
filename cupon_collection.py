import numpy as np
import matplotlib.pyplot as plt

def lucky_daw(prob):
    current_hist = np.zeros_like(prob)
    num_draws = 0
    finished = False
    while not finished:
        this_draw = np.random.multinomial(1,prob)
        current_hist += this_draw
        num_draws += 1
        if current_hist[1] > 0 and current_hist[2] > 0 and current_hist[3] > 0:
            finished = True
    duplicated_items = np.sum((current_hist-1)*(current_hist > 1))
    max_duplicated_items = np.max(current_hist-1)
    return current_hist, num_draws, duplicated_items, max_duplicated_items


def main():
    up_probs = np.array([2.479,*([1.24]*3),*([0.413]*6),*[0.310]*12])/(4.958+7.437)
    num_users = 1000000
    user_draw_nums = []
    user_duplicated_items = []
    user_max_duplicated_items = []
    for u in range(num_users):
        _,this_num_draws,this_user_duplicated_item, max_duplicate = \
            lucky_daw(up_probs)
        user_draw_nums.append(this_num_draws)
        user_duplicated_items.append(this_user_duplicated_item)
        user_max_duplicated_items.append(max_duplicate)
    user_draw_nums = np.array(user_max_duplicated_items).astype(np.int32)
    plt.hist(user_draw_nums,bins=user_draw_nums.max()-user_draw_nums.min())
    plt.show()
    return

if __name__ == '__main__':
    main()
