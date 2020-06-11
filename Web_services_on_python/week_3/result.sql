use test;
set names utf8;

-- 1. Выбрать все товары (все поля)
select * from product;

-- 2. Выбрать названия всех автоматизированных складов
select * from store
where store.is_automated = 1;

-- 3. Посчитать общую сумму в деньгах всех продаж
select sum(total) from sale;

-- 4. Получить уникальные store_id всех складов, с которых была хоть одна продажа
select distinct store_id from sale;


-- 5. Получить уникальные store_id всех складов, с которых не было ни одной продажи
select store_id from store
	where store_id not in (select store_id from sale);

-- 6. Получить для каждого товара название и среднюю стоимость единицы товара avg(total/quantity), если товар не продавался, он не попадает в отчет.
select product.name, avg(sale.total/sale.quantity)
	from sale join product on
		sale.product_id = product.product_id 
        group by product.name;

-- 7. Получить названия всех продуктов, которые продавались только с единственного склада
select product.name from product join sale on
	sale.product_id = product.product_id
    group by product.name 
    having COUNT(distinct store_id) = 1;

-- 8. Получить названия всех складов, с которых продавался только один продукт
select store.name from store join sale on
	sale.store_id = store.store_id
	group by store.name 
		having COUNT(distinct product_id) = 1;

-- 9. Выберите все ряды (все поля) из продаж, в которых сумма продажи (total) максимальна (равна максимальной из всех встречающихся)
select * from sale
where total = (select max(total) from sale);

-- 10. Выведите дату самых максимальных продаж, если таких дат несколько, то самую раннюю из них
select date from sale
	group by date
    order by sum(total) DESC limit 1;
