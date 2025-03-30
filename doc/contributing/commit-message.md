# Commit Message Guidelines

#### **Valid**:  
```  
enhance(euicc): reduce APDU response latency by 30ms 

Meet GSMA T+1 sec compliance for mass provisioning    
Latency: ≤1000ms @ 1k req/s (GSMA 5.6.2)  

Ref #43
```  
**Falsification**:   Measure APDU latency under 1k concurrent requests. **Pass**: ≤1000ms. **Fail**: >1000ms.  

```  
fix(ci): auto-delete stale Docker images  
 
Free 80GB/month on AWS ECR    
Storage freed: ≥80GB/month (ECR audit logs) 
 
DEPRECATED: /v1/auth. Use /v2/auth.

Closes #02
```  
**Falsification**:  Check AWS storage logs. **Pass**: ≥80GB freed. **Fail**: <80GB.  

#### **Rejected**:  
- `docs: update README` (Missing scope)  
- `feat(gateway): improve security` (Vague intent)  
  


# Rules 
Each commit message MUST consists of **header**, **body**, and **footer**.

1. **Zero abstractions**. Only observable code/behavior.  
1. **Intent**: Must reference **external standards** (e.g., GSMA), **SLA terms**, or **quantifiable system goals**.  
2. **Metric**: Directly tied to intent (e.g., "GSMA T+1" → `≤1000ms`).  
3. **Reject**:  
   - Intents without measurable outcomes (`Improve code quality`).  
   - Metrics unrelated to the intent (e.g., `Latency` for a storage fix). 
   - Missing type or scope

<br>


**Enforced Syntax**:  
```  
<type>(<scope>): <observable code change>  
--  
<intent: objective outcome>  
<metric>: <operator><value> [@ <test>] 
--
BREAKING|DEPRECATED: <instruction>
--
Ref|Fixes|Closes #<issueID>
``` 


### 1. **Header** (Code/Behavior Delta)  
- **Type**: `feat|fix|enhance|chore|docs|test|style`
- **Scope**: `javacard|gateway|contract|euicc|ci|benchmark`  
- **Observable Change**: *What the code physically does*.  
  - ✅ `enhance(euicc): batch APDU commands`  
  - ❌ `improve performance`  

### 2. **Intent** (Objective Outcome)  
- **1 line**: *What problem is resolved?* Must reference **external standards** or **system goals**.  
  - ✅ `Meet GSMA T+1 sec compliance for mass provisioning`  
  - ✅ `Free 80GB/month on AWS ECR`  

### 3. **Metric** (Falsifiable Pass/Fail)  
- **1 line**: `<metric>: <operator><value> [@ <test params>]`.
  - ✅ `Latency: ≤1000ms @ 1k req/s (GSMA 5.6.2)`
  - ✅ `Storage freed: ≥80GB/month (ECR audit logs) `  
  - **Value**: Derived directly from intent (e.g., `GSMA T+1` → `≤1000ms`).  
  - **Operators**: `≤` (max), `≥` (min), `=` (exact). 




## Revert commits
```
revert: <original header>  
--  
This reverts commit <SHA>.
-- 
<core reason for revert>  
```

