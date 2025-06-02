"""
Gym Membership Management System

This module provides functionalities to manage gym memberships, including:
- Displaying available membership plans
- Calculating costs based on selected plans and additional features
- Applying discounts and surcharges
- Confirming membership selections
"""

# Membership plans and their costs
MEMBERSHIP_PLANS = {
    "Basic": 50,
    "Premium": 100,
    "Family": 150
}

# Additional features and their costs
ADDITIONAL_FEATURES = {
    "Personal Training": 30,
    "Group Classes": 20
}

def display_membership_plans():
    print("Available Membership Plans:")
    for plan, cost in MEMBERSHIP_PLANS.items():
        print(f"- {plan}: ${cost}/month")

def get_membership_cost(membership_plan):
    """Return the cost of the selected membership plan."""
    return MEMBERSHIP_PLANS.get(membership_plan, 0)

def add_features(selected_features):
    """Calculate the cost of additional features."""
    total_feature_cost = 0
    for feature in selected_features:
        total_feature_cost += ADDITIONAL_FEATURES.get(feature, 0)
    return total_feature_cost

def apply_group_discount(total_cost, group_size):
    """Apply a 10% discount if two or more members sign up together."""
    if group_size >= 2:
        print("Group Discount Applied: 10% off")
        return total_cost * 0.90
    return total_cost

def apply_special_offers(total_cost):
    """Apply special discounts based on total cost."""
    if total_cost > 400:
        print("Special Offer: $50 discount applied!")
        return total_cost - 50
    if total_cost > 200:
        print("Special Offer: $20 discount applied!")
        return total_cost - 20
    return total_cost

def apply_premium_surcharge(membership_plan, total_cost):
    """Apply a 15% surcharge for premium memberships."""
    if membership_plan == "Premium":
        print("Premium Membership Surcharge: 15% applied!")
        return total_cost * 1.15
    return total_cost

def validate_membership(membership_plan):
    """Check if the selected membership plan is valid."""
    if membership_plan not in MEMBERSHIP_PLANS:
        print("Error: Invalid membership plan selected.")
        return False
    return True

def confirm_membership(membership_plan, selected_features, total_cost):
    """Confirm membership details with the user."""
    print(f"Selected Plan: {membership_plan}")
    print(f"Selected Features: {', '.join(selected_features)}")
    print(f"Total Cost: ${total_cost}")
    confirm = input("Do you want to confirm? (y/n): ")
    return confirm.lower() == 'y'

def calculate_total_cost(membership_plan, selected_features, group_size=1):
    """Calculate the total cost based on selected membership, features, and discounts."""
    base_cost = get_membership_cost(membership_plan)
    feature_cost = add_features(selected_features)

    total_cost = base_cost + feature_cost
    total_cost = apply_group_discount(total_cost, group_size)
    total_cost = apply_special_offers(total_cost)
    total_cost = apply_premium_surcharge(membership_plan, total_cost)

    return total_cost
