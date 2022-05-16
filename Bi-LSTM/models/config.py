# 设置lstm训练参数
class TrainingConfig(object):
    batch_size = 32
    # 学习速率
    lr = 0.001
    epoches = 50
    print_step = 10


class LSTMConfig(object):
    emb_size = 500  # 词向量的维数
    hidden_size = 256  # lstm隐向量的维数
    n_layers = 2
