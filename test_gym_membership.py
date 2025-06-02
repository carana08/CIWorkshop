# test_gym_membership.py

import pytest
from gym_membership_system import calculate_total_cost, apply_group_discount, add_features

def test_calculate_total_cost_basic():
    """Test for basic membership with no additional features."""
    total_cost = calculate_total_cost("Basic", [], group_size=1)
    assert total_cost == 50, f"Expected 50 but got {total_cost}"

def test_calculate_total_cost_with_features():
    """Test for membership with additional features."""
    total_cost = calculate_total_cost("Basic", ["Personal Training"], group_size=1)
    assert total_cost == 80, f"Expected 80 but got {total_cost}"

def test_apply_group_discount():
    """Test for applying group discount."""
    total_cost = apply_group_discount(100, 2)
    assert total_cost == 90, f"Expected 90 but got {total_cost}"

def test_add_features():
    """Test for adding multiple features."""
    feature_cost = add_features(["Personal Training", "Group Classes"])
    assert feature_cost == 50, f"Expected 50 but got {feature_cost}"
