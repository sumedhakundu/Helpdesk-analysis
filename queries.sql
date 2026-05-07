-- Query 1: Ticket Volume by Issue Type
SELECT issue_type, COUNT(*) AS total_tickets
FROM tickets
GROUP BY issue_type
ORDER BY total_tickets DESC;

-- Query 2: Average Resolution Time by Priority
SELECT priority, ROUND(AVG(resolution_time_hours), 2) AS avg_resolution_hours
FROM tickets
WHERE resolution_time_hours IS NOT NULL
GROUP BY priority
ORDER BY avg_resolution_hours DESC;

-- Query 3: Monthly Ticket Volume Trend
SELECT DATE_FORMAT(created_at, '%Y-%m') AS month,
       COUNT(*) AS tickets_opened
FROM tickets
GROUP BY month
ORDER BY month;

-- Query 4: Tickets by Customer Segment
SELECT customer_segment,
       COUNT(*) AS total_tickets,
       ROUND(AVG(resolution_time_hours), 2) AS avg_resolution_hours
FROM tickets
GROUP BY customer_segment
ORDER BY total_tickets DESC;

-- Query 5: Ticket Status Breakdown
SELECT status,
       COUNT(*) AS total_tickets,
       ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) AS percentage
FROM tickets
GROUP BY status
ORDER BY total_tickets DESC;
