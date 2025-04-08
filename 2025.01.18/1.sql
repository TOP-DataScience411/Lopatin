1. Вывести названия стран и названия сопоставленных им столиц:

SELECT country.Name as country_name, city.Name as city_name
FROM country
INNER JOIN city
	ON country.Capital = city.id;

2. Сравнить по регионам сумму населения стран и сумму населения городов:

SELECT country.Region,
	SUM(country.Population) as country_pop,
	SUM(city.Population) as city_pop
FROM country
INNER JOIN city
	ON country.code = city.countrycode
GROUP BY country.Region;

3. Вывести десять языков, на которых разговаривает больше всего людей:

SELECT 
    Language,
    SUM((Percentage / 100) * c.Population) AS total_speakers
FROM 
    countrylanguage as cl
INNER JOIN 
    country as c
    ON cl.CountryCode = c.Code
GROUP BY 
    Language
ORDER BY 
    total_speakers DESC
LIMIT 10;

Запросы к таблицам схемы hospital

4. Вывести названия специальностей и суммарное количество дней отпусков, в которых были врачи каждой специальности; отсортировать по возрастанию суммарного количества дней отпуска:

SELECT sp.name as spec_name,
		SUM(EXTRACT(DAY FROM AGE(vac.end_date, vac.start_date))) as day_vac
FROM specializations as sp
INNER JOIN doctors_specs as ds
	ON sp.id = ds.spec_id
INNER JOIN vacations as vac
	using (doctor_id)
GROUP BY spec_name
ORDER BY day_vac;

5. Вывести округлённую до целого сумму средств, которую можно выделить на одну палату этого отделения (в зависимости от количества палат в отделении), от всех пожертвований каждому отделению; отсортировать по убыванию найденной суммы:

SELECT dep.name as dep_name, 
	ROUND(sum(d.amount) / COUNT(w.id)) as sum_ward
FROM departments as dep
JOIN donations as d
	ON dep.id = d.dep_id
JOIN wards as w
	ON dep.id = w.dep_id
GROUP BY dep.id, dep.name
ORDER BY sum_ward DESC;