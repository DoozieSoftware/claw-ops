# MEMORY.md - ClawOps Business

## Business Identity
- **Name**: ClawOps
- **Mission**: Production-ready OpenClaw operations for enterprises
- **Tagline**: "Without the infrastructure babysitting"

## Strategy (No Fork)
Use upstream OpenClaw core. Add enterprise value via skills/plugins, not core changes. This ensures automatic updates and no merge hell.

## Pricing
- QuickStart: $99 (1 channel, 1 use case)
- Starter: $199 (1 channel, 3 use cases)
- Business: $499 (all defaults, all channels)
- ClawCare: $99/mo (support and maintenance)
- Indian Clients: 30% off, GST extra

## Channels (Focus)
1. WhatsApp (Meta Business API)
2. Telegram (Bot API)
3. Slack (Bot Tokens)
4. Discord (Bot Intents)

## AI Providers
### Enterprise Tier (Complex Reasoning)
- Claude.ai (Anthropic)
- GPT-4o (OpenAI)
- Gemini (Google)

### Mid-Range Tier (Skills)
- GLM (智谱AI)
- Kimi k2.5 (Moonshot)
- Minimax (Recommended for diverse needs)

**Note**: AI API subscription costs are billed by the provider, NOT included in our fees.

## Pipeline Use Cases (Coming Soon)
- **Account Operator** - Real-time account access, Indian market (no middleman)
- **Safety Officer** - Offline camera feed & document audit
- **Purchase Officer** - Negotiation research assistant
- **Project Manager** - PM Bot for developer management

## SOUL.md Framework (Key Innovation)

Each client gets a **custom SOUL.md** that defines:

1. **Bot Identity** — Name, channels, purpose
2. **Boundaries (DENY ALL)** — Explicit allowlist only
3. **Validation Engine** — Automated checks before every action
4. **Safety Guards** — Alerts on violations, block threats
5. **Audit Trail** — Every action logged

### SOUL Components

| Component | Purpose |
|-----------|---------|
| Identity | Bot name, channels, purpose |
| Boundaries | Allowed/blocked actions |
| Time Limits | Active hours, read-only hours |
| Geo Limits | Allowed countries |
| User Allowlist | Who can use the bot |
| Validation Rules | Pre-action checks (5 things) |
| Safety Guards | Alert triggers |
| Audit Format | Log structure |

## Key Files
- Public: `DoozieSoftware/claw-ops` - Landing page, channels, AI recommendations, case studies
- Private: `DoozieSoftware/claw-ops-internal` - Engineer guide, configs, use-case-engine skill

## Documentation (Internal)
| Document | Description |
|----------|-------------|
| CLAWOPS_OVERVIEW.md | Business overview and positioning |
| MARKETING_PLAN.md | Detailed marketing strategy |
| ROADMAP.md | Feature and timeline roadmap |
| ENGINEER_GUIDE.md | **Client setup with SOUL.md + security hardening** |
| templates/SOUL_TEMPLATE.md | **Bot identity & safety template** |
| PROGRESS.md | Current status and milestones |

## User Context
- **Akshay** (dooziesoft.com)
- Timezone: Asia/Calcutta
- Browser relay not available - use Git commands

## Last Session (Feb 6, 2026)
- Reorganized landing page flow (Problem → Solution → Use Cases → Pricing)
- Added Case Studies page (Redmine, Telegram bots, Camera automation, Boss Tasks)
- Added Custom Use Cases section (API integrations)
- Added Pipeline section (Account Operator, Safety Officer, etc.)
- Added ClawCare package ($99/mo)
- Added 30% Indian client discount
- Created comprehensive internal documentation (Overview, Marketing Plan, Roadmap)

## This Session (Feb 6, 2026 - Evening)
- Redesigned ENGINEER_GUIDE.md with client setup focus
- Added SOUL.md concept — Bot identity, boundaries, validation engine
- Added DENY ALL security hardening (firewall, fail2ban, rate limiting)
- Created SOUL_TEMPLATE.md for client-specific bots
- Added SOUL validator Python script for automated validation
- Added safety guards and audit logging requirements
