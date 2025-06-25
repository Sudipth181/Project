SELECT COUNT(*) FROM employee_payroll;

SELECT Fiscal_Year,Job_Title, AVG(Base_Pay) AS AverageBasePay
From employee_payroll
GROUP BY Fiscal_Year, Job_Title
ORDER BY Fiscal_Year, Job_Title;

SELECT Fiscal_Quarter, Bureau, AVG(Base_Pay) AS AverageBasePay
FROM employee_payroll
GROUP BY Fiscal_Quarter, Bureau
ORDER BY Fiscal_Quarter, Bureau;

SELECT COUNT(DISTINCT Employee_Identifier)
FROM employee_payroll;

SELECT Fiscal_Year, COUNT(*) as Count
FROM employee_payroll
GROUP BY Fiscal_Year;

SELECT Base_Pay, COUNT(*) as Salary
FROM employee_payroll
WHERE Base_Pay <= 20000
GROUP BY Base_Pay;