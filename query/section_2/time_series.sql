-- =============================================================================================================
-- Time Series
-- =============================================================================================================
SELECT 
  admission_date,
  sum(amount) as total_amount,
  count(admission_date) as frequency
FROM
  `voltaic-reducer-399714.TestAAI.admission_payment`
GROUP BY 
  admission_date
ORDER BY 
  frequency DESC;