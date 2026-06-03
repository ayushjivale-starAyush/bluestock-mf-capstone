# Data Dictionary

## 02_nav_history_cleaned.csv
- amfi_code: Unique mutual fund scheme code
- date: NAV record date
- nav: Net Asset Value of the scheme

## 08_investor_transactions_cleaned.csv
- investor_id: Unique investor identifier
- transaction_date: Date of transaction
- amfi_code: Mutual fund scheme code
- transaction_type: SIP, Lumpsum, or Redemption
- amount_inr: Transaction amount in INR
- state: Investor state
- city: Investor city
- city_tier: City classification
- age_group: Investor age group
- gender: Investor gender
- annual_income_lakh: Annual income in lakhs
- payment_mode: Payment method
- kyc_status: KYC verification status

## 07_scheme_performance_cleaned.csv
- amfi_code: Mutual fund scheme code
- scheme_name: Name of mutual fund scheme
- fund_house: AMC or fund house name
- category: Fund category
- plan: Investment plan type
- return_1yr_pct: 1-year return percentage
- return_3yr_pct: 3-year return percentage
- return_5yr_pct: 5-year return percentage
- benchmark_3yr_pct: Benchmark return over 3 years
- alpha: Excess return compared to benchmark
- beta: Volatility compared to market
- sharpe_ratio: Risk-adjusted return measure
- sortino_ratio: Downside risk-adjusted return measure
- std_dev_ann_pct: Annualized standard deviation
- max_drawdown_pct: Maximum observed loss from peak
- aum_crore: Assets under management in crore
- expense_ratio_pct: Fund expense ratio percentage
- morningstar_rating: Fund rating
- risk_grade: Risk level of fund