USE lab1

SELECT * FROM coaches;
SELECT * FROM sportsmen;

SELECT DISTINCT Рівень_майстерності FROM coaches;

SELECT Стать, Тренер, ПІБ
FROM sportsmen
WHERE Стать IN ('ж');

SELECT Стать, Тренер, ПІБ
FROM sportsmen
WHERE Стать = 'ж';

SELECT Стать, Тренер, ПІБ
FROM sportsmen
WHERE Стать NOT IN ('ж');

SELECT Рейтинг, Тренер, ПІБ
FROM sportsmen
WHERE Рейтинг BETWEEN 1100 AND 1600;

-----------

SELECT Рейтинг, Тренер, ПІБ
FROM sportsmen
WHERE ПІБ LIKE '%р%';

SELECT Рейтинг, Тренер, ПІБ
FROM sportsmen
WHERE ПІБ LIKE '__а%';

SELECT Рейтинг, Тренер, ПІБ
FROM sportsmen
WHERE ПІБ LIKE 'т%ч';

SELECT Рейтинг, Тренер, ПІБ
FROM sportsmen
WHERE ПІБ LIKE '%ч';

SELECT Рейтинг, Тренер, ПІБ
FROM sportsmen
WHERE ПІБ LIKE 'м%';

-----------

SELECT Рейтинг, Тренер, ПІБ
FROM sportsmen
WHERE ПІБ REGEXP 'ій|ія';

SELECT Рейтинг, Тренер, ПІБ
FROM sportsmen
WHERE ПІБ REGEXP 'Васил';

SELECT Рейтинг, Тренер, ПІБ
FROM sportsmen
WHERE ПІБ REGEXP 'ич$';

SELECT Рейтинг, Тренер, ПІБ
FROM sportsmen
WHERE Рейтинг REGEXP '^(11[0-9]{2}|16[0-9]{2})$';

SELECT Рейтинг, Тренер, ПІБ
FROM sportsmen
WHERE Рейтинг REGEXP '[6,9]';

-----------

SELECT Рейтинг, Тренер, ПІБ
FROM sportsmen
WHERE Домашній_телефон IS NULL;

-----------

SELECT Рейтинг, Тренер, ПІБ
FROM sportsmen
ORDER BY Тренер ASC;

SELECT Рейтинг, Тренер, ПІБ
FROM sportsmen
ORDER BY Тренер DESC;

SELECT Рейтинг, Тренер, ПІБ
FROM sportsmen
ORDER BY Тренер ASC, Рейтинг ASC;

-----------

SELECT Рейтинг, Тренер, ПІБ
FROM sportsmen
LIMIT 3;





------------

SELECT Стипендія FROM sportsmen;
SELECT AVG(Стипендія) AS СередняСтипендія FROM sportsmen;
SELECT SUM(Стипендія) AS СумаСтипендій FROM sportsmen;
SELECT MIN(Стипендія) AS МiнiмальнаСтипендія FROM sportsmen;
SELECT MAX(Стипендія) AS МаксимальнаСтипендія FROM sportsmen;
SELECT COUNT(Стипендія) AS КiлькiстьСтипендіатiв FROM sportsmen;

-------------
SELECT Тренер, AVG(Стипендія) AS СередняСтипендія
FROM sportsmen 
GROUP BY Тренер;

SELECT Тренер, AVG(Стипендія) AS СередняСтипендія
FROM sportsmen 
GROUP BY Тренер
HAVING СередняСтипендія > 3900;