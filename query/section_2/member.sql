-- =============================================================================================================
-- member
-- =============================================================================================================
WITH member_status AS (
  SELECT 
    m.member_id,
    ap.name,
    m.balance,
    SUM(ap.amount) AS total_amount,
    CASE WHEN m.balance >= SUM(ap.amount) THEN 'N' ELSE 'Y' END AS status
  FROM
    `voltaic-reducer-399714.TestAAI.members` m
  LEFT JOIN
    `voltaic-reducer-399714.TestAAI.admission_payment` ap
  ON
    m.member_id = ap.member_id
  GROUP BY 
    m.member_id, ap.name, m.balance
)

SELECT * FROM member_status;