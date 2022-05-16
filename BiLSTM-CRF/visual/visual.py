import re
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

file_path=r'F:\研究生课件\自然语言处理\作业\WordSeg\BiLSTM-CRF\visual\train2.log'
def main(type):
    file = open(file_path,'r')
    list1 = []
    # search the line including accuracy
    for line in file:
        m=re.search('f1 score', line)
        if m:
        # [0-9]  匹配任何数字,类似于 [0123456789]
        # .  匹配除 "\n" 之外的任何单个字符
            #dev——loss
            n=re.search('[0-9]+\.[0-9]{3}', line[m.span()[0]:]) # 正则表达式
            # n=re.search('[0-9]+\.[0-9]{3}', line) # 正则表达式
            if n is not None:
                list1.append(n.group()) # 提取精度数字
    # list1=list1[:-1]
    list1=list(map(float,list1))
    file.close()

    x=np.arange(0,11)
    plt.plot(x, list1)

    plt.xlabel('epoch')
    plt.ylabel('f1')
    plt.title('Kfold')

    plt.show()

if __name__ == '__main__':
    main('train loss')

# import numpy as np
# from matplotlib import pyplot as plt
# from scipy.interpolate import make_interp_spline
#
# x = np.array([6, 7, 8, 9, 10, 11, 12])
# y = np.array([1.53E+03, 5.92E+02, 2.04E+02, 7.24E+01, 2.72E+01, 1.10E+01, 4.70E+00])
# x_smooth = np.linspace(x.min(), x.max(), 300)
# y_smooth = make_interp_spline(x, y)(x_smooth)
# plt.plot(x_smooth, y_smooth)
# plt.show()
