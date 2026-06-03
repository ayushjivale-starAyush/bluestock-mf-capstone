-- 1. Top 5 funds by AUM
SELECT scheme_name, aum_crore
FROM 07_scheme_performance_cleaned
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average 1-year return
SELECT AVG(return_1yr_pct) AS avg_1yr_return
FROM 07_scheme_performance_cleaned;

-- 3. Funds with expense ratio below 1%
SELECT scheme_name, expense_ratio_pct
FROM 07_scheme_performance_cleaned
WHERE expense_ratio_pct < 1;

-- 4. Count funds by risk grade
SELECT risk_grade, COUNT(*) AS total_funds
FROM 07_scheme_performance_cleaned
GROUP BY risk_grade;

-- 5. Top 5 Sharpe ratio funds
SELECT scheme_name, sharpe_ratio
FROM 07_scheme_performance_cleaned
ORDER BY sharpe_ratio DESC
LIMIT 5;

-- 6. Top Alpha funds
SELECT scheme_name, alpha
FROM 07_scheme_performance_cleaned
ORDER BY alpha DESC
LIMIT 5;

-- 7. Average NAV
SELECT AVG(nav)
FROM 02_nav_history_cleaned;

-- 8. Transaction count by state
SELECT state, COUNT(*)
FROM 08_investor_transactions_cleaned
GROUP BY state;

-- 9. Transaction amount by type
SELECT transaction_type, SUM(amount_inr)
FROM 08_investor_transactions_cleaned
GROUP BY transaction_type;

-- 10. Count investors by KYC status
SELECT kyc_status, COUNT(*)
FROM 08_investor_transactions_cleaned
GROUP BY kyc_status;