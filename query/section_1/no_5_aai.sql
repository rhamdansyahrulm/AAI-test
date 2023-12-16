-- =============================================================================================================
-- Bonus ::	return the only member with the largest claimt amount as per question 2.
-- =============================================================================================================

SELECT 
  member_id,
  name,
  SUM(amount) as total_amount
FROM
  `voltaic-reducer-399714.TestAAI.admission_payment`
GROUP BY 
  member_id, name
ORDER BY
  total_amount DESC
LIMIT 1;