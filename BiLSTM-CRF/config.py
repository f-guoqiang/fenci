import os
import torch
data_dir = os.getcwd() + '/data/'
train_dir = data_dir + 'training.npz'
test_dir = data_dir + 'test.npz'
files = ['training', 'test']
vocab_path = data_dir + 'vocab.npz'

exp_dir = os.getcwd() + '/experiments/'
model_dir = exp_dir + 'model_2.pth'
log_dir = exp_dir + 'train_2.log'
case_dir = os.getcwd() + '/case/bad_case_2.txt'
output_dir = data_dir + 'output_2.txt'

max_vocab_size = 1000000

n_split = 10
dev_split_size = 0.1
batch_size = 16
embedding_size = 200
hidden_size = 256
lstm_layers = 2
lstm_drop_out = 0.2
nn_drop_out = 0
lr = 0.001
betas = (0.9, 0.999)
lr_step = 3
lr_gamma = 0.5

epoch_num = 50
min_epoch_num = 5
patience = 0.0002
patience_num = 3

# 只能设置成0
gpu = '0'

# # if gpu != '':
# #     torch.distributed.init_process_group(backend='nccl')
# #     local_rank = torch.distributed.get_rank()
# #     torch.cuda.set_device(local_rank)
# #     device = torch.device("cuda", local_rank)
# # else:
# #     device = torch.device("cpu")


# B：分词头部 M：分词词中 E：分词词尾 S：独立成词
label2id = {'B': 0, 'M': 1, 'E': 2, 'S': 3}

id2label = {_id: _label for _label, _id in list(label2id.items())}