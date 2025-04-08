import numpy as np
from scipy import stats

import numpy as np
from scipy import stats


class task_solver:
    def __init__(self, N, R, alpha=0.05):
        """
        Инициализация анализатора статистических данных

        Parameters:
        N (array-like): Массив значений нагрузки
        R (array-like): Массив значений несущей способности
        alpha (float): Уровень значимости (по умолчанию 0.05)
        """
        self.N = np.array(N)
        self.R = np.array(R)
        self.alpha = alpha
        self.results = {
            'outliers': None,
            'variances': None,
            'means': None,
            'normality': None
        }

    def analyze(self):
        """Выполняет все статистические проверки"""
        self.results['outliers'] = self._check_outliers()
        self.results['variances'] = self._check_variances()
        self.results['means'] = self._check_means()
        self.results['normality'] = self._check_normality()
        return self.results

    def _check_outliers(self):
        """Проверка крайних значений на выбросы (критерий Ирвина)"""

        def check(data):
            sorted_data = np.sort(data)
            s = np.std(data, ddof=1)
            lambda_min = abs(sorted_data[0] - sorted_data[1]) / s
            lambda_max = abs(sorted_data[-1] - sorted_data[-2]) / s
            lambda_crit = 1.5

            return {
                'min_value': float(sorted_data[0]),
                'max_value': float(sorted_data[-1]),
                'lambda_min': float(lambda_min),
                'lambda_max': float(lambda_max),
                'is_min_outlier': lambda_min > lambda_crit,
                'is_max_outlier': lambda_max > lambda_crit
            }

        return {
            'N': check(self.N),
            'R': check(self.R)
        }

    def _check_variances(self):
        """Проверка равенства дисперсий (F-тест)"""
        var_N = np.var(self.N, ddof=1)
        var_R = np.var(self.R, ddof=1)
        F = var_N / var_R if var_N > var_R else var_R / var_N
        df1 = len(self.N) - 1
        df2 = len(self.R) - 1
        F_crit = stats.f.ppf(1 - self.alpha / 2, df1, df2)
        p_value = 2 * min(stats.f.cdf(F, df1, df2), 1 - stats.f.cdf(F, df1, df2))

        return {
            'var_N': float(var_N),
            'var_R': float(var_R),
            'F': float(F),
            'F_crit': float(F_crit),
            'p_value': float(p_value),
            'equal_variances': F <= F_crit
        }

    def _check_means(self):
        """Проверка равенства средних (t-тест Уэлча)"""
        t, p = stats.ttest_ind(self.N, self.R, equal_var=False)
        t_crit = stats.t.ppf(1 - self.alpha / 2, min(len(self.N), len(self.R)) - 1)

        return {
            'mean_N': float(np.mean(self.N)),
            'mean_R': float(np.mean(self.R)),
            't': float(t),
            't_crit': float(t_crit),
            'p_value': float(p),
            'equal_means': abs(t) <= t_crit
        }

    def _check_normality(self):
        """Проверка нормальности распределения (Шапиро-Уилк)"""

        def check(data):
            w, p = stats.shapiro(data)
            return {
                'W': float(w),
                'p_value': float(p),
                'is_normal': p >= self.alpha
            }

        return {
            'N': check(self.N),
            'R': check(self.R)
        }

    def print_results(self):
        """Выводит результаты анализа в читаемом формате"""
        if not all(self.results.values()):
            raise ValueError("Сначала выполните analyze()")

        print("Результаты статистического анализа:")

        # Вывод проверки выбросов
        outliers = self.results['outliers']
        print("\n1. Проверка крайних значений на выбросы:")
        for name in ['N', 'R']:
            data = outliers[name]
            print(f"\nДля {name}:")
            print(f"Минимальное значение: {data['min_value']}, λ = {data['lambda_min']:.2f}")
            print(f"Максимальное значение: {data['max_value']}, λ = {data['lambda_max']:.2f}")
            print("Вывод:")
            print(f"Минимальное значение {'ЯВЛЯЕТСЯ' if data['is_min_outlier'] else 'НЕ является'} выбросом")
            print(f"Максимальное значение {'ЯВЛЯЕТСЯ' if data['is_max_outlier'] else 'НЕ является'} выбросом")

        # Вывод проверки дисперсий
        var = self.results['variances']
        print("\n2. Проверка равенства дисперсий:")
        print(f"Дисперсия N: {var['var_N']:.2f}, Дисперсия R: {var['var_R']:.2f}")
        print(f"F-статистика: {var['F']:.2f}, Критическое значение F: {var['F_crit']:.2f}")
        print(f"p-value: {var['p_value']:.4f}")
        print("Вывод:")
        print("Дисперсии НЕ равны" if not var['equal_variances'] else "Дисперсии равны")

        # Вывод проверки средних
        means = self.results['means']
        print("\n3. Проверка равенства средних:")
        print(f"Среднее N: {means['mean_N']:.2f}, Среднее R: {means['mean_R']:.2f}")
        print(f"t-статистика: {means['t']:.2f}, Критическое значение t: ±{means['t_crit']:.2f}")
        print(f"p-value: {means['p_value']:.4f}")
        print("Вывод:")
        print("Средние НЕ равны" if not means['equal_means'] else "Средние равны")

        # Вывод проверки нормальности
        norm = self.results['normality']
        print("\n4. Проверка нормальности распределения:")
        for name in ['N', 'R']:
            data = norm[name]
            print(f"\nДля {name}: W = {data['W']:.3f}, p-value = {data['p_value']:.4f}")
            print("Вывод:")
            print("Распределение НЕ нормальное" if not data['is_normal'] else "Распределение нормальное")



