import os
import random
TRAINING_PATH_AD = 'data/AD'
TRAINING_PATH_MCI = 'data/MCI'
TRAINING_PATH_normal = 'data/normal'
train=[TRAINING_PATH_AD,TRAINING_PATH_MCI,TRAINING_PATH_normal]
f = open("label.txt",'a')
for train_data in train:


    for img_name in os.listdir(train_data):

        f.writelines([img_name,' ',train_data.split('/')[-1]])
        f.write('\n')
with open('label.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()  # 获取所有行
    sum = 0
    list = []
    for line in lines:  # 第i行
            # 找到第一个空格
        list.append(line)


with open('test.txt', 'a', encoding='utf-8') as g:
    a = random.sample(list, 50)  # 随机抽取500行
    for i in a:
        g.write(i)
    f.close()
    g.close()
