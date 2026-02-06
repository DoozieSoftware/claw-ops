# 🦞 ClawOps - AI Agent Operations

> **Your AI workforce, managed.**

This workspace contains ClawOps — the brain and operations for your AI agent business.

## Two Repositories

| Repository | Purpose | Access |
|------------|---------|--------|
| `claw-ops` (public) | Landing page, docs | Public |
| `claw-ops-internal` (private) | **Your brain!** | Private |

---

## 👉 Go Here for Everything

```
claw-ops-internal/
├── 📁 memory/              ← Your long-term memory
├── 📁 scripts/             ← Your tools
├── 📁 skills/             ← Your capabilities
├── 📁 vault/              ← Client data
├── 📄 SOUL.md              ← Your identity
├── 📄 PROGRESS.md          ← Current status
├── 📄 ENGINEER_GUIDE.md    ← How to work
└── 📄 README.md            ← Start here!
```

---

## Quick Start

```bash
# Go to internal repo
cd claw-ops-internal

# Read the README
cat README.md

# Check memory
cat MEMORY.md

# Check today's todos
cat PROGRESS.md

# Run daily backup
python3 scripts/backup_manager.py --daily
```

---

## Public Repository (claw-ops)

Public-facing landing page and documentation:

```
claw-ops/
├── 📄 index.html          ← Main landing page
├── 📄 README.md           ← Public overview
└── 📁 ...                 ← Marketing materials
```

---

## Commands

```bash
# Daily workflow
cd claw-ops-internal
cat memory/$(date +%Y-%m-%d).md  # Today's notes
cat PROGRESS.md                  # What's in flight

# Backup
python3 scripts/backup_manager.py --daily

# Client management
python3 scripts/client_vault.py --list-clients
```

---

*ClawOps — Your AI workforce, managed.*

