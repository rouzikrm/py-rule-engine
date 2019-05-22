# py-rule-engine

## How To Run:

```
docker-compose up -d  --build
docker-compose exec nameko-client nameko shell --config config.yml
```
`in nameko shell:`
```
from example.FactMessage  import FactMessage
a = FactMessage({"age":19})
import pickle
import base64
dumped = pickle.dumps(a)
b64  = base64.b64encode(dumped).decode()
n.rpc.ruleengine.validateRule(b64)
```

## Steps To Add a new Rule

```
1. define a Rule Classa as follows:
add @rule decorator on top of  your generic class
add your condition method with returns Boolean
decorate it using @condition

add your action method and decorate it with @action

2. import your Rule class in RuleReference.py

3. Create your Fact Class extending FactMessage.py
add fact_message decorator on top of class as below:
@fact_message(validated_by="<Your Rule Class Name>")

4. follow steps in <## How To Run:> section to test your rule!

Happy Rulling!
```
