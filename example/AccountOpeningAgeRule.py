from RuleDecorator import rule
from ActionDecorator import action
from ConditionDecorator import condition
from NextDecorator import next
from example.AccountOpeningFamilyFactMessage \
    import AccountOpeningFamilyFactMessage
from Rule import Rule


@rule
class AccountOpeningAgeRule(Rule):
    @condition
    def isHappy(self, facts):
        if facts.get("age") > 18:
            return True
        return False

    @next
    def throwParty(self, facts):
        print("let's throw party")
        return AccountOpeningFamilyFactMessage({"happy": "False"})
