"""Utility module for calculating gym membership cost."""

from membership import Membership

def calculate_cost(plan, features, group_size=1):
    """Calculate total cost based on plan, features, and group size.

    Returns -1 if the input is invalid.
    """
    if not Membership.is_valid_plan(plan):
        return -1

    base_cost = Membership.plans[plan]
    features_cost = 0
    has_premium = False

    for feature in features:
        if Membership.is_valid_feature(feature):
            features_cost += Membership.additional_features[feature]
        elif Membership.is_premium_feature(feature):
            has_premium = True
            features_cost += 50
        else:
            return -1

    total = base_cost + features_cost

    if total > 400:
        total -= 50
    elif total > 200:
        total -= 20

    if has_premium:
        total += total * 0.15

    total *= group_size
    if group_size >= 2:
        total *= 0.9

    return int(total)
