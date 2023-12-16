-- =============================================================================================================
-- 1	Return the registered hospital with the highest total number of claim ordered
-- =============================================================================================================
SELECT 
  hospital_name,
  SUM(amount) as total_amount
FROM
  `voltaic-reducer-399714.TestAAI.admission_payment`
GROUP BY 
  hospital_name
ORDER BY 
  total_amount DESC
LIMIT 1;