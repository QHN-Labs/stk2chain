#  A GSM-Based Protocol for Expanding Blockchain Accessibility
---

STKS2Chain is a protocol designed to `bridge GSM technologies` with `blockchain systems`. It leverages the ubiquitous nature of `SIM cards` and `SMS messaging` to enable seamless `transactions`, `wallet management`, and `smart contract interactions` `without requiring an internet connection`. At its core, STK2Chain allows users to perform blockchain-based operations via familiar mobile interfaces such as STK menus, making blockchain more accessible to underserved demographics and areas with limited internet access.

---




### How it works
```mermaid

graph LR
  A(Start)

    A[STK Menu] --> B["GSM Tower Network
    (Carrier BTS)"]
    B --> C["STK2Chain Middleware
    (ERC-4337 Bundler)"]
    C --> D["Ethereum Node
    (ERC-4337 EntryPoint)"]
    D -->|TX Hash| C
    C -->|SMS Confirm| A
```

---

### eSIM Profile Architecture
```
┌───────────────────────────┐
│   eSIM Profile Elements   │
│───────────────────────────│
│  • eUICC Network Config   │
│  • STK Interface          │
│    └ Java Card Applet     │
│  • HD Wallet [stk2wallet] │
└───────────────────────────┘



┌──────────────────────────────┐
│       eSIM Profile (TEE)     │
│──────────────────────────────│
│ 1. eUICC (Secure Element)    │ ← Hardware root of trust
│ 2. Java Card Applet          │ ← Isolated execution
│ 3. ERC-4337 Wallet Logic     │ ← Code integrity
└──────────────────────────────┘
```
---

| Chain | Implementation |
|-------|----------------|
|Ethereum| [STK2ETH](./doc/SPEC.md)|


<!--


The building block fo stk2chain is the eSIM Profile that can either be burned int a UICC (SIM Card) or used on an eUICC compitible device via Remote Provisioning (Airdrop)

[ eSIM Profile ]
================
	+ eUICC Network Configurations
	+ STK Interface
		+ Javacard Applet
	+ eUICC HD Wallet
		+ stk2wallet


The eSIM Profile IMSI is a CREATE2 Wallet Smart Contract address generated by ERC-4337 Compliant Smart Contract
and Remote SIM Provisioning is done via an AirDrop

```markdown
# SMS2Chain: Blockchain via SMS/STK Menus (No Internet Needed)
*A first-principles protocol for 3B+ feature phone users*


## :triangular_flag_on_post: Why This Exists
**Problem**: 50% of humanity can't access blockchain due to:
1. No internet connectivity
2. Complex wallet interfaces
3. Smartphone dependency

**Solution**:
- Perform Ethereum transactions via basic SMS/STK menus
- eSIM acts as hardware wallet (bank-grade security)
- Works on any $2 phone


## :gear: Atomic Components

### Key Innovations
1. **CREATE2 Wallet Address**
   - IMSI number → ERC-4337 smart contract address
   - `0xIMSI = keccak256(imsi)[12:]`
2. **Airdrop Provisioning**
   ```solidity
   // Deploy wallet contract for new SIM
   function airDropSIM(bytes memory imsi) external {
       address wallet = CREATE2(imsi, "stk2wallet");
       emit WalletCreated(imsi, wallet);
   }
   ```
3. **STK Menu Flow**
   ```
   *384# → Send ETH → Enter Amount → Confirm → TX mined
   ```



## :test_tube: How It Works
1. **User** sends STK TX via USSD menu
2. **Carrier** routes request to STK2Chain middleware
3. **Middleware** converts to Ethereum TX:
   - Verifies SIM signature (Java Card Applet)
   - Broadcasts via decentralized node network
4. **Blockchain** processes TX → Confirmation SMS sent



## :rocket: Get Started
```bash
git clone https://github.com/stk2chain/core
cd core && make testnet
```
**Test**: Send 0.001 ETH via STK menu simulator:
`make send-eth to=0x... amount=0.001`

---

## :handshake: Why Build This
| **Feature**      | **Legacy Systems** | **SMS2Chain**       |
|-------------------|--------------------|---------------------|
| Internet Required | Yes                | **No**              |
| Hardware Cost     | $500+ smartphone  | **$2 SIM card**     |
| Tx Speed          | 15 sec (L1)       | **3 sec (SMS)**     |

**Join us**: [Contribution Guide](CONTRIBUTE.md) | *"Be the compiler"*
```
-->
