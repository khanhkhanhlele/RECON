# Copyright 2020-present, Pietro Buzzega, Matteo Boschini, Angelo Porrello, Davide Abati, Simone Calderara.
# All rights reserved.
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

import sys
from datetime import datetime
import time
from typing import Union


class ProgressBar:
    def __init__(self, verbose=True):
        self.old_time = 0
        self.running_sum = 0
        self.verbose = verbose
        self.start_time = time.time()
        
    def reset_start_time(self):
        self.start_time = time.time()

    def prog(self, log_vars, max_iter) -> None:
        epoch = log_vars.pop('epoch')
        current_iter = log_vars.pop('iter')
        # lrs = log_vars.pop('lrs')

        message = (f'[epoch:{epoch:3d}, iter:{current_iter:8,d}]')
        # for v in lrs:
        #     message += f'{v:.3e},'
        # message += ')] '

        # time and estimated time
        # if 'time' in log_vars.keys():
        #     iter_time = log_vars.pop('time')
        #     data_time = log_vars.pop('data_time')

        #     total_time = time.time() - self.start_time
        #     time_sec_avg = total_time / (current_iter - self.start_iter + 1)
        #     eta_sec = time_sec_avg * (self.max_iters - current_iter - 1)
        #     eta_str = str(datetime.timedelta(seconds=int(eta_sec)))
        #     message += f'[eta: {eta_str}, '
        #     message += f'time (data): {iter_time:.3f} ({data_time:.3f})] '

        # other items, especially losses
        for k, v in log_vars.items():
            message += f'{k}: {v:.4f} '
        """
        Prints out the progress bar on the stderr file.
        :param i: the current iteration
        :param max_iter: the maximum number of iteration
        :param epoch: the epoch
        :param task_number: the task index
        :param loss: the current value of the loss function
        """
        # if num_neurons is not None:
        #     num_neurons = '-'.join(str(int(num)) for num in num_neurons)
        # if not self.verbose:
        #     i = log_vars.pop('iter')
        #     if i == 0:
        #         print('[ {} ] Task {} | epoch {}\n'.format(
        #             datetime.now().strftime("%m-%d | %H:%M"),
        #             task_number if isinstance(task_number, int) else task_number,
        #             epoch
        #         ), file=sys.stderr, end='', flush=True)
        #     else:
        #         return
        i = current_iter
        # if i == 0:
        #     self.old_time = time()
        #     self.running_sum = 0
        # else:
        #     self.running_sum = self.running_sum + (time() - self.old_time)
        #     self.old_time = time()
        if i:  # not (i + 1) % 10 or (i + 1) == max_iter:
            progress = min(float((i + 1) / max_iter), 1)
            progress_bar = ('█' * int(30 * progress)) + ('┈' * (30 - int(30 * progress)))
            print('\r{} | {}'.format(
                progress_bar,
                message
            ), file=sys.stderr, end='', flush=True)

def progress_bar(i: int, max_iter: int, epoch: Union[int, str],
                 task_number: int, loss: float) -> None:
    """
    Prints out the progress bar on the stderr file.
    :param i: the current iteration
    :param max_iter: the maximum number of iteration
    :param epoch: the epoch
    :param task_number: the task index
    :param loss: the current value of the loss function
    """
    global static_bar

    if i == 0:
        static_bar = ProgressBar()
    static_bar.prog(i, max_iter, epoch, task_number, loss)
