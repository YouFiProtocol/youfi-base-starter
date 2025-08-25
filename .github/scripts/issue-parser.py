#!/usr/bin/env python3
import sys
import re
import json
from pathlib import Path

def main():
    if len(sys.argv) < 4:
        return
        
    body = sys.argv[1]
    title = sys.argv[2] 
    number = sys.argv[3]
    
    if '[MINI-APP]' in title:
        create_mini_app(title, number)
    elif '[CONTRACT]' in title:
        create_contract(title, number)
    else:
        create_task(title, body, number)

def create_mini_app(title, number):
    name = re.sub(r'.*\[MINI-APP\]\s*', '', title).strip()
    safe_name = re.sub(r'[^a-zA-Z0-9]', '-', name.lower())
    
    app_dir = Path(f'apps/{safe_name}')
    app_dir.mkdir(parents=True, exist_ok=True)
    
    package = {
        "name": safe_name,
        "version": "0.1.0",
        "scripts": {"dev": "next dev"},
        "dependencies": {"@coinbase/onchainkit": "^0.24.0", "next": "14.2.5", "react": "18.3.1"}
    }
    with open(app_dir / 'package.json', 'w') as f:
        json.dump(package, f, indent=2)
    
    with open(app_dir / 'README.md', 'w') as f:
        f.write(f"# {name}\n\nMini App gerado automaticamente da issue #{number}")

def create_contract(title, number):
    name = re.sub(r'.*\[CONTRACT\]\s*', '', title).strip()
    safe_name = ''.join(x for x in name.title() if x.isalnum())
    
    contracts_dir = Path('contracts')
    contracts_dir.mkdir(exist_ok=True)
    
    with open(contracts_dir / f'{safe_name}.sol', 'w') as f:
        f.write(f"""// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

contract {safe_name} {{
    address public owner = msg.sender;
}}""")

def create_task(title, body, number):
    tasks_dir = Path('tasks')
    tasks_dir.mkdir(exist_ok=True)
    
    with open(tasks_dir / f'task-{number}.md', 'w') as f:
        f.write(f"# {title}\n\n{body}\n\nIssue: #{number}")

if __name__ == "__main__":
    main()
