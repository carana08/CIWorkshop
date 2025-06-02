"""Unit tests for the gym membership cost calculation function."""

from utils import calculate_cost

def test_basic_plan_no_features():
    """Test Basic plan with no additional features."""
    assert calculate_cost("Basic", []) == 50

def test_premium_with_features():
    """Test Premium plan with personal training and premium feature."""
    assert calculate_cost("Premium", ["Personal Training", "Exclusive Access"]) == 207

def test_group_discount():
    """Test Family plan with group classes for 3 members with group discount."""
    assert calculate_cost("Family", ["Group Classes"], 3) == 378

def test_invalid_plan():
    """Test invalid membership plan."""
    assert calculate_cost("InvalidPlan", []) == -1

def test_invalid_feature():
    """Test invalid additional feature."""
    assert calculate_cost("Basic", ["InvalidFeature"]) == -1

def test_large_discount():
    """Test discount when total cost is large with group and premium features."""
    result = calculate_cost(
        "Premium", ["Personal Training", "Nutrition Plan", "Exclusive Access"], 2
    )
    assert result < 400
