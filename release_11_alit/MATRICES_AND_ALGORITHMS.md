# ALIT Matrices & Algorithms

## Matrix 01 — Coverage Matrix 2022-2026

| Year | Month | Payslip | Exposed Hours | Payroll Hours | Real Calendar | Health Data | Confidence |
|---|---|---|---|---|---|---|---|

Rules:
- every year has 12 rows.
- missing data cannot delete a month.
- ND != zero.

## Matrix 02 — Exposed vs Real Calendar

| Exposed Date | Exposed Code | Real Date | Real Shift | Real Hours | Rule Applied | Confidence |
|---|---|---|---|---|---|---|

Algorithm:
```python
if code == '1':
    real_date = exposed_date
    hours = '08:00-16:00'
elif code == '2':
    real_date = exposed_date
    hours = '16:00-24:00'
elif code == '3':
    real_date = exposed_date + 1
    hours = '00:00-08:00'
```

## Matrix 03 — Smonto Detection

| Date | Previous Exposed Code | Current Code | Real Night Present | Smonto Alert |
|---|---|---|---|---|

Algorithm:
```python
if previous_day.code == '3' and current_day.code in ['R','F']:
    alert = 'SMONTO-NOTTE'
```

## Matrix 04 — Payroll Crosscheck

| Month | Theoretical Night Hours | Paid Night Hours | Delta | Scenario | Confidence | Alert |
|---|---|---|---|---|---|---|

Formula:
`delta = theoretical_night_hours - paid_night_hours`

## Matrix 05 — ROL Erosion

| Month | ROL Start | Matured | Used | Expected Residual | Real Residual | Drift |
|---|---|---|---|---|---|---|

Formula:
`drift = expected_residual - real_residual`

## Matrix 06 — Compensation Masking

| Month | Minor Presence | ROL Used | Vacation Used | Transfer Italy | Suspicion Score |
|---|---|---|---|---|---|

Formula:
`suspicion = cooccurrence * recurrence * payroll_gap`

## Matrix 07 — Health Load

| Week | Night Shifts | Smonto Days | Recovery Deficit | CSI Estimate | Load Score |
|---|---|---|---|---|---|

Formula:
`CSI = (night_hours * compression_factor) / recovery_hours`

## Matrix 08 — Evidence Gravity

| Evidence | Type | Weight | Supports | Contradicts | Reliability |
|---|---|---|---|---|---|

Base weights:
- payslip = 1.00
- payroll hours = 0.95
- exposed schedule = 0.90
- timestamped photo = 0.85
- diary = 0.75
- reconstructed pattern = 0.60-0.85
- simulation = 0.35-0.70

## Matrix 09 — Adversarial Review

| Hypothesis | Supporting Evidence | Weak Point | Alternative Explanation | Survives Review |
|---|---|---|---|---|

## Matrix 10 — Professional Routing

| Finding | Accountant | Labour Consultant | Union | Lawyer | Occupational Doctor | Medico-Legal | INL/ASL |
|---|---|---|---|---|---|---|---|

Routing formula:
`routing_score = evidence_strength * professional_relevance * operational_impact`
