# py-rule-engine
### There are many cases when you want to implement a complex rule set or action flow based on some conditions and you want to keep your code readable and clean from hassle of too many (if/else)
### py-rule-engine is a scalable rule-engine which support implementing complicated rule flows in a fast manner. it utilize nameko framework to pass data in format of FactMessage Class objects.
### Each FactMessage use a @fact_message decorator to map these inputs to its rule class. the code in main.py then reads the decorator in FactMessage and loads Rule class.
### To increase code readability we used @condition , @action and @next_rule decorator to mark those methods so you can assign clean names to your methods and mark their roles using decorators.

## How To Run

```
docker-compose up -d  --build
docker-compose exec nameko-client nameko shell --config config.yml
```
`in nameko shell:`
```
import sys
sys.path.append(".")
from example.AccountOpeningAgeFactMessage import AccountOpeningAgeFactMessage
a = AccountOpeningAgeFactMessage({"age":19})
import pickle
import base64
dumped = pickle.dumps(a)
b64  = base64.b64encode(dumped).decode()
n.rpc.ruleengine.validate_rule(b64)
```

## Steps To Add a new Rule

```
1. Create your Fact Class extending FactMessage.py
add fact_message decorator on top of class as below:
@fact_message(validated_by="<Your Rule Class Name>")

2. define a Rule Class as follows:
create a .py file with the same name as your desired class

define your desired class in that file

add @rule decorator on top of  your class

add your condition method which returns Boolean
decorate it using @condition

add your action method and decorate it with @action
 
if you want to go to another rule from this action method just use @next_rule decorator instead of @action.

be aware when using @next_rule you should return an object of FactMessage type so that the framework recognize next Rule Class


3. follow steps in <## How To Run:> section to test your rule!

Happy Rulling!
```
