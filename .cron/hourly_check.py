#!/usr/bin/env python3
"""
Hourly Status Check
Generates status update for Akshay every hour.
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path

# Paths
LOOP_STATE = Path('/home/akshay/.openclaw/workspace/LOOP_STATE.json')
PROGRESS = Path('/home/akshay/.openclaw/workspace/PROGRESS.md')
WORKSPACE = Path('/home/akshay/.openclaw/workspace')

def get_loop_state():
    """Read LOOP_STATE.json"""
    if LOOP_STATE.exists():
        with open(LOOP_STATE) as f:
            return json.load(f)
    return {'mode': 'normal', 'last_nudge': None}

def get_last_active():
    """Calculate how long since last activity"""
    state = get_loop_state()
    if state.get('last_nudge'):
        last = datetime.fromisoformat(state['last_nudge'])
        now = datetime.now()
        diff = now - last
        hours = diff.total_seconds() / 3600
        if hours < 1:
            return f"{int(diff.total_seconds() / 60)}m ago"
        return f"{int(hours)}h ago"
    return "Unknown"

def check_pending_tasks():
    """Check PROGRESS.md for pending tasks"""
    if PROGRESS.exists():
        with open(PROGRESS) as f:
            content = f.read()
            if 'pending' in content.lower() or 'todo' in content.lower():
                return "Check PROGRESS.md"
    return "None"

def format_status_update():
    """Format the hourly status update"""
    state = get_loop_state()
    last_active = get_last_active()
    next_action = check_pending_tasks()
    
    mode = state.get('mode', 'normal')
    
    # Auto-update last_nudge
    state['last_nudge'] = datetime.now().isoformat()
    with open(LOOP_STATE, 'w') as f:
        json.dump(state, f, indent=2)
    
    return f"Mode: {mode} | Last Active: {last_active} | Next Action: {next_action}"

if __name__ == '__main__':
    status = format_status_update()
    print(status)
