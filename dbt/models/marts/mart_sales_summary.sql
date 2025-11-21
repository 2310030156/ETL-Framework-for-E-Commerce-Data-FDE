with sales as (
  select order_date, quantity, price, quantity * price as sales_amount
  from {{ ref('stg_sales') }}
)
select
  order_date,
  sum(quantity) as total_items,
  sum(sales_amount) as total_revenue
from sales
group by order_date
order by order_date
