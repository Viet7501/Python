INSERT INTO person VALUES ('Duy', 'Tang', 2001-12-12);
;-- -. . -..- - / . -. - .-. -.--
INSERT INTO person VALUES (6, 'Duy', 'Tang', 2001-12-12);
;-- -. . -..- - / . -. - .-. -.--
INSERT INTO person VALUES (id,'Duy', 'Tang', 2001-12-12);
;-- -. . -..- - / . -. - .-. -.--
SELECT * FROM person;
;-- -. . -..- - / . -. - .-. -.--
SELECT COUNT(*) AS Dem FROM person WHERE Date_of_birth >= '2001-05-05';
;-- -. . -..- - / . -. - .-. -.--
INSERT INTO person(First_Name, Last_Name, Date_of_birth) VALUES ('Duy', 'Tang', '2001-12-12');
;-- -. . -..- - / . -. - .-. -.--
ALTER TABLE customer AUTO_INCREMENT = 99;
;-- -. . -..- - / . -. - .-. -.--
ALTER TABLE customer AUTO_INCREMENT = 1;
;-- -. . -..- - / . -. - .-. -.--
select * FROM customer;
;-- -. . -..- - / . -. - .-. -.--
SELECT name FROM products WHERE price = max(price);
;-- -. . -..- - / . -. - .-. -.--
SELECT * FROM products ORDER BY price;
;-- -. . -..- - / . -. - .-. -.--
SELECT * FROM products ORDER BY price DESC;
;-- -. . -..- - / . -. - .-. -.--
SELECT * FROM products ORDER BY price DESC LIMIT 3;
;-- -. . -..- - / . -. - .-. -.--
SELECT name FROM employee WHERE id = 2;
;-- -. . -..- - / . -. - .-. -.--
SELECT COUNT(employee_id) FROM `order`;
;-- -. . -..- - / . -. - .-. -.--
SELECT DISTINCT COUNT(employee_id) FROM `order`;
;-- -. . -..- - / . -. - .-. -.--
SELECT COUNT(DISTINCT employee_id) FROM `order`;
;-- -. . -..- - / . -. - .-. -.--
SELECT employee_id, count(employee_id)
    FROM `order`
    GROUP BY employee_id;
;-- -. . -..- - / . -. - .-. -.--
SELECT employee_id, count(employee_id) AS doanhthu
    FROM `order`
    GROUP BY employee_id;
;-- -. . -..- - / . -. - .-. -.--
SELECT name.employee, count(employee_id) AS doanhthu
    FROM order, employee
    GROUP BY employee_id;
;-- -. . -..- - / . -. - .-. -.--
SELECT name, count(employee_id) AS doanhthu
    FROM order, employee
    GROUP BY employee_id;
;-- -. . -..- - / . -. - .-. -.--
SELECT employee.name, count(employee_id) AS doanhthu
    FROM `order`
    INNER JOIN employee e on `order`.employee_id = e.id
    GROUP BY employee_id;
;-- -. . -..- - / . -. - .-. -.--
SELECT employee.name, count(employee_id) AS doanhthu
    FROM `order`, employee
    GROUP BY employee_id;
;-- -. . -..- - / . -. - .-. -.--
SELECT employee.name, count(employee_id) AS doanhthu
    FROM `order`, employee
    GROUP BY employee_id, employee.name;
;-- -. . -..- - / . -. - .-. -.--
SELECT DISTINCT employee.name, count(employee_id) AS doanhthu
    FROM `order`, employee
    GROUP BY employee_id, employee.name;
;-- -. . -..- - / . -. - .-. -.--
SELECT  employee.name, count(employee_id) AS doanhthu
    FROM `order`, employee
    GROUP BY  employee_id, employee.name;
;-- -. . -..- - / . -. - .-. -.--
SELECT employee.name;
;-- -. . -..- - / . -. - .-. -.--
SELECT  employee.name, count(employee_id) AS sales
    FROM `order`, employee
    GROUP BY  employee_id, employee.name;
;-- -. . -..- - / . -. - .-. -.--
SELECT  count(employee_id) AS sales
    FROM `order`
    GROUP BY  employee_id;
;-- -. . -..- - / . -. - .-. -.--
SELECT  employee.name, count(employee_id) AS sales
    FROM `order`
    INNER JOIN employee ON employee.name
    GROUP BY  employee_id, employee.name;
