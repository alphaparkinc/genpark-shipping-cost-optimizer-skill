"""
example_usage.py -- Demonstrates ShippingCostOptimizerClient
"""
from client import ShippingCostOptimizerClient

def main():
    client = ShippingCostOptimizerClient()
    result = client.optimize_options(
        weight_lbs=4.0,
        dimensions={"length": 10, "width": 8, "height": 6},
        destination_zip="10001"
    )
    print("[Shipping Cost Optimizer Result]")
    print(f"Cheapest: {result['best_cost_option']['carrier']} (${result['best_cost_option']['cost']})")
    print(f"Fastest: {result['best_speed_option']['carrier']} (${result['best_speed_option']['cost']})")
    print(f"Savings Potential: ${result['potential_savings']}")

if __name__ == "__main__":
    main()
