# Задача 44: В ячейке ниже представлен код генерирующий DataFrame,
#  которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид.
# Сможете ли вы это сделать без get_dummies?

import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(data.head())
# используя get_dummies
print(pd.get_dummies(data['whoAmI']).head())

# без get_dummies
data1 = {list(set(lst))[a]: a for a in range(len(list(set(lst))))}
for key_ in data1.keys():
    data1[key_] = [key_ == el for el in lst]
data1 = pd.DataFrame(data1)
print(data1.head())