# jwt-hs256-secret-audit
## Overview
This project demonstrates why using weak secrets with JWT HS256
signing is insecure. The tool is intended for educational purposes
and authorized security testing only.

It shows how an attacker could recover a signing secret if:
- HS256 is used
- the secret has low entropy
- no rate limiting or monitoring is in place

## What this tool does
- Validates JWT signatures using HS256
- Tests candidate secrets against a provided token
- Reports whether a weak secret was discovered

## Legal & Ethical Notice
This tool must only be used against systems you own or have
explicit permission to test. Unauthorized use may be illegal.

## Why this matters
HS256 relies on a shared secret. If that secret is weak or reused,
the integrity of authentication is compromised.

**Recommended mitigations:**
- Use strong, high-entropy secrets
- Rotate signing keys regularly
- Prefer RS256 with asymmetric keys
- Implement monitoring and token invalidation

## Usage
```bash
python jwt_audit.py --token "<JWT>" --secrets secrets.txt
