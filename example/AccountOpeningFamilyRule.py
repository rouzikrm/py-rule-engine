from RuleDecorator import rule
from ActionDecorator import action
from ConditionDecorator import condition
from Rule import Rule
@rule
class AccountOpeningFamilyRule(Rule):
    @condition
    def isHappy(self,facts):
        if facts.get("happy")=="True":
            return True
        return False

    @action
    def throwParty(self, facts):
        print("let's throw party")
        return "Happy Hoe!!"