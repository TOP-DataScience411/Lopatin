1. Вывести названия всех стран Евразии
SELECT Name 
FROM country 
WHERE Continent IN ('Asia','Europe');
2. Вывести названия регионов и стран, в которых ожидаемая продолжительность жизни меньше пятидесяти лет
SELECT Name, Region
FROM country 
WHERE LifeExpectancy < 50;
3. Вывести название самой крупной по площади страны Африки
SELECT Name
FROM country 
WHERE Continent = 'Africa' AND SurfaceArea = MAX(SurfaceArea);
4. Вывести названия пяти азиатских стран с самой низкой плотностью населения
SELECT Name 
FROM country 
WHERE Continent = 'Asia' 
ORDER BY Population / SurfaceArea
limit 5;
Запросы к таблице city

5. Вывести в порядке возрастания населения коды стран и названия городов, численность населения которых превышает пять миллионов человек
SELECT Name, CountryCode 
FROM city 
WHERE Population>5000000 
ORDER BY Population;
6. Вывести название города в Индии с самым длинным названием
      для подсчёта количества символов используйте встроенную функцию char_length()

SELECT Name 
FROM city 
WHERE MAX(char_length(name)) = char_length(name)
AND CountryCode = "IND";