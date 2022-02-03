select c.name, SUM(p.amount) 
from categories c
inner join products p 
on c.id = p.id_categories
group by c.id;