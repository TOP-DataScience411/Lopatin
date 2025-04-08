1. Вывести средний оклад (salary) всех сотрудников:

SELECT ROUND(AVG(salary), 2) as avg_salary
FROM doctors;


2. Вывести среднюю премию для всех сотрудников, чей доход выше среднего (взять явное значение из результата предыдущего запроса):

SELECT ROUND(AVG(premium), 2) as avg_premium 
FROM doctors 
WHERE salary > 57084.31;

Запросы к таблице vacations:

3. Вывести с сортировкой по возрастанию среднее количество дней в отпуске для каждого сотрудника:

SELECT AVG(end_date - start_date)::int as avg_vacations 
FROM vacations 
GROUP BY id 
ORDER BY avg_vacations;

4. Вывести для каждого сотрудника самый ранний год отпуска и самый поздний год отпуска с сортировкой по возрастанию разности между этими двумя значениями:

SELECT MIN(date_part('year', start_date)) as min_vacations_year, 
    MAX(date_part('year', start_date)) as max_vacations_year 
FROM vacations 
GROUP BY id 
ORDER BY (end_date - start_date);

Запросы к таблице donations:

5. Вывести сумму пожертвований за всё время для каждого отделения с сортировкой по возрастанию номеров отделений:

SELECT SUM(amount) as sum_amount 
FROM donations 
GROUP BY dep_id 
ORDER BY dep_id;

6. Вывести сумму пожертвований за каждый год для каждого спонсора с сортировкой по возрастанию номеров спонсоров и годов:

SELECT SUM(amount) as sum_amount_year 
FROM donations 
GROUP BY sponsor_id, date_part('year', date) 
ORDER BY sponsor_id, date_part('year', date);