# DSPy Experimentation

This repo contains experimentations done with the DSPy framework. The [repo]((https://github.com/stanfordnlp/dspy)) contains great documentation on getting started and helpful examples.

By default DSPy will use the OpenAI api for model calls, however this can be changed to a different api service or locally hosted model. For this to work for OpenAI you will need to set your API key. This can be done by adding the following to your bash profile.

```
export OPENAI_API_KEY='your-api-key'
```

## Examples
- `minimal_example.py` this example uses the openai API and has a minimal example.
- `local_inference.py` this example shows how you would use a locally hosted model.