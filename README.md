# Тесты, проверяющие, что по треку заказа можно получить данные о заказе при создании заказа в Яндекс.Самокаты с помощью API Яндекс.Самокаты
- Для запуска тестов должны быть установлены пакеты pytest и requests
- Запуск всех тестов выполняется командой pytest

![**Скриншот результата выполнения теста** ]
(https://drive.google.com/file/d/1W9qB0YnrpX-y07tz-2xl5DdIVk2f5JUB/view?usp=sharing) 

## SQL-запросы

Работа с базой данных

Задание 1

SELECT c.login,
COUNT(*) as ord_amount
FROM "Couriers" AS c
JOIN "Orders" AS o ON o."courierId" = c.id
WHERE o."inDelivery" = true 
GROUP BY c.login

Задание 2

SELECT track, 
CASE
WHEN finished == true THEN 2
WHEN canсelled == true THEN -1
WHEN inDelivery == true THEN 1
ELSE 0
END AS status
FROM "Orders"