;-- -. . -..- - / . -. - .-. -.--
SELECT  employee.name, count(employee_id) AS sales
    FROM `order`
    INNER JOIN employee ON employee.id = `order`.id
    GROUP BY  employee_id;
;-- -. . -..- - / . -. - .-. -.--
SELECT  employee.name, count(employee_id) AS sales
    FROM `order`
    INNER JOIN employee ON employee.id = `order`.id
    GROUP BY  employee_id, employee.name;
;-- -. . -..- - / . -. - .-. -.--
SELECT  employee.name, count(employee_id) AS sales
    FROM `order`
    INNER JOIN employee ON employee.id = `order`.id;
;-- -. . -..- - / . -. - .-. -.--
SELECT  employee.name, count(employee_id) AS sales
    FROM `order`
    INNER JOIN employee ON employee.id = `order`.id
    GROUP BY employee.name, sales;
;-- -. . -..- - / . -. - .-. -.--
SELECT  employee.name, count(employee_id) AS sales
    FROM `order`
    INNER JOIN employee ON employee.id = `order`.id
    GROUP BY employee.name;
;-- -. . -..- - / . -. - .-. -.--
SELECT  employee.name, count(employee_id) AS sales
    FROM `order`
    INNER JOIN employee ON employee.id = `order`.id
    GROUP BY employee.name, count(`order`.employee.id);
;-- -. . -..- - / . -. - .-. -.--
SELECT  employee.name, count(employee_id) AS sales
    FROM `order`, employee
    INNER JOIN employee ON employee.id = `order`.id between 01-01-2022 and 03-31-2022
    GROUP BY employee.name;
;-- -. . -..- - / . -. - .-. -.--
SELECT  employee.name, count(employee_id) AS sales
    FROM `order`, employee
    GROUP BY employee.name;
;-- -. . -..- - / . -. - .-. -.--
SELECT count(employee_id) AS doanhthu
    FROM `order`
    GROUP BY employee_id;
;-- -. . -..- - / . -. - .-. -.--
SELECT name
    FROM employee
    INNER JOIN `order`
    ON employee.id = `order`.employee_id;
;-- -. . -..- - / . -. - .-. -.--
SELECT distinct name
    FROM employee
    INNER JOIN `order`
    ON employee.id = `order`.employee_id;
;-- -. . -..- - / . -. - .-. -.--
SELECT DISTINCT name, count(order.employee.id)
    FROM employee
    INNER JOIN `order`
    ON employee.id = `order`.employee_id;
;-- -. . -..- - / . -. - .-. -.--
SELECT name, count(order.employee.id)
    FROM employee
    INNER JOIN `order`
    ON employee.id = `order`.employee_id
    GROUP BY name;
;-- -. . -..- - / . -. - .-. -.--
SELECT name, count(order.employee.id) as sales
    FROM employee
    INNER JOIN `order`
    ON employee.id = `order`.employee_id
    GROUP BY name;
;-- -. . -..- - / . -. - .-. -.--
SELECT employee.id, name, count(order.employee.id) as sales
    FROM employee
    INNER JOIN `order`
    ON employee.id = `order`.employee_id
    GROUP BY name;
;-- -. . -..- - / . -. - .-. -.--
SELECT employee.id, name, count(order.employee.id) as sales
    FROM employee
    INNER JOIN `order`
    ON employee.id = `order`.employee_id between 01-01-2022 and 03-31-2022
    GROUP BY name;
;-- -. . -..- - / . -. - .-. -.--
SELECT employee.id, name, count(order.employee.id) as sales
    FROM employee
    INNER JOIN `order`
    ON employee.id = `order`.employee_id
    GROUP BY name between 01-01-2022 and 03-31-2022;
;-- -. . -..- - / . -. - .-. -.--
SELECT employee.id, name, count(order.employee.id between 01-01-2022 and 03-31-2022) as sales
    FROM employee
    INNER JOIN `order`
    ON employee.id = `order`.employee_id
    GROUP BY name;
;-- -. . -..- - / . -. - .-. -.--
SELECT employee.id, name, count(order.employee.id WHERE purchase_at between 01-01-2022 and 03-31-2022) as sales
    FROM employee
    INNER JOIN `order`
    ON employee.id = `order`.employee_id
    GROUP BY name;
