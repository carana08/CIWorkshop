import pytest
from unittest.mock import patch
from io import StringIO
from gym_membership.cli import GymMembershipCLI


def run_cli_with_inputs(inputs):
    """Helper function to simulate user inputs"""
    with patch('sys.stdin', StringIO('\n'.join(inputs))), \
            patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        cli = GymMembershipCLI()
        cli.run()
        return mock_stdout.getvalue()


def test_single_member_no_extras(capsys):
    inputs = [
        '1',  # Number of members
        'Basic',  # Membership plan
        '',  # No features
        'yes'  # Confirm
    ]
    output = run_cli_with_inputs(inputs)

    assert "Base Cost: $100" in output
    assert "Additional Features: $0" in output
    assert "Total Cost: $100" in output
    assert "Membership confirmed!" in output


def test_group_discount(capsys):
    inputs = [
        '2',  # Number of members
        'Premium',  # Member 1 plan
        '',  # Member 1 features
        'Premium',  # Member 2 plan
        '',  # Member 2 features
        'yes'  # Confirm
    ]
    output = run_cli_with_inputs(inputs)

    assert "Base Cost: $400" in output  # 200 * 2
    assert "Group Discount: -$40" in output  # 10% of 400
    assert "Total Cost: $360" in output


def test_premium_surcharge(capsys):
    inputs = [
        '1',
        'Basic',
        'Exclusive Facility Access',  # Premium feature
        'yes'
    ]
    output = run_cli_with_inputs(inputs)

    assert "Premium Surcharge: $11" in output  # 15% of 70
    assert "Total Cost: $181" in output  # 100 + 70 + 11


def test_special_discounts(capsys):
    # Should trigger $20 discount (total $390)
    inputs = [
        '1',
        'Premium',
        'Specialized Training',  # $200 + $90 = $290
        'yes'
    ]
    output = run_cli_with_inputs(inputs)
    assert "Special Discount: -$20" in output
    assert "Total Cost: $290" not in output

    # Should trigger $50 discount (total $510)
    inputs = [
        '2',
        'Family',
        'Exclusive Facility Access,Specialized Training',  # $300 + $70 + $90 = $460
        'Family',
        'Exclusive Facility Access,Specialized Training',  # Another $460
        'yes'
    ]
    output = run_cli_with_inputs(inputs)
    assert "Special Discount: -$50" in output
    assert "Total Cost: $870" in output  # (460*2) - 50


def test_invalid_inputs(capsys):
    # Test invalid member count
    inputs = [
        '0',  # Invalid
        'two',  # Invalid
        '3',  # Valid
        'Basic', '', 'Basic', '', 'Basic', '', 'yes'
    ]
    output = run_cli_with_inputs(inputs)
    assert "Error: Must have at least 1 member" in output
    assert "Error: Please enter a valid number" in output

    # Test invalid membership
    inputs = [
        '1',
        'Invalid Plan',  # Invalid
        'Basic',  # Then valid
        '', 'yes'
    ]
    output = run_cli_with_inputs(inputs)
    assert "Error: Invalid plan selection" in output

    # Test invalid feature
    inputs = [
        '1',
        'Basic',
        'Invalid Feature, Personal Training',  # One invalid
        'Personal Training',  # Then valid
        'yes'
    ]
    output = run_cli_with_inputs(inputs)
    assert "Error: Invalid features" in output


def test_cancellation(capsys):
    inputs = [
        '1',
        'Basic',
        '',
        'no'  # Cancel
    ]
    output = run_cli_with_inputs(inputs)
    assert "Membership canceled" in output
    assert "Total Cost: $" not in output


def test_error_handling(capsys):
    # Test invalid input in feature selection
    inputs = [
        '1',
        'Basic',
        'Invalid Feature',  # Will cause ValueError
    ]
    output = run_cli_with_inputs(inputs)
    assert "Error: Invalid feature" in output
    assert "Membership canceled" not in output