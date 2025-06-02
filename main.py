"""Main module for the Gym Membership Management System."""

from membership import Membership
from utils import calculate_cost

def main():
    """Handles user interaction and input/output."""
    try:
        print("Available Plans:")
        for plan, cost in Membership.plans.items():
            print(f"- {plan}: ${cost}")

        plan = input("Select a membership plan: ").strip()
        if not Membership.is_valid_plan(plan):
            print("Invalid plan selected.")
            print(-1)
            return

        print("Available additional features:")
        for feat, cost in Membership.additional_features.items():
            print(f"- {feat}: ${cost}")
        print("Premium Features (extra cost):", ", ".join(Membership.premium_features))

        features_input = input("Enter additional features separated by comma: ").strip()
        features = [f.strip() for f in features_input.split(",")] if features_input else []

        group_input = input("Number of members (1 for individual): ").strip()
        if not group_input.isdigit() or int(group_input) < 1:
            print("Invalid number of members.")
            print(-1)
            return
        group_size = int(group_input)

        total_cost = calculate_cost(plan, features, group_size)
        if total_cost == -1:
            print("Invalid selections made.")
            print(-1)
            return

        print(f"\nSelected Plan: {plan}")
        print(f"Features: {', '.join(features) if features else 'None'}")
        print(f"Group Size: {group_size}")
        print(f"Total Cost: ${total_cost}")

        confirm = input("Confirm membership? (yes/no): ").strip().lower()
        if confirm == "yes":
            print(total_cost)
        else:
            print("Membership canceled.")
            print(-1)
    except ValueError as e:
        print("Input error:", e)
        print(-1)

if __name__ == "__main__":
    main()
