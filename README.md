# Bible API Registry

A **human- and machine-readable** registry of English Bible translations and Bible-content API providers.

> Status: researched 2026-07-26. This is research, not legal advice. Always read the current upstream licence before shipping a product.

## Machine-readable data

- [`data/translations.json`](data/translations.json) — translation-level publisher, access and caveat records.
- [`data/providers.json`](data/providers.json) — provider signup, pricing, commercial-use and restriction records.
- [`schema/translation.schema.json`](schema/translation.schema.json) — JSON Schema for translation records.
- [`schema/provider.schema.json`](schema/provider.schema.json) — JSON Schema for provider records.

## Human-readable guidance

### Sensible defaults

| Need | Recommended route |
|---|---|
| NLT + ESV church lookup | Official NLT API + official ESV API; comply with both attribution and non-commercial terms. |
| Several modern copyrighted translations | API.Bible, after checking the authenticated catalogue and commercial status. |
| Commercial/offline/indexed application | Use only editions whose own licence permits that use, or obtain publisher licences. |
| Multilingual audio/video | Bible Brain; check each fileset and upstream licence. |
| Public-domain fallback | WEB, ASV, historic KJV, Darby, or Douay-Rheims—using a verified source and exact edition label. |

### Contribution rule

A record must include at least one first-party source. Do not infer a redistribution, commercial, AI-training, offline-caching, or derivative-work right merely from a public lookup endpoint.

## Validation

```bash
python3 -m unittest discover -s tests -v
```

## Licence

The registry structure and original summaries are released under [CC0-1.0](LICENSE). Bible translation text, names, logos, metadata, and upstream terms remain owned by their respective rights holders.
