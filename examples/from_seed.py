#!/usr/bin/env python3

from eth_wallet import Wallet

import json

# Wallet seed
SEED = "bd421c81fbbb1cea7910851857817ac18f1fce9b9577a3e732ad28ae8ba4e097b072c48e694e5053df5db8a86d5cbacbbfee02b42d" \
       "12c554d06313a0dadacf6b"

# Initialize wallet
wallet = Wallet()
# Get Ethereum wallet from seed
wallet.from_seed(seed=SEED)

# Derivation from path
# wallet.from_path("m/44'/60'/0'/0/0")
# Derivation from index
wallet.from_index(44, harden=True)
wallet.from_index(60, harden=True)
wallet.from_index(0, harden=True)
wallet.from_index(0)
wallet.from_index(0, harden=True)

# Print all wallet information's
print(json.dumps(wallet.dumps(), indent=4, ensure_ascii=False))

print("Entropy:", wallet.entropy())
print("Mnemonic:", wallet.mnemonic())
print("Language:", wallet.language())
print("Passphrase:", wallet.passphrase())
print("Seed:", wallet.seed())
print("Root Private Key:", wallet.root_private_key())
print("Root Public Key:", wallet.root_public_key())
print("Uncompressed:", wallet.uncompressed())
print("Compressed:", wallet.compressed())
print("Chain Code:", wallet.chain_code())
print("Private Key:", wallet.private_key())
print("Public Key:", wallet.public_key())
print("Wallet Import Format:", wallet.wallet_import_format())
print("Finger Print:", wallet.finger_print())
print("Path:", wallet.path())
print("Address:", wallet.address())

print("---- Serialized ----")

print("Private Key Hex:", wallet.extended_key(private_key=True, encoded=False))
print("Public Key Hex:", wallet.extended_key(private_key=False, encoded=False))
print("Private Key Base58:", wallet.extended_key(private_key=True, encoded=True))
print("Public Key Base58:", wallet.extended_key(private_key=False, encoded=True))
