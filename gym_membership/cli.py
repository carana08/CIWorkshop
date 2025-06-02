import sys
from .system import MembershipSystem
from .models import MEMBERSHIP_PLANS, ADDITIONAL_FEATURES


class GymMembershipCLI:
    def __init__(self):
        self.system = MembershipSystem()

    def display_plans(self):
        print("\nAvailable Membership Plans:")
        for plan, details in MEMBERSHIP_PLANS.items():
            print(f"- {plan}: ${details['cost']} ({details['description']})")

    def display_features(self):
        print("\nAdditional Features:")
        for feature, details in ADDITIONAL_FEATURES.items():
            premium_tag = " [Premium]" if details["premium"] else ""
            print(f"- {feature}: ${details['cost']}{premium_tag}")

    def get_member_count(self):
        while True:
            try:
                count = int(input("\nNumber of members: "))
                if count < 1:
                    print("Error: Must have at least 1 member")
                else:
                    return count
            except ValueError:
                print("Error: Please enter a valid number")

    def get_membership_choice(self):
        while True:
            choice = input("Select membership plan: ").strip().title()
            if choice in MEMBERSHIP_PLANS:
                return choice
            print("Error: Invalid plan selection. Please choose from available options.")

    def get_feature_choices(self):
        while True:
            choices = input("Select features (comma-separated): ").split(',')
            choices = [c.strip().title() for c in choices if c.strip()]

            invalid = [c for c in choices if c not in ADDITIONAL_FEATURES]
            if invalid:
                print(f"Error: Invalid features - {', '.join(invalid)}")
            else:
                return choices

    def get_confirmation(self, summary):
        print("\n" + "=" * 50)
        print("Membership Summary:")
        print(summary)
        print("=" * 50)

        while True:
            choice = input("\nConfirm membership? (yes/no): ").lower()
            if choice in ['y', 'yes']:
                return True
            elif choice in ['n', 'no']:
                return False
            print("Error: Please enter 'yes' or 'no'")

    def run(self):
        try:
            print("==== Gym Membership Management System ====")
            self.display_plans()
            self.display_features()

            member_count = self.get_member_count()

            for i in range(member_count):
                print(f"\nMember #{i + 1}:")
                plan = self.get_membership_choice()
                features = self.get_feature_choices()
                self.system.add_member(plan, features)

            # Calculate costs
            base, features, surcharge, group_disc, total = self.system.calculate_costs()

            # Build summary
            summary = f"Base Cost: ${base}\n"
            summary += f"Additional Features: ${features}\n"
            summary += f"Premium Surcharge: ${surcharge}\n"

            if group_disc:
                summary += f"Group Discount: -${group_disc}\n"

            if total > 400:
                summary += "Special Discount: -$50\n"
            elif total > 200:
                summary += "Special Discount: -$20\n"

            summary += f"Total Cost: ${total}"

            # Confirmation
            if self.get_confirmation(summary):
                final_cost = self.system.confirm_membership()
                print(f"\nMembership confirmed! Total cost: ${final_cost}")
                sys.exit(0)
            else:
                result = self.system.cancel_membership()
                print("\nMembership canceled")
                sys.exit(result)

        except Exception as e:
            print(f"\nError: {str(e)}", file=sys.stderr)
            sys.exit(-1)


if __name__ == "__main__":
    cli = GymMembershipCLI()
    cli.run()