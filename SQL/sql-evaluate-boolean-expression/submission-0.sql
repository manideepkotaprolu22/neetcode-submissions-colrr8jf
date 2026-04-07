-- Write your query below
select e.left_operand,e.operator,e.right_operand, 
    case
    WHEN e.operator = '>' THEN v1.value > v2.value
    WHEN e.operator = '<' THEN v1.value < v2.value
    WHEN e.operator = '=' THEN v1.value = v2.value
    end as value
    from expressions as e join variables as v1 on e.left_operand = v1.name
                          join variables as v2 on e.right_operand = v2.name;
