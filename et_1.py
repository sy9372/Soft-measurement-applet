
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
# from sklearn import preprocessing
# import joblib
# import os

# 1.导入数据
def load_csv(filename):
    data = pd.read_csv(filename)
    # D:/磷化工帮助汇总/GBDT/GBDT_last/gbdt/machine learningtest.csv
    # C:/Users/czx/Desktop/SHUJU1.csv
    # data.head()  # 读取前五行的数据，pycharm中可以不加，用在jupyter notebook中查看数据用
    # data1 = data.iloc[:, :-1]  # iloc函数：通过行号来取行数据（切片：最后一列提取出来）
    feature = data.iloc[:, :-1].values
    target = data.iloc[:, -1].values

    # 2.数据处理
    x_train, x_test, y_train, y_test = train_test_split(feature, target, test_size=0.2, random_state=1)

    dataset_train = np.concatenate((x_train, np.array([y_train]).T), axis=1)
    dataset_test = np.concatenate((x_test, np.array([y_test]).T), axis=1)

    return dataset_train, dataset_test, x_train, x_test, y_train, y_test

# 调用svm模型
def ET():
    et = ExtraTreesRegressor( max_depth=1, min_samples_leaf=2,
min_samples_split=3, n_estimators=100)
    et.fit(x_train, y_train)
    y_pred = et.predict(x_test)
    # print('预测输出为：', y_pred)

    max_error = max(abs(y_pred - y_test) / y_test)
    print('平均绝对误差：', mean_absolute_error(y_test, y_pred))
    print('平均相对绝对误差：', mean_absolute_percentage_error(y_test, y_pred))
    print('均方误差：', mean_squared_error(y_test, y_pred))
    print('R方: ', r2_score(y_test, y_pred))
    print('最大相对误差：', max_error)
    return y_pred

# 4.数据准确度分析



if __name__ == '__main__':
    dataset_train, dataset_test, x_train, x_test, y_train, y_test = load_csv(r"E:\老电脑内容备份\磷化工项目汇总文件\亮-硫酸模型上传\硫酸B系列焙烧炉\焙烧风量模型\GBDT\已处理_焙烧风量模型.csv")
    # lr = float(input('学习率：'))
    # max_num = int(input('学习器最大深度：'))
    # minl_num = int(input('叶子节点最小样本数：'))
    # mins_num = int(input('请内部节点最小样本数：'))
    # num = int(input('迭代次数:'))
    # GBDT(lr, max_num, minl_num, mins_num, num, x_train, y_train,x_test, y_test)
    y_pred = ET()


    # 拟合曲线
    plt.plot(dataset_test[:, -1], color="red", label="True value")
    plt.plot(y_pred, color="blue", label="predict value")
    plt.legend()
    plt.show()



# import os
# # from sklearn.externals import joblib
# import joblib
#
# # 保存模型，并创建文件目录
# dirs = 'data'
# if not os.path.exists(dirs):
#     os.makedirs(dirs)
# # 保存模型
# joblib.dump(gbdt, dirs+'/gbdt_trained.joblib')

# # 读取模型
# LR = joblib.load(dirs + '/gbdt.pkl')
#
# test = [[435.3583, 125, 614]]
#
# print('预测结果:\n', gbdt.predict(test))




