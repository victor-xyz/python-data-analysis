# Findings

## Initial Analysis

Using the synthetic sales dataset:

- Revenue is calculated as `units × unit_price`.
- Higher-priced products can generate substantially more revenue even when their unit volume is lower.
- Regional aggregation provides a simple way to compare contribution to total revenue.
- Product-level analysis separates sales volume from monetary contribution.

## Recommended Next Steps

For a larger real-world dataset, the analysis should also consider:

1. Profit margin rather than revenue alone.
2. Discounts and returns.
3. Customer segments.
4. Time-series trends.
5. Missing and anomalous values.
6. Statistical uncertainty.
7. Operational or business constraints.

The findings in this repository are demonstrations based on synthetic data and should not be treated as real business recommendations.
