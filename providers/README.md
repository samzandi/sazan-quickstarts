# Provider Layer

Quickstarts should depend on a small provider interface rather than directly coupling application logic to one model vendor.

## Initial targets

- OpenAI
- Anthropic
- Local models through Ollama or compatible gateways

## Design principle

Application code should ask for capabilities such as chat, tool use, structured output, embeddings, or multimodal input. Provider adapters translate those capabilities into vendor-specific API calls.

This keeps examples portable and makes model comparison easier.
