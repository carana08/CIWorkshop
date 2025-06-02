"""Membership module defining plans and features for the gym system."""

class Membership:
    """Handles available membership plans and their features."""

    plans = {
        "Basic": 50,
        "Premium": 100,
        "Family": 120
    }

    premium_features = ["Exclusive Access", "Special Training"]

    additional_features = {
        "Personal Training": 30,
        "Group Classes": 20,
        "Nutrition Plan": 25
    }

    @staticmethod
    def is_valid_plan(plan):
        """Check if the membership plan is valid."""
        return plan in Membership.plans

    @staticmethod
    def is_valid_feature(feature):
        """Check if the additional feature is valid."""
        return feature in Membership.additional_features

    @staticmethod
    def is_premium_feature(feature):
        """Check if the feature is a premium feature."""
        return feature in Membership.premium_features
