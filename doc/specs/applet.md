# STK2ETH JavaCard Applet Specifications

<img src="../Consumer_eUICC.excalidraw.svg" />

## Trusted Execution Environment
|Component| Function|
|---------|-------------------------|
|`eUICCs` |  Hardware root of trust.|
|`Java Card VM` | Isolated execution environment.|

We leverages the eUICCs as a hardware root of trust, operating within the isolated execution environment of the Java Card VM, effectively creating a Trusted Execution Environment (TEE).

This secure, isolated compute environment guarantees:
  - Confidentiality: Private keys cannot be read externally.
        No seed phrases.
        Keys are generated and stored exclusively within the eUICC Secure Element, ensuring they never leave.
  - Integrity: Code execution is tamper-proof.
        Ensured by the combination of the Attested Java Card VM, eUICC and ERC-4337 wallet.
  - Attestation: Proof of execution in a trusted environment.
        Transactions are signed exclusively within the Java Card VM.


This design enables a non-custodial, optimally secure, seedless ERC-4337 mobile wallet by using eSIM Profiles as Trusted Execution Environments (TEE).
It’s highly inspired by Daimo’s and Taisys' models, combining and extending them by leveraging eUICC secure enclaves operating within the isolated execution environment of the Java Card VM for key generation, signing and attestation.


## Private Key Generation and Storage

No seed phrases. Keys are generated and stored `exclusively` within the eUICC Secure Element. Private keys cannot be read externally, `they never leave`.
Private keys cannot be read externally.
Private keys cannot be read externally.

1. Keys are generated and stored exclusively within the eUICC Secure Element ( hardware root of trust )
2. No seed phrases - keys never leave the Secure Element and cannot be read external of applet's Java Card VM TEE (isolated execution environment)

<br/>

#### Must TestCase
1. Keys are generated `exclusively` within the Java Card VM (isolated execution environment).
2. Keys are stored `exclusively` within the eUICC Secure Element ( hardware root of trust )
3. No seed phrases - keys never leave the Secure Element.
4. Keys cannot be read external of applet's Java Card VM (isolated execution environment)
5. Access Policy is by default exclusive to the applet signature
6. 2 applets by deafault cannot have the same signature
7. By default All is erased when applet is erased

### Key Derivation
Uses `SECP236r1`(P-256) with future support for Ed25519. Follows `m/44'/60'/0'/0/x` derivation path (BIP-32,BIP-44 compliant).

- secp256k1 : [BTC/ETH]
- secp256r1: Rest of world  (our default)

| Curve			| Blockchain Use		|		Non-Blockchain Use		|	Security Level	|	Java Card Support |
|-----------|-------------------|-------------------------|-----------------|-------------------|
|secp256k1	|	Bitcoin, Ethereum	|		Rare outside blockchain|			128-bit		|	❌ No official support
|secp256r1 (P-256)	|XRP, Hedera				|TLS, Passkeys, Apple, Google, FIDO2|	128-bit			| ✅ Yes
|Ed25519			|Monero, Solana, NEAR, Polkadot|		SSH, Signal, Tor, WebAuthn|		128-bit			| ✅ Yes
|Ed448			|Limited					|FIDO2, Post-Quantum Research|		224-bit			| ✅ Yes


<!-- R1: [ DeepSeek, P-256, Yamaha, PlayStation ] #M1 -->

#### Summary

| Step		|	Action |
|---------|--------|
|🔹 No Seed Phrase	|Keys stored inside Secure Enclave, generated securely|
|🔹 BIP-32 secp256r1	|Follow m/44'/60'/0'/0/x derivation|
|🔹 Ethereum Address|	Compute from secp256r1 public key → keccak256 → EIP-55|
|🔹 MetaMask Import|	Document path for future R1 support|
|🔹 Security		|Private keys never leave enclave|



     SAIP v3.3.1 Compliant eUICC Unprotected Profile Package
        Application Element (Java Card Applet):
              Implements a Text-Based User Interface for:
                1. Deposit
                2. Send ETH
                3. Swap
                4. Check Balance

            Private Key Generation and storage:
                 1. Keys are generated and stored exclusively within the eUICC Secure Element ( hardware root of trust )
                   2. No seed phrases - keys never leave the Secure Element

            Signing Logic:
                  1. Transaction are signed exclusively within the Java Card VM (Trusted Execution Environment) using the Generated Key


        ERC-4337 Contract Metadata Element
                Part of Attestation process

        Other Profile Elements
                Multi IMSI eSIM with automatic failover


    ERC-4337 contract wallet.

        Treats a H(Bound Profile Package data) + H(eUICC info (Chip)) + SK.sig as an Attested Signer                
        Delegates signing to the Trusted Execution Environment (TEE)

## UserOp Signing
Transactions are signed `exclusively` within the Java Card VM (isolated execution environment) using the Generated Key.

## USSD Submission

## Text-Based User Interface (STK Menu)
1. Send ETH
2. Swap
3. Withdraw Cash
4. Buy Airtime
5. My Account
6. Check Balance


```JSON
{

"MainScreen": {
			"text": "xQuid Main Menu",
			"screen_type": "Menu",
			"default_next_screen": "DefaultNoneScreen",
			"menu_items": {
				"SendETHOption": {
					"option": "1",
					"display_name": "Send ETH",
					"next_screen": "SendETHScreen"
				},
                "SwapOption": {
                    "option": "2",
					"display_name": "Swap",
					"next_screen": "SwapScreen"
				},
                "WithdrawOption": {
					"option": "3",
					"display_name": "Withdraw Cash",
					"next_screen": "WithdrawScreen"
				},
			    "AirtimeOption": {
					"option": "4",
					"display_name": "Buy Airtime",
					"next_screen": "AirtimeScreen"
				},
                "AccountOption": {
					"option": "5",
					"display_name": "My Account",
					"next_screen": "AccountScreen"
				},
               "BalanceOption": {
					"option": "6",
					"display_name": "Balance",
					"next_screen": "BalanceScreen"
				},
			}
		},
}
```

## Protocol

- [**USSD-ETH Gateway**](./specs/middleware.md) - The STK2ETH USSD-ETH Gateway.
- [**JavaCard Applet (eSTK)**](./tx-format/index.md) - The STK2ETH JavaCard Applet.
-
