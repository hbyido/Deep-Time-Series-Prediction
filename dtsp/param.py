# encoding: utf-8
"""
@author : zhirui zhou
@contact: evilpsycho42@gmail.com
@time   : 2019/11/25 11:00
"""
SIMPLE_WAVENET_HP = {
    'path': None,
    'target_size': 1,
    'dilation': None,
    'residual_channels': 12,
    'optimizer': 'Adam',
    'learning_rate': 0.001,
    'loss_fn': 'MSELoss',
    'teacher_forcing_rate': 0.5,
    'lr_scheduler': None,
    'lr_scheduler_kw': None,
}

SIMPLE_SEQ2SEQ_HP = {
    'path': None,
    'target_size': 1,
    'hidden_size': 12,
    'rnn_type': 'LSTM',
    'optimizer': 'Adam',
    'learning_rate': 0.001,
    'loss_fn': 'MSELoss',
    'teacher_forcing_rate': 0.5,
    'lr_scheduler': None,
    'lr_scheduler_kw': None,
}