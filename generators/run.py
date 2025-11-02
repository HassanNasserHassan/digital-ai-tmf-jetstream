import json
from pathlib import Path

def load_text(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")

def call_llm(prompt: str, context: str) -> str:
    # -------- POC MODE ----------
    # For now we just return the prompt+context so we see it works.
    # TO DO we'll replace this with a real LLM call.
    return f"PROMPT:\n{prompt}\n\nCONTEXT:\n{context}\n"

def main():
    # 1) load request
    request_path = Path("generators/requests/change-tmf641-eg.json")
    req = json.loads(request_path.read_text(encoding="utf-8"))

    # 2) load prompts
    blueprint_prompt = load_text("generators/prompts/blueprint.txt")
    openapi_prompt = load_text("generators/prompts/openapi.txt")

    # 3) build context for blueprint (for POC: just request JSON)
    context_for_blueprint = json.dumps(req, indent=2)

    # 4) LLM #1 → blueprint
    blueprint_md = call_llm(blueprint_prompt, context_for_blueprint)

    # 5) save blueprint
    Path("blueprints").mkdir(exist_ok=True)
    blueprint_file = Path("blueprints") / f"{req['journey'].lower()}-{req['tmf'].lower()}-{req['market'].lower()}.md"
    blueprint_file.write_text(blueprint_md, encoding="utf-8")

    # 6) LLM #2 → OpenAPI (use blueprint as context)
    openapi_yaml = call_llm(openapi_prompt, blueprint_md)

    Path("generators/output").mkdir(parents=True, exist_ok=True)
    openapi_file = Path("generators/output") / f"{req['tmf'].lower()}-{req['journey'].lower()}-{req['market'].lower()}.yaml"
    openapi_file.write_text(openapi_yaml, encoding="utf-8")

    print("Created:")
    print(" -", blueprint_file)
    print(" -", openapi_file)

if __name__ == "__main__":
    main()
