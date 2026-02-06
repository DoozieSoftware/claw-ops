# SOP-001: Production Hardening Checklist
**Status:** LOCKED for v1.0.0
**Applies to:** Hardened Deployment Package ($399–$699)

## 1. Security Baseline
- [ ] **Secrets Isolation:** Ensure `.env.claw` exists, is populated, and is NOT in gitignore.
- [ ] **Network Binding:** Gateway bound to `127.0.0.1:3000` by default (or behind reverse proxy).
- [ ] **External Ports:** Verify no ports are exposed to `0.0.0.0` unless intentional (e.g., Nginx proxy).
- [ ] **Secret Key:** `GATEWAY_SECRET_KEY` is cryptographically strong (not "secret" or "key").
- [ ] **SSL/TLS:** If exposed to internet, Nginx proxy with valid SSL is active.
- [ ] **Firewall:** UFW/Firewalld rules block all non-essential ports.

## 2. Operational Stability
- [ ] **Restart Policy:** `unless-stopped` is set on all containers.
- [ ] **Resource Limits:** CPU/Memory limits configured in `docker-compose` to prevent runaway processes.
- [ ] **Volume Persistence:** OpenClaw data volume is correctly mounted and persistent.
- [ ] **Backup Strategy:** Backups scheduled (cron) and functional. Test restore performed once.

## 3. Upgrade Safety
- [ ] **Version Pinning:** Docker image tags are specific (e.g., `v1.2.0`, not `latest`).
- [ ] **Rollback Plan:** Documented steps to revert to previous Docker image tag.
- [ ] **Breaking Change Monitor:** User has been instructed to check release notes before running `git pull`.

## 4. Observability
- [ ] **Logs:** `LOG_LEVEL` set to `info` or `warn`.
- [ ] **Log Rotation:** `journald` or container log rotation configured.
- [ ] **Health Check:** Gateway `/status` endpoint is responding.
- [ ] **Alerting:** User has a mechanism (UptimeRobot, Cron job) to check `/status`.

## 5. Documentation Handover
- [ ] **Runbook:** Environment-specific start/stop/restart commands provided.
- [ ] **File Locations:** User knows where `docker-compose.yml`, `.env`, and data volumes live.
- [ ] **Emergency Contacts:** Clear instructions on what to do if the container won't start.

---

**Delivery is NOT "Done" until all items in this checklist are checked.**
