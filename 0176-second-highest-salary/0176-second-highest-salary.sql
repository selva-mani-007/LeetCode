SELECT IFNULL(
    (
        SELECT DISTINCT salary
        FROM Employee
        ORDER BY salary DESC
        LIMIT 1 OFFSET 1
    ),
    NULL
) AS SecondHighestSalary;



/*


SELECT IFNULL(
    (
        SELECT salary
        FROM (
            SELECT distinct salary, 
                   RANK() OVER (ORDER BY salary DESC) AS rnk
            FROM Employee
        ) AS t
        WHERE rnk = 2
        LIMIT 1
    ),
    NULL
) AS SecondHighestSalary;
*/
