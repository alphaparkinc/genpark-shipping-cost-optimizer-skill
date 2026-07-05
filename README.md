# shipping-cost-optimizer-skill

> **GenPark AI Agent Skill** -- Multi-carrier cost and speed logistics optimizer.

## Quick Start

```python
from client import ShippingCostOptimizerClient
client = ShippingCostOptimizerClient()
res = client.optimize_options(3.0, {"length": 5, "width": 5, "height": 5}, "90210")
print(res["best_cost_option"])
```