;-- -. . -..- - / . -. - .-. -.--
SELECT employee.id, name, count(order.employee.id WHERE order.purchase_at between 01-01-2022 and 03-31-2022) as sales
    FROM employee
    INNER JOIN `order`
    ON employee.id = `order`.employee_id
    GROUP BY name;
;-- -. . -..- - / . -. - .-. -.--
SELECT employee.id, name, count(order.employee_id WHERE order.purchase_at between 01-01-2022 and 03-31-2022) as sales
    FROM employee
    INNER JOIN `order`
    ON employee.id = `order`.employee_id
    GROUP BY name;
;-- -. . -..- - / . -. - .-. -.--
SELECT employee.id, name, count(order.employee_id ) as sales
    FROM `order`
    INNER JOIN `employee`
    ON employee.id = `order`.employee_id
    GROUP BY name;
;-- -. . -..- - / . -. - .-. -.--
SELECT name
    FROM products;
;-- -. . -..- - / . -. - .-. -.--
NOT ;
;-- -. . -..- - / . -. - .-. -.--
SELECT name
    FROM products
    INNER JOIN order_detail
    ON products.id = order_detail.product_id
    WHERE product_id is NOT NULL;
;-- -. . -..- - / . -. - .-. -.--
SELECT name
    FROM products
    INNER JOIN order_detail
    ON products.id = order_detail.product_id
    WHERE product_id is NULL;
;-- -. . -..- - / . -. - .-. -.--
SELECT name
    FROM products
    LEFT JOIN order_detail
    ON products.id = order_detail.product_id
    WHERE product_id is NULL;
;-- -. . -..- - / . -. - .-. -.--
SELECT employee.id, name, count(order.employee_id ) as sales
    FROM employee
    INNER JOIN `order`
    ON employee.id = `order`.employee_id
    GROUP BY name;
;-- -. . -..- - / . -. - .-. -.--
SELECT employee.id, name, count(order.employee_id ) as sales
    FROM employee
    INNER JOIN `order`
    ON employee.id = `order`.employee_id
    WHERE '01-01-2022' < purchase_at < '03-31-2022'
    GROUP BY name;
;-- -. . -..- - / . -. - .-. -.--
SELECT employee.id, name, count(order.employee_id ) as sales
    FROM employee
    INNER JOIN `order`
    ON employee.id = `order`.employee_id
    WHERE '2022-01-01' < purchase_at < '2022-03-31'
    GROUP BY name;
;-- -. . -..- - / . -. - .-. -.--
SELECT employee.id, name, count(order.employee_id ) as sales
    FROM employee
    INNER JOIN `order`
    ON employee.id = `order`.employee_id
    WHERE '2022-01-01' < purchase_at < '2022-03-31'
    GROUP BY name LIMIT 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT * FROM products ORDER BY price DESC LIMIT 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT employee.id, name, count(order.employee_id ) as sales
    FROM employee
    INNER JOIN `order`
    ON employee.id = `order`.employee_id
    WHERE purchase_at between '2022-01-01' and '2022-03-31'
    GROUP BY name LIMIT 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT employee.id, employee.name, count(order.id ) as sales
    FROM employee
    INNER JOIN `order`
    ON employee.id = `order`.employee_id
    WHERE purchase_at between '2022-01-01' and '2022-03-31'
    GROUP BY employee.id LIMIT 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT employee.id, employee.name, count(order.id ) as sales
    FROM employee
    INNER JOIN `order`
    ON employee.id = `order`.employee_id
    WHERE purchase_at between '2022-01-01' and '2022-03-31'
    GROUP BY employee.id ORDER BY sales LIMIT 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT employee.id, employee.name, count(order.id ) as sales
    FROM employee
    INNER JOIN `order`
    ON employee.id = `order`.employee_id
    WHERE purchase_at between '2022-01-01' and '2022-03-31'
    GROUP BY employee.id ORDER BY sales DESC LIMIT 1;
;-- -. . -..- - / . -. - .-. -.--
SELECT employee.id, employee.name, count(order.id) as sales
    FROM employee
    INNER JOIN `order`
    ON employee.id = `order`.employee_id
    WHERE purchase_at between '2022-01-01' and '2022-03-31'
    GROUP BY employee.id ORDER BY sales DESC;
;-- -. . -..- - / . -. - .-. -.--
SELECT * FROM products WHERE quantity > 50 AND price > 2000000;
;-- -. . -..- - / . -. - .-. -.--
SELECT name, contact_name, contact_number FROM customer WHERE address = 'Hanoi';