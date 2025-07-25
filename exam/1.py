from pathlib import Path
from matplotlib import pyplot as plt

import numpy as np
import pandas as pd


from sklearn.linear_model import LinearRegression,RANSACRegressor

#          == == == == == 1 == == == == ==                                                == == == == == 1 == == == == ==                                                       == == == == == 1 == == == == ==

# VAR 1 Выполните задачу кластеризации. Количество кластеров известно заранее и равно двум.

filepath = Path.cwd()/'data1.npz'
file = np.load(filepath)



data = pd.DataFrame({"X": file["x"],'Y': file["y"]})

data = (data-data.mean()) / data.std()# стандартизирую


print(data.info()) # нет пропусков

plt.scatter(data['X'],data['Y'])
plt.title('Визуализация сырых данных')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

#Явно видны две группы (1 - несколько наложенных друг на друга синусоид (наверное две) с некоторым шумом и 2 - некоторая прямая линия с малым шумом и резким возростанием в начале и в конце )

# точки линейно не разделимы, первая мысль использовать алгоритм (SpectralClustering) для разделения всх данных на меньшее количество векторов а потом dbscan (для окончательного разделения)

# Пробуем Spectral Clustering

# я попробовал все возможные алгоритмы, и ни один не дал результат. возможно я не правильно подбираю параметры, но есть идея, я знаю что один кластер линейный,
# значит можно использовать линейную регрессию, находить точки которые в неё не вписываются (например 5-10% по максимальному среднеквадратичному отклонению),
# удалять их из датафрейма,и повторять до тех пор пока средняя квадратичная ошибка не будет меньше некоторого значения или просто какое-то количество итераций

# я уже начал писать код, но подумал что может что-то подобное уже кто-то делал, проверил ещё разок и нашёл алгоритм RANSAC https://ru.wikipedia.org/wiki/RANSAC
# алгоритм действия там абсолютно другой, но мне он нравится, похож на генетический алгоритм (а я как раз в последнее время с ними игрался ломал голову с библиотекой DEAP https://deap.readthedocs.io/en/master)

ransac_model = RANSACRegressor(estimator=LinearRegression(),
                               min_samples=30,
                               residual_threshold=0.18,
                               max_trials=5000)
X = data[["X"]].values
Y = data["Y"].values

ransac_model.fit(X,Y)

linear_mask = ransac_model.inlier_mask_
data["kluster_key"] = np.where(linear_mask,1,0)
# 1 - где линейный

plt.scatter(
    data['X'], data['Y'],
    c=['red' if k == 1 else 'black' for k in data['kluster_key']]
)

plt.title('Результаты кластеризации RANSAC')
plt.xlabel('X')
plt.ylabel('Y')

plt.show()
# так как метод имеет внутри себя random то не всегда получаются одинаковые кластеры, у меня часто концы линии теряют пару точек (они явно нелинейны)
# (можно зафиксировать random state в момент создания RANSACRegressor) но в рабочих задачах мне кажется это не имеет смысла, поэтому я так делать не стал

#          == == == == == 2 == == == == ==          == == == == == 2 == == == == ==          == == == == == 2 == == == == ==          == == == == == 2 == == == == ==          == == == == == 2 == == == == ==          == == == == == 2 == == == == ==

#Любым способом выделите линейную часть выборки.
#Для этой линейной части выполните задачу регрессии.

linear_regression_model = ransac_model.estimator_
print(f" уравнение: y = {linear_regression_model.coef_[0]:.4f} * x + {linear_regression_model.intercept_:.4f}")

plt.scatter(
    data['X'], data['Y'],
    c=['red' if k == 1 else 'black' for k in data['kluster_key']]
)
x_min = data['X'].min()
x_max = data['X'].max()

x_line = np.array([x_min, x_max]).reshape(-1, 1)
y_line = linear_regression_model.predict(x_line)

plt.plot(
    [x_min, x_max],
    y_line,
    c = 'blue',
    linewidth=2,
    label=f'Линия регрессии: y = {linear_regression_model.coef_[0]:.2f}x + {linear_regression_model.intercept_:.2f}'
)

plt.title('кластеризованные данные с линией регрессии')
plt.xlabel('X')
plt.ylabel('Y')

plt.show()

data_cleated = data[data['kluster_key'] == 1].copy()

plt.scatter(
    data_cleated['X'], data_cleated['Y'],
    c='red'
)

plt.plot(
    [x_min, x_max],
    y_line,
    c = 'blue',
    linewidth=2,
    label=f'Линия регрессии: y = {linear_regression_model.coef_[0]:.2f}x + {linear_regression_model.intercept_:.2f}'
)

plt.title('очищенные от синусоид данные с линией регрессии')
plt.xlabel('X')
plt.ylabel('Y')

plt.show()
