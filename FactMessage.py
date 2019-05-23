#!/usr/bin/env python3
from abc import ABC, abstractmethod
class FactMessage(ABC):
    def __init__(self,facts):
        self.facts=facts