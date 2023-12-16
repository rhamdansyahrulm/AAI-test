-- =============================================================================================================
-- 3	Find the member with cumulative amount claimed more than 200
-- =============================================================================================================
SELECT 
  member_id,
  name,
  SUM(amount) as total_amount
FROM
  `voltaic-reducer-399714.TestAAI.admission_payment`
GROUP BY 
  member_id, name
HAVING
  total_amount > 200;