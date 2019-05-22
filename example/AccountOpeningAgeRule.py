from RuleDecorator import rule
from ActionDecorator import action
from ConditionDecorator import condition
@rule
class AccountOpeningAgeRule(object):
    @condition
    def isHappy(self,facts):
        if facts.get("age") > 18:
            return True
        return False

    @action
    def throwParty(self, facts):
        print("let's throw party")
        return "Happy Now!"