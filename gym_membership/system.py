from .models import MEMBERSHIP_PLANS, ADDITIONAL_FEATURES


class MembershipSystem:
    def __init__(self):
        self.members = []
        self.confirmed = False

    def add_member(self, plan, features):
        if plan not in MEMBERSHIP_PLANS:
            raise ValueError(f"Invalid membership plan: {plan}")

        for feature in features:
            if feature not in ADDITIONAL_FEATURES:
                raise ValueError(f"Invalid feature: {feature}")

        self.members.append({"plan": plan, "features": features})

    def calculate_costs(self):
        if not self.members:
            return 0, 0, 0, 0, 0

        base_cost = 0
        features_cost = 0
        premium_surcharge = 0

        for member in self.members:
            # Base membership cost
            base_cost += MEMBERSHIP_PLANS[member["plan"]]["cost"]

            # Additional features cost
            for feature in member["features"]:
                feature_data = ADDITIONAL_FEATURES[feature]
                features_cost += feature_data["cost"]

                # Premium feature surcharge
                if feature_data["premium"]:
                    premium_surcharge += feature_data["cost"] * 0.15

        # Calculate raw total before discounts
        raw_total = base_cost + features_cost + premium_surcharge

        # Apply group discount (10% if ≥2 same plan members)
        group_discount = 0
        plan_counts = {}
        for member in self.members:
            plan_counts[member["plan"]] = plan_counts.get(member["plan"], 0) + 1

        if any(count >= 2 for count in plan_counts.values()):
            group_discount = raw_total * 0.10

        # Apply special offer discounts
        special_discount = 0
        if raw_total > 400:
            special_discount = 50
        elif raw_total > 200:
            special_discount = 20

        # Calculate final total
        final_total = raw_total - group_discount - special_discount

        return (
            round(base_cost),
            round(features_cost),
            round(premium_surcharge),
            round(group_discount),
            round(max(final_total, 0))
        )

    def confirm_membership(self):
        self.confirmed = True
        return self.calculate_costs()[-1]  # Return final total

    def cancel_membership(self):
        self.members = []
        self.confirmed = False
        return -1