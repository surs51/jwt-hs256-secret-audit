#!/usr/bin/env python3
"""
JWT HS256 secret strength audit tool.

Intended for educational purposes and authorized security testing only.
Demonstrates the risks of using low-entropy secrets with HS256-signed JWTs.
"""

import argparse
import base64
import hmac
import hashlib
import sys


def b64url_encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode()


def main():
    parser = argparse.ArgumentParser(
        description="JWT HS256 secret audit"
    )
    parser.add_argument(
        "-j", "--jwt", required=True, help="JWT token (HS256)"
    )
    parser.add_argument(
        "-w", "--wordlist", required=True, help="Path to candidate secrets file"
    )

    args = parser.parse_args()

    try:
        header_b64, payload_b64, signature_b64 = args.jwt.split(".")
    except ValueError:
        print("[-] Invalid JWT format")
        sys.exit(1)

    signing_input = f"{header_b64}.{payload_b64}".encode()

    try:
        with open(args.wordlist, "r", errors="ignore") as f:
            for line in f:
                secret = line.strip().encode()
                if not secret:
                    continue

                sig = hmac.new(
                    secret,
                    signing_input,
                    hashlib.sha256
                ).digest()

                sig_b64 = b64url_encode(sig)

                if sig_b64 == signature_b64:
                    print(f"[+] Secret found: {secret.decode()}")
                    return
    except FileNotFoundError:
        print("[-] Wordlist not found")
        sys.exit(1)

    print("[-] Secret not found")


if __name__ == "__main__":
    main()
