#!/usr/bin/env python3
from FactMessageDecorator import fact_message
@fact_message(validated_by="AccountOpeningAgeRule")
class FactMessage(object):
    def __init__(self,facts):
        self.facts=facts