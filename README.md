# Финальный проект Тиханская Виктория, 19-я когорта

## Автоматизация теста к API

Автоматизируй сценарий, который подготовили коллеги-тестировщики:
1. Клиент создает заказ.
2. Проверяется, что по треку заказа можно получить данные о заказе.

Шаги автотеста:
1. Выполнить запрос на создание заказа.
2. Сохранить номер трека заказа.
3. Выполнить запрос на получения заказа по треку заказа.
4. Проверить, что код ответа равен 200.

### Скриншот результата: 

![auto_test_sc](https://github.com/TikhanskayaV/Yandex_auto_test_and_SQL/blob/main/screenshots/auto_test.png)

## **Работа с базой данных. PostgreSQL**

Задание 1

Представь: тебе нужно проверить, отображается ли созданный заказ в базе данных.

Для этого: выведи список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true). 

### SQL-Запрос:

SELECT c.login, COUNT(o.id) AS "deliveryCount" FROM "Couriers" AS c LEFT JOIN "Orders" AS o ON c.id = o."courierId" WHERE o."inDelivery" = true GROUP BY c.login;

### Скриншот:

![sql_1_sc](https://github.com/TikhanskayaV/Yandex_auto_test_and_SQL/blob/main/screenshots/sql_1.png)

Задание 2

Ты тестируешь статусы заказов. Нужно убедиться, что в базе данных они записываются корректно.

Для этого: выведи все трекеры заказов и их статусы. 

Статусы определяются по следующему правилу:

Если поле finished == true, то вывести статус 2.

Если поле canсelled == true, то вывести статус -1.

Если поле inDelivery == true, то вывести статус 1.

Для остальных случаев вывести 0.

### SQL-Запрос:

SELECT track, CASE WHEN finished = true THEN 2 WHEN cancelled = true THEN -1 WHEN "inDelivery" = true THEN 1 ELSE 0 END AS status FROM "Orders";

### Скриншот:

![sql_2_sc](https://github.com/TikhanskayaV/Yandex_auto_test_and_SQL/blob/main/screenshots/sql_2.png)
