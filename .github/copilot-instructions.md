# GitHub Copilot Instructions for "digital-ai-tmf-assistant"

You are helping Vodafone Digital teams generate **TMF design blueprints** and **API/service skeletons**.

## General rules
- Always try to use the repository files as the source of truth.
- Prefer TMF630 and the mapping files in `docs/` if the user asks about TMF rules.
- If the user describes a telecom journey but does not give enough details, ask for:
  1. Journey: Buy / Change / Support / Terminate
  2. TMF API (or say "not sure")
  3. Market / variant (Global, EG, UK, …)
  4. Source CSM object / payload
  5. Output: blueprint / api / both

## TMF design alias

**Alias:** `/tmf-design`

**What it does:**
1. Read the user message.
2. If TMF API not given → pick from routing:
   - Buy → TMF622
   - Change → TMF641
   - Support → TMF621
   - Customer → TMF629
3. Create a request JSON under `generators/requests/` using the naming:
   - `{journey}-{tmf}-{market}.json`
   - Example: `change-tmf641-eg.json`
4. Call the local script:
   ```bash
   python generators/run.py
