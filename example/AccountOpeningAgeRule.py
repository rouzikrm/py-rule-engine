from RuleDecorator import rule


from ConditionDecorator import condition
from NextDecorator import next_rule
from example.AccountOpeningCardIssueFactMessage \
    import AccountOpeningCardIssueFactMessage
from Rule import Rule


@rule
class AccountOpeningAgeRule(Rule):
    @condition
    def is_authorized_to_own_a_bank_account(self, facts):
        if facts.get("age") > 17:
            return True
        return False

    @next_rule
    def issue_account(self,fact):
        print("Account Number XXXXYYYYZZZZ is yours!")
        return AccountOpeningCardIssueFactMessage({"account_number":"XXXXYYYYZZZZ","account_balance": 12.00})
