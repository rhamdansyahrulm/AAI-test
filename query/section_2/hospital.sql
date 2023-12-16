-- =============================================================================================================
-- hospital
-- =============================================================================================================
SELECT 
  hospital_name,
  SUM(amount) as total_amount,
  count(hospital_name) as frequency
FROM
  `voltaic-reducer-399714.TestAAI.admission_payment`
GROUP BY 
  hospital_name
ORDER BY 
  total_amount DESC;