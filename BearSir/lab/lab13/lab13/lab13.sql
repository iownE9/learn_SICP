.read data.sql

CREATE TABLE average_prices AS
  SELECT category, AVG(MSRP) AS average_price FROM products GROUP BY category;


CREATE TABLE lowest_prices AS
  SELECT store, item, MIN(price) FROM inventory GROUP BY item;


CREATE TABLE shopping_list AS
  SELECT item, store FROM lowest_prices, products
  WHERE item = name GROUP BY category HAVING MIN(MSRP / rating);


CREATE TABLE total_bandwidth AS
  SELECT sum(Mbs) FROM shopping_list, stores WHERE stores.store = shopping_list.store;

