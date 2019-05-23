from RuleDecorator import rule
from ActionDecorator import action
from ConditionDecorator import condition
import pickle
import base64
import re
import os
import sys
import importlib
import inspect
import yaml


class Rule(object):

    def validate_rule(self, fact_message):
        rule_reference = self.load_plugins(fact_message._validated_by)
        a = getattr(rule_reference, fact_message._validated_by)
        print(rule_reference)
        if (a()._condition(None, fact_message.facts)):
            try:
                return a()._action(None, fact_message.facts)
            except AttributeError:
                return a()._next(None, fact_message.facts)
        else:
            raise Exception(
                fact_message._validated_by + ' condition returned false'
            )

    def load_plugins(self, name):
        with open("config.yml", 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
        pysearchre = re.compile(name + '.py$', re.IGNORECASE)
        pluginfiles = filter(pysearchre.search,
                             os.listdir(
                                 os.path.join(os.path.dirname(__file__),
                                              cfg['rule_engine']['rule_mod_base_dir']
                                              )
                             )
                             )
        form_module = lambda fp: '.' + os.path.splitext(fp)[0]
        plugins = map(form_module, pluginfiles)
        # import parent module / namespace
        importlib.import_module(
            cfg['rule_engine']['rule_mod_base_dir'].split('/')[-1]
        )
        modules = []
        for plugin in plugins:
            print(plugin)
            modules.append(
                self.get_module_base_dir(cfg, plugin))
        for module in modules:
            for name, obj in inspect.getmembers(module, inspect.isclass):
                print('name:', name, 'obj:', obj)
        return modules[0]

    def get_module_base_dir(self, cfg, plugin):
        return importlib.import_module(
            plugin,
            package=cfg['rule_engine']['rule_mod_base_dir']
                .split('/')[-1])

    def prepend_dot(self, fp):
        return '.' + os.path.splitext(fp)[0]
