# Отчет по лаборатоной работе №3. Вариант 4. Геращенко Сергей Тигранович

# Table of Contents
1. [Условие](#условие)
2. [Контекст базы данных](#контекст-базы-данных)
## Условие
Використовуючи створену БД, навести приклади використання:
1. Агрегатних функцій AVG, SUM, MIN, MAX, COUNT.
1. Операторів GROUP BY і HAVING.
1. Коригуючого підзапиту.
1. Некоригующого підзапиту.
1. Підзапитів в командах SELECT, INSERT, UPDATE, DELETE.
1. Оператора EXISTS

## Контекст базы данных
Тренери (Id (ПК), ПІБ, Рівень майстерності (1Р, КМС, МС, ЗМС, МСМК), Рейтинг). 
Спортсмени(Номер посвідчення (N 6 0, ПК), ПІБ (C 40, обов'язкове поле) Дата народження (Id (ПК), D, обов'язкове поле), Стать (ч, ж, обов'язкове поле), Рівень майстерності (1Р, КМС, МС, ЗМС, МСМК), Тренер (обов'язкове, зовнішній ключ до таблиці Тренери), Рейтинг (N 4 0 ), Стипендія (N 7 2, по умовчанням 0), Адреса (С 40, обов'язкове поле), Мобільний телефон, Домашній телефон ).
Змагання (Id (ПК), Тип , Місце проведення, Дата проведення, Обмеження за віком). 
Участь у змаганнях (Id (ПК), Змагання(ЗК), Спортсмен (ЗК), Результат (кількість завойованих очок), Зайняте місце).
## Код запросов для решения заданий лабораторной работы
```sql=1
SELECT AVG(Стипендія) AS СередняСтипендія FROM sportsmen;
SELECT SUM(Стипендія) AS ЗагальнаСумаСтипендій FROM sportsmen;
SELECT MIN(Стипендія) AS МiнiмальнаСтипендія FROM sportsmen;
SELECT MAX(Стипендія) AS МаксимальнаСтипендія FROM sportsmen;
SELECT COUNT(ПІБ) AS КiлькiстьСпортсменiв FROM sportsmen;

SELECT Тренер, COUNT(ПІБ) AS КiлькiстьСпортсменiв
FROM sportsmen 
GROUP BY Тренер;

SELECT Тренер, MIN(Стипендія) AS МiнiмальнаСтипендія
FROM sportsmen 
GROUP BY Тренер
HAVING МiнiмальнаСтипендія > 3900;

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
        950, 2000.00, 'Черкаси, вул. Героїв, 5', '0506789023', '0472678902');

SET SQL_SAFE_UPDATES = 0;
UPDATE Sportsmen
SET Стипендія = Стипендія * 1.1
WHERE Рейтинг > (
    SELECT avg_rating FROM (SELECT AVG(Рейтинг) AS avg_rating FROM Sportsmen) AS temp
);
SET SQL_SAFE_UPDATES = 1;

SET SQL_SAFE_UPDATES = 0;
DELETE FROM Sportsmen
WHERE Номер_посвідчення NOT IN (SELECT Спортсмен FROM Participation_in_competitions);
SET SQL_SAFE_UPDATES = 1;
```
### COUNT:
![Снимок экрана (516)](https://hackmd.io/_uploads/Skvi1s8-kx.png)
### GROUP BY:
![Снимок экрана (517)](https://hackmd.io/_uploads/HkKflsL-kx.png)
### GROUP BY ... HAVING:
![Снимок экрана (518)](https://hackmd.io/_uploads/r10rli8WJl.png)
### Коррелирующий подзапрос:
![Снимок экрана (519)](https://hackmd.io/_uploads/Bye2giLWke.png)
### Некоррелирующий подзапрос:
![Снимок экрана (520)](https://hackmd.io/_uploads/SyqgWjUZkg.png)
### Подзапрос в SELECT:
![Снимок экрана (521)](https://hackmd.io/_uploads/r1qQZj8Zkg.png)
### Подзапрос в INSERT:
![Снимок экрана (522)](https://hackmd.io/_uploads/HyrOZjLZyx.png)
### Подзапрос в UPDATE:
![Снимок экрана (523)](https://hackmd.io/_uploads/Bks5Wi8-kx.png)
### Подзапрос в DELETE:
![Снимок экрана (524)](https://hackmd.io/_uploads/rk31zjUZyl.png)
