#1
SELECT name, contact_name, contact_number FROM customer WHERE address = 'Hanoi';
#2
SELECT * FROM products WHERE quantity > 50 AND price > 2000000;
#3
SELECT name
    FROM products
    LEFT JOIN order_detail
    ON products.id = order_detail.product_id
    WHERE product_id is NULL;

#4
SELECT * FROM products ORDER BY price DESC LIMIT 1; # Chỉ lấy được 1 cái, có thể nhiều cái bằng nhau
#5
SELECT employee.id, employee.name, count(order.id) as sales
    FROM employee
    INNER JOIN `order`
    ON employee.id = `order`.employee_id
    WHERE purchase_at between '2022-01-01' and '2022-03-31'
    GROUP BY employee.id ORDER BY sales DESC LIMIT 1;
#6
SELECT employee.id, employee.name, count(order.id) as sales
    FROM employee
    INNER JOIN `order`
    ON employee.id = `order`.employee_id
    WHERE purchase_at between '2022-01-01' and '2022-03-31'
    GROUP BY employee.id ORDER BY sales DESC
