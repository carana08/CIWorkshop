import pytest
from gym_membership.system import MembershipSystem
from gym_membership.models import MEMBERSHIP_PLANS, ADDITIONAL_FEATURES

@pytest.fixture
def system():
    return MembershipSystem()

def test_add_valid_member(system):
    system.add_member("Basic", ["Personal Training"])
    assert len(system.members) == 1

def test_add_invalid_plan(system):
    with pytest.raises(ValueError):
        system.add_member("Invalid", ["Personal Training"])

def test_add_invalid_feature(system):
    with pytest.raises(ValueError):
        system.add_member("Basic", ["Invalid Feature"])

def test_single_member_cost(system):
    system.add_member("Basic", [])
    base, features, surcharge, discount, total = system.calculate_costs()
    assert base == 100
    assert total == 100

def test_group_discount(system):
    system.add_member("Basic", [])
    system.add_member("Basic", [])
    _, _, _, discount, total = system.calculate_costs()
    assert discount == 20  # 10% of 200
    assert total == 180

def test_premium_surcharge(system):
    system.add_member("Basic", ["Exclusive Facility Access"])
    _, _, surcharge, _, total = system.calculate_costs()
    assert surcharge == round(70 * 0.15)  # 10.5 -> 11
    assert total == 100 + 70 + 11

def test_special_discount(system):
    # Total = 300 (Premium) + 90 = 390
    system.add_member("Premium", ["Specialized Training"])
    _, _, _, _, total = system.calculate_costs()
    assert total == 390 - 20  # Special discount $20

    system.add_member("Premium", [])
    _, _, _, _, total = system.calculate_costs()
    assert total == (390 + 200) - 50  # Special discount $50

def test_confirmation(system):
    system.add_member("Basic", [])
    total = system.confirm_membership()
    assert total == 100
    assert system.confirmed

def test_cancellation(system):
    system.add_member("Basic", [])
    result = system.cancel_membership()
    assert result == -1
    assert not system.members