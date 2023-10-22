
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from datetime import datetime
from sklearn import preprocessing
import joblib
import os
import shutil

def load_csv(filename):
    data = pd.read_csv(filename)
    global n
    n = data.shape[1]
    n = n - 1
    feature = data.iloc[:, :-1].values
    target = data.iloc[:, -1].values
    x_train, x_test, y_train, y_test = train_test_split(feature, target, test_size=0.2, random_state=1)
    dataset_train = np.concatenate((x_train, np.array([y_train]).T), axis=1)
    dataset_test = np.concatenate((x_test, np.array([y_test]).T), axis=1)
    return dataset_train, dataset_test, x_train, x_test, y_train, y_test

def HGBR(lr,max_num,minl_num,maxs_num,num,x_train, y_train,x_test,y_test):
    hgbr = HistGradientBoostingRegressor(learning_rate=lr, loss='absolute_error', max_depth=max_num, min_samples_leaf=minl_num,
max_leaf_nodes=maxs_num, max_iter=num)
    hgbr.fit(x_train, y_train)
    y_pred = hgbr.predict(x_test)
    max_error = max(abs(y_pred - y_test) / abs(y_test))
    print('平均绝对误差：', mean_absolute_error(y_test, y_pred))
    print('平均相对绝对误差：', mean_absolute_percentage_error(y_test, y_pred))
    print('均方误差：', mean_squared_error(y_test, y_pred))
    print('R方: ', r2_score(y_test, y_pred))
    print('最大相对误差：', max_error)
    m_score = (1-max_error)*100
    r_score = (r2_score(y_test, y_pred))*100
    score = (m_score*0.3) + (r_score*0.7)
    print('模型得分：', int(score))
    a = float(('%.6f' % (max_error)))
    b = float('%.4f' % (r2_score(y_test, y_pred)))
    return y_pred, hgbr, a, b, score

def HGBRS(path,lr,max_num,minl_num,maxs_num,num):
    dataset_train, dataset_test, x_train, x_test, y_train, y_test = load_csv(path)
    name1 = os.path.basename(path)
    name = name1.split('.')[0]
    now = datetime.now()
    timestr = now.strftime("-%Y%m%d-%H%M%S")

    y_pred, hgbr, a, b, score = HGBR(lr, max_num, minl_num, maxs_num, num, x_train, y_train, x_test, y_test)
    name1 = str(name + '+hgbr+' + str(int(score)) +'分+'+str(n)+'输入' + timestr)
    dirs = name1
    if not os.path.exists(dirs):
        os.makedirs(dirs)
    joblib.dump(hgbr, dirs+"/hgbr_model.joblib")

    def picture():
        dirs = name1
        if not os.path.exists(dirs):
            os.makedirs(dirs)
        dir = 'picture'
        if not os.path.exists(dir):
            os.makedirs(dir)
        plt.switch_backend('agg')
        plt.clf()
        plt.plot(dataset_test[:, -1], color="red", label="True value")
        plt.plot(y_pred, color="blue", label="predict value")
        plt.legend()
        plt.savefig("picture/hgbr_figure.png")
        plt.savefig(dirs + "/hgbr_figure.png")

        def get_desk_p():
            return os.path.join(os.path.expanduser('~'), "Desktop")
        path1 = get_desk_p() + "/Model"
        if not os.path.exists(path1):
            os.makedirs(path1)
        shutil.move(dirs, path1)
    picture()
    return a, b, score




