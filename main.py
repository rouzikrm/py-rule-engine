import pickle
import base64
import re
import os
import sys
import importlib
import inspect
import yaml

# pickle.dumps
#
from nameko.rpc import rpc


class Main(object):
        name = 'ruleengine'
        @rpc
        def validateRule(self, fact):
            desfact = pickle.loads(base64.b64decode(fact.encode('utf8')))  # FactMessage({"age":19})
            rule_reference = self.load_plugins(desfact._validated_by)
            a = getattr(rule_reference,   desfact._validated_by)
            print(rule_reference)
            if(a()._condition(None,desfact.facts)):
                try:
                    return a()._action(None,desfact.facts)
                except AttributeError:
                    return a()._next(None, desfact.facts)
            else : raise Exception(a + ' condition method returned false')


        @rpc
        def sayhello(self,name):
            return "hello "+name

        def load_plugins(self,name):
            with open("config.yml", 'r') as ymlfile:
                cfg = yaml.load(ymlfile)
            pysearchre = re.compile(name+'.py$', re.IGNORECASE)
            print(pysearchre)
            pluginfiles = filter(pysearchre.search,
                                 os.listdir(os.path.join(os.path.dirname(__file__),
                                                         cfg['rule_engine']['rule_mod_base_dir'])))
            form_module = lambda fp: '.' + os.path.splitext(fp)[0]
            plugins = map(form_module, pluginfiles)
            print(plugins)
            # import parent module / namespace
            importlib.import_module( cfg['rule_engine']['rule_mod_base_dir'].split('/')[-1])
            modules = []
            for plugin in plugins:
                print(plugin)
                modules.append(importlib.import_module(plugin, package= cfg['rule_engine']['rule_mod_base_dir'].split('/')[-1]))
            for module in modules:
                for name, obj in inspect.getmembers(module,inspect.isclass):
                        print('name:',name,'obj:',obj)
            return modules[0]