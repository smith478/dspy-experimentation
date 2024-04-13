import dspy
from dspy.evaluate import Evaluate
from dspy.teleprompt import BootstrapFewShot, BootstrapFewShotWithRandomSearch, BootstrapFinetune

llama = dspy.HFClientTGI(model="meta-llama/Llama-2-13b-chat-hf", port=[7140, 7141, 7142, 7143], max_tokens=150)
colbertv2 = dspy.ColBERTv2(url='http://20.102.90.50:2017/wiki17_abstracts')

dspy.settings.configure(rm=colbertv2, lm=llama)