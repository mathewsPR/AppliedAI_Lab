# EmailJira — Accepted standards and references

Version 0.2.0 · 2026-10-22. The user accepted this baseline in the conversation. Application is proportional and document-level; no certification or full conformance claim. Requirements refer to these stable IDs. ISO full texts may require purchase; no clause references are invented.

| ID | Reference | Applicability | Official access |
| --- | --- | --- | --- |
| STD-01 | ISO/IEC/IEEE 29148:2018 | Requirements form, review, change and traceability | https://www.iso.org/standard/72089.html |
| STD-02 | ISO/IEC 25010:2023 | Relevant product quality characteristics | https://www.iso.org/standard/78176.html |
| STD-03 | NIST SP 800-218 SSDF v1.1 | Selected secure development and vulnerability practices | https://csrc.nist.gov/pubs/sp/800/218/final |
| STD-04 | OWASP ASVS 5.0 | Applicable validation, authorization, secret, communication, logging and crypto controls; web-only controls assessed for exclusion | https://github.com/OWASP/ASVS/tree/v5.0.0 |
| STD-05 | OWASP LLM Top 10, 2025 | AI threat/verification guide, not a conformance certification | https://genai.owasp.org/llm-top-10/ |
| STD-06 | RFC 8252, RFC 7636, RFC 9700 | Native-app OAuth, PKCE, security best current practice with Google guidance | https://www.rfc-editor.org/rfc/rfc8252 ; https://www.rfc-editor.org/rfc/rfc7636 ; https://www.rfc-editor.org/rfc/rfc9700 |
| STD-07 | RFC 5322, MIME RFC 2045/2046 and applicable related email specifications | Parsing/constructing messages via maintained libraries | https://www.rfc-editor.org/rfc/rfc5322 ; https://www.rfc-editor.org/rfc/rfc2045 ; https://www.rfc-editor.org/rfc/rfc2046 |
| STD-08 | SHA-256 in FIPS 180-4 | Content identities only; no FIPS module-validation claim | https://csrc.nist.gov/pubs/fips/180-4/upd1/final |
| STD-09 | PEP 8, PEP 257, Python typing guidance beginning with PEP 484 | Code style, public behavior documentation, static typing | https://peps.python.org/pep-0008/ ; https://peps.python.org/pep-0257/ ; https://peps.python.org/pep-0484/ |
| STD-10 | PEP 440 | Package-version interoperability with agreed semantic release approach | https://peps.python.org/pep-0440/ |
| REF-01 | Google desktop OAuth, Gmail API and applicable policies | Scopes, token handling, messages, drafts, sending and deployment obligations | https://developers.google.com/identity/protocols/oauth2/native-app ; https://developers.google.com/workspace/gmail/api ; https://developers.google.com/workspace/gmail/api/auth/scopes ; https://developers.google.com/workspace/workspace-api-user-data-developer-policy |
| REF-02 | Official documentation for selected Jira edition | Authentication, permissions, actor evidence, writes and rate limits; Cloud URLs conditional on Cloud selection | https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/ ; https://developer.atlassian.com/cloud/jira/platform/rate-limiting/ |
| REF-03 | Python 3.12 and SQLite | Database transactions, constraints, safe queries, backup | https://docs.python.org/3.12/library/sqlite3.html ; https://www.sqlite.org/docs.html |
| REF-04 | Windows security documentation | Account access controls and selected OS credential protection | https://learn.microsoft.com/en-us/windows/win32/api/dpapi/nf-dpapi-cryptprotectdata ; https://learn.microsoft.com/en-us/windows/win32/fileio/file-security-and-access-rights |
| REF-05 | Official uv, pytest, Ruff, mypy, LangChain, Ollama documentation | Supported tool behavior and compatible versions checked when introduced | https://docs.astral.sh/uv/ ; https://docs.pytest.org/ ; https://docs.astral.sh/ruff/ ; https://mypy.readthedocs.io/ ; https://docs.langchain.com/oss/python/langchain/overview ; https://docs.ollama.com/ |

## Applicability decisions

- DEC-10 selects restricted deterministic JSON for v0.2.0; RFC 8785 is not adopted: https://www.rfc-editor.org/rfc/rfc8785 . Do not mistake ordinary sorted JSON for a claim of full RFC 8785 conformance.
- SHA-256 detects content differences; it does not authenticate the reviewer or encrypt credentials. Canonicalization must preserve the exact protected semantics; different protected payloads cannot be treated as unchanged merely through lossy normalization.
- Gmail draft-management scopes may also permit sending. OAuth scopes do not replace the application sending guard.
- STD-04 is tailored to a local client. No blanket ASVS level is claimed. Before implementation acceptance, record exact applicable controls and exclusions using the actual standard text.
- NIST SP 800-218A may be consulted for relevant model/supplier guidance; full model-development adoption is outside scope because this project consumes a local model rather than training a foundation model.
- ISO certification, SOC 2, FIPS validation, enterprise control-framework adoption, and custom security infrastructure are not required by the agreed scope. Applicable privacy/legal/provider obligations require deployment-specific assessment (DEC-16).
- Provider documentation evolves; record documentation/version checks when implementing each integration. These links identify sources, not evidence of a working integration.
