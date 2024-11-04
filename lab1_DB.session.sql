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
SELECT SUM(Стипендія) AS ЗагальнаСумаСтипендій FROM sportsmen;
SELECT MIN(Стипендія) AS МiнiмальнаСтипендія FROM sportsmen;
SELECT MAX(Стипендія) AS МаксимальнаСтипендія FROM sportsmen;
SELECT COUNT(ПІБ) AS КiлькiстьСпортсменiв FROM sportsmen;

-------------
SELECT Тренер, COUNT(ПІБ) AS КiлькiстьСпортсменiв
FROM sportsmen 
GROUP BY Тренер;

SELECT Тренер, MIN(Стипендія) AS МаксимальнаСтипендія
FROM sportsmen 
GROUP BY Тренер
HAVING МаксимальнаСтипендія > 3900;

-------------
SELECT ПІБ
FROM Sportsmen AS s
WHERE EXISTS (
    SELECT 1
    FROM Participation_in_competitions AS p
    WHERE p.Спортсмен = s.Номер_посвідчення
      AND p.Зайняте_місце = 1
);

SELECT ПІБ, Рейтинг
FROM Sportsmen
WHERE Рейтинг > (
    SELECT AVG(Рейтинг)
    FROM Sportsmen
);

SELECT ПІБ, Рейтинг
FROM Sportsmen
WHERE Рейтинг > (SELECT AVG(Рейтинг) FROM Coaches);

INSERT INTO Sportsmen (Номер_посвідчення, ПІБ, Дата_народження, Стать, Рівень_майстерності, Тренер, Рейтинг, Стипендія, Адреса, Мобільний_телефон, Домашній_телефон)
VALUES (678902, 'Новаченко Олег Олегович', '2004-04-25', 'ч', '1Р', 
        (SELECT Id FROM Coaches ORDER BY Рейтинг DESC LIMIT 1), 
        950, 2000.00, 'Черкаси, вул. Героев, 5', '0506789023', '0472678902');

UPDATE Sportsmen
SET Стипендія = Стипендія * 1.1
WHERE Рейтинг < (SELECT AVG(Рейтинг) FROM Sportsmen);

DELETE FROM Sportsmen
WHERE Номер_посвідчення NOT IN (SELECT Спортсмен FROM Participation_in_competitions);
