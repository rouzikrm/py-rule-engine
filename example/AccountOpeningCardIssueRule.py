from decorators.RuleDecorator import rule
from decorators.ActionDecorator import action
from decorators.ConditionDecorator import condition
from rule_subtype.Rule import Rule


@rule
class AccountOpeningCardIssueRule(Rule):
    @condition
    def has_sufficient_remaining_balance_after_card_issue(self, facts):
        if (facts.get("account_balance") - 2.29) > 4.00:
            return True
        return False

    @action
    def issue_card(self,fact):
        print("calling issue card service")
        return "Your Account Number is "+ fact.get("account_number") +", Card Number TTTT-XXXX-YYYY-NNNN"
