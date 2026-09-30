-- DAD 220 portfolio adaptation. Use existing Customers, Orders, and RMA tables.
-- Expected keys: Customers.CustomerID; Orders.OrderID and CustomerID;
-- RMA.RMAID and OrderID. Orders has SKU, Customers has State.

-- Orders by customer state. Order counts are not unique-customer counts.
SELECT c.State, COUNT(*) AS OrderCount
FROM Customers c JOIN Orders o ON c.CustomerID = o.CustomerID
GROUP BY c.State ORDER BY OrderCount DESC, c.State;

-- Return records by state.
SELECT c.State, COUNT(*) AS ReturnRecords
FROM RMA r JOIN Orders o ON r.OrderID = o.OrderID
JOIN Customers c ON o.CustomerID = c.CustomerID
GROUP BY c.State ORDER BY ReturnRecords DESC, c.State;

-- Each product's share of all return records, not its return rate among sales.
SELECT o.SKU, COUNT(*) AS ReturnRecords,
       ROUND(100.0 * COUNT(*) / NULLIF((SELECT COUNT(*) FROM RMA), 0), 2) AS ShareOfReturnsPct
FROM RMA r JOIN Orders o ON r.OrderID = o.OrderID
GROUP BY o.SKU ORDER BY ReturnRecords DESC, o.SKU;

-- Return rate using distinct order IDs, avoiding duplicate RMA inflation.
SELECT o.SKU, COUNT(DISTINCT o.OrderID) AS Orders,
       COUNT(DISTINCT r.OrderID) AS ReturnedOrders,
       ROUND(100.0 * COUNT(DISTINCT r.OrderID) / NULLIF(COUNT(DISTINCT o.OrderID), 0), 2) AS ReturnedOrderPct
FROM Orders o LEFT JOIN RMA r ON o.OrderID = r.OrderID
GROUP BY o.SKU ORDER BY ReturnedOrderPct DESC, o.SKU;
