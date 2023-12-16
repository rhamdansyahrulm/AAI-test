-- =============================================================================================================
-- 2	Return the ordered claim amount on monthly basis per member
-- =============================================================================================================
SELECT 
  member_id,
  FORMAT_DATE('%B', DATE(EXTRACT(YEAR FROM admission_date), EXTRACT(MONTH FROM admission_date), 1)) as admission_month,
  SUM(amount) as total_amount
FROM
  `voltaic-reducer-399714.TestAAI.admission_payment`
GROUP BY 
  member_id, admission_month
ORDER BY
  member_id, admission_month DESC;