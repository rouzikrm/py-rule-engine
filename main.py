import RuleReference
import pickle
import base64
# pickle.dumps
#
from nameko.rpc import rpc


class Main(object):
        name = 'ruleengine'
        @rpc
        def validateRule(self, fact):

            desfact = pickle.loads(base64.b64decode(fact.encode('utf8'))) # FactMessage({"age":19})
            a = getattr(RuleReference,desfact._validated_by)
            if(a()._condition(None,desfact.facts)):
                return a()._action(None,desfact.facts)
            else : raise Exception('the condition returned false')
