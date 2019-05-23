#!/usr/bin/env python3
from FactMessage import FactMessage
from FactMessageDecorator import fact_message
@fact_message(validated_by="AccountOpeningFamilyRule")
class  AccountOpeningFamilyFactMessage(FactMessage):
    def __init__(self,facts):
        self.facts=facts