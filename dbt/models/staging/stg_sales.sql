with raw as (
  select
    order_id,
    order_date::date as order_date,
    customer_id,
    product_id,
    quantity,
    price
  from raw.sales
)

select * from raw
