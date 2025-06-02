import pytest
from utils import calculate_cost

def test_basic_plan_no_features():
    assert calculate_cost("Basic", []) == 50

def test_premium_with_features():
    assert calculate_cost("Premium", ["Personal Training", "Exclusive Access"]) == 207

def test_group_discount():
    assert calculate_cost("Family", ["Group Classes"], 3) == 378

def test_invalid_plan():
    assert calculate_cost("InvalidPlan", []) == -1

def test_invalid_feature():
    assert calculate_cost("Basic", ["InvalidFeature"]) == -1

def test_large_discount():
    assert calculate_cost("Premium", ["Personal Training", "Nutrition Plan", "Exclusive Access"], 2) < 400
