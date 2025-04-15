# Contributing to STK2CHAIN
Thank you for your interest in contributing to STK2CHAIN.

## Contribution flow
`Issue → Fork → Branch → Commit → PR`

### 1. Pick Issue
**Make sure what you want to contribute is already traced as an issue**.

- We may discuss the problem and solution in the issue.
- Pull Requests must be linked to at least one issue in the same repo.
### 2. Create Branch

Create a Git branch from where you want to base your work. This is usually main.

**Enforced Sytax:**
```
<type>/<scope>-issueID-<atomic_issue_desc>
```

## <a name="rules"></a> Coding Rules
To ensure consistency throughout the source code, keep these rules in mind as you are working:

* All features or bug fixes **must be tested** by one or more specs (unit-tests).
* All public API methods **must be documented**.


###  <a name="commit"></a> Commit Message

<!-- Git commit messages must follow: -->

We have very precise rules over how our Git commit messages must be formatted:

**Enforced Syntax**:

```
<type>(<scope>): <observable code change>
--
<intent>
<metric>: <operator><value> [@ <test>]
--
BREAKING|DEPRECATED: <instruction>
--
Ref|Fixes|Closes #<issueID>
```
`-- BLANK LINE`



See [Commit Message Guidelines][commit-message-guidelines] for details.




[commit-message-guidelines]: ./doc/contributing/commit-message.md
