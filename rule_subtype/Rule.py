from nameko.standalone.rpc import ClusterRpcProxy
import yaml
import pickle
import base64


class Rule(object):

    def validate(self, fact_message):
        with open("config.yml", 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
        CONFIG = {'AMQP_URI': str(cfg['rule_engine']['AMQP_URI'])}
        with ClusterRpcProxy(CONFIG) as rpc:
            # asynchronously spawning and email notification
            dumped = pickle.dumps(fact_message)

            b64 = base64.b64encode(dumped).decode()

            return rpc.ruleengine.validate_rule(b64)
