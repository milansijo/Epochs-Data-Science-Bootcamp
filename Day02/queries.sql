#1
SELECT p.ProductName,
SUM(od.Quantity) AS
TotalQuantitySold FROM "Order Details" od
JOIN products p
ON od.ProductID=p.ProductID
GROUP BY p.ProductName
ORDER BY TotalQuantitySold DESC LIMIT 10;

#2
SELECT c.CompanyName,ROUND(SUM(od.UnitPrice*od.Quantity*(1-od.Discount)),2) AS Revenue
FROM Customers c
JOIN Orders o
ON c.CustomerID=o.CustomerID
JOIN "Order Details" od
ON o.OrderID=od.OrderID
GROUP BY c.CompanyName
ORDER BY Revenue DESC LIMIT 10;

#3
SELECT strftime('%Y-%m',o.OrderDate) AS Month,
ROUND(SUM(od.UnitPrice*od.Quantity*(1-od.Discount)),2) AS Sales
FROM Orders o
JOIN "Order Details" od
ON o.OrderID=od.OrderID
GROUP BY Month
ORDER BY Month;

#4
SELECT c.CategoryName,
ROUND(SUM(od.UnitPrice*od.Quantity*(1-od.Discount)),2) AS Revenue
FROM Categories c
JOIN Products p
ON c.CategoryID=p.CategoryID
JOIN "Order Details" od
ON p.ProductID=od.ProductID
GROUP BY c.CategoryName
ORDER BY Revenue DESC;

#5
SELECT c.CompanyName,
COUNT(o.OrderID) AS NumberOfOrders
FROM Customers c
JOIN Orders o
ON c.customerID=o.CustomerID
GROUP BY c.CompanyName
ORDER BY NumberOfOrders DESC;