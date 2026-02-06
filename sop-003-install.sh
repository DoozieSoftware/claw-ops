#!/bin/bash
# ClawOps SOP-003: Automated Install & Harden
# Status: DRAFT v1.0.1

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

usage() {
    echo "Usage: $0 [COMMAND]"
    echo "Commands:"
    echo "  install     (default) Run full install & validation"
    echo "  restore     Restore from latest backup"
    echo "  validate    Run validation checks only"
    echo "  status      Check container health"
    exit 1
}

case "${1:-install}" in
    install)
        echo -e "${YELLOW}🚀 ClawOps: Starting Production Install...${NC}"
        
        # 1. Pre-Flight Checks
        echo -e "${YELLOW}📋 Step 1: Pre-Flight Checks${NC}"
        if ! command -v docker &> /dev/null; then
            echo -e "${RED}❌ Docker is not installed. Aborting.${NC}"
            exit 1
        fi
        if [ ! -f ".env.claw" ]; then
            echo -e "${RED}❌ .env.claw file not found. Please create it from the template.${NC}"
            exit 1
        fi
        echo -e "${GREEN}✅ Pre-flight checks passed.${NC}"

        # 2. Network & Security Audit
        echo -e "${YELLOW}🔒 Step 2: Network & Security Audit${NC}"
        EXPOSED_PORTS=$(netstat -tuln | grep -E ':(80|443|3000)' || true)
        if [ ! -z "$EXPOSED_PORTS" ]; then
            echo -e "${YELLOW}⚠️  Warning: Detected ports in use: ${EXPOSED_PORTS}${NC}"
        fi

        # 3. Backup Existing
        echo -e "${YELLOW}💾 Step 3: Backup Existing Config${NC}"
        if [ -f "docker-compose.yml" ]; then
            cp docker-compose.yml docker-compose.yml.bak.$(date +%s)
            echo -e "${GREEN}✅ Backed up existing docker-compose.yml${NC}"
        fi

        # 4. Deploy
        echo -e "${YELLOW}🚀 Step 4: Deploying Services${NC}"
        docker-compose -f docker-compose.prod.yml up -d

        # 5. Validation (SOP-001)
        echo -e "${YELLOW}✅ Step 5: Validating Deployment (SOP-001)${NC}"

        # Check 1: Running
        CONTAINER_STATUS=$(docker inspect -f '{{.State.Running}}' claw_gateway 2>/dev/null || echo "false")
        if [ "$CONTAINER_STATUS" != "true" ]; then
            echo -e "${RED}❌ Container failed to start.${NC}"
            exit 1
        fi
        echo -e "${GREEN}✅ Container is running${NC}"

        # Check 2: Health Endpoint
        HEALTH=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:3000/status || echo "000")
        if [ "$HEALTH" != "200" ]; then
            echo -e "${RED}❌ Health check failed (Status: $HEALTH)${NC}"
            exit 1
        fi
        echo -e "${GREEN}✅ Health check passed${NC}"

        # Check 3: Logs
        LOGS=$(docker logs --tail 20 claw_gateway 2>&1)
        if echo "$LOGS" | grep -q "Error: Uncaught"; then
            echo -e "${RED}❌ Critical error found in logs.${NC}"
            exit 1
        fi
        echo -e "${GREEN}✅ Logs look clean${NC}"

        # 6. Generate Runbook
        echo -e "${YELLOW}📝 Step 6: Generating Runbook${NC}"
        cat > RUNBOOK.md <<EOF
# ClawOps Runbook
Generated: $(date)

## Quick Commands
- Status: ./sop-003-install.sh status
- Logs: docker-compose -f docker-compose.prod.yml logs -f
- Restart: ./sop-003-install.sh install
EOF
        echo -e "${GREEN}✅ Installation Complete!${NC}"
        ;;
        
    restore)
        echo -e "${YELLOW}♻️  ClawOps: Attempting Restore...${NC}"
        LATEST_BACKUP=$(ls -t docker-compose.yml.bak.* 2>/dev/null | head -1)
        if [ -z "$LATEST_BACKUP" ]; then
            echo -e "${RED}❌ No backups found.${NC}"
            exit 1
        fi
        echo -e "${GREEN}✅ Found backup: $LATEST_BACKUP${NC}"
        mv "$LATEST_BACKUP" docker-compose.yml
        echo -e "${GREEN}✅ Restored docker-compose.yml${NC}"
        echo -e "${YELLOW}🚀 Run './sop-003-install.sh install' to apply restore.${NC}"
        ;;
        
    validate)
        echo -e "${YELLOW}✅ ClawOps: Validation Only${NC}"
        CONTAINER_STATUS=$(docker inspect -f '{{.State.Running}}' claw_gateway 2>/dev/null || echo "false")
        if [ "$CONTAINER_STATUS" != "true" ]; then
            echo -e "${RED}❌ Container is NOT running.${NC}"
            exit 1
        fi
        HEALTH=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:3000/status || echo "000")
        if [ "$HEALTH" != "200" ]; then
            echo -e "${RED}❌ Health check failed (Status: $HEALTH)${NC}"
            exit 1
        fi
        echo -e "${GREEN}✅ All checks passed.${NC}"
        ;;
        
    status)
        echo -e "${YELLOW}📊 ClawOps Status${NC}"
        docker-compose -f docker-compose.prod.yml ps
        ;;
        
    *)
        usage
        ;;
esac
