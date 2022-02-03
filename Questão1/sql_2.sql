select c.id, c.name as categories, sum(o.units_sold) 
from categories c
inner join products p 
on c.id = p.id_categories
inner join orders_products o
on p.id = o.product_id
group by c.id
order by sum(o.units_sold) desc
limit 4;