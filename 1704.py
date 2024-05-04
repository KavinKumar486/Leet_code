s = "SELECT e.employee_id,e.name,reports_count,average_age FROM (SELECT e.employee_id,e.name,(SELECT COUNT(e2.reports_to) FROM employees e2 WHERE e2.reports_to = e.employee_id) AS reports_count,(SELECT ROUND(AVG(e3.age)) FROM employees e3 WHERE e3.reports_to = e.employee_id) AS average_ageFROM employees e)AS e WHERE reports_count > 0 ORDER BY e.employee_id;"
s=s.lower()
print(s)

