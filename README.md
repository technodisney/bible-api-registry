# Bible API Registry

Find where to get an English Bible. The JSON files contain the publisher, licensing, pricing, signup, caveat, and source detail.

## Find a Bible

| Translation | API | Read online |
|---|---|---|
| New International Version (NIV, NIVUK) | [API.Bible](https://api.bible/sign-up/starter) | [Bible Gateway](https://www.biblegateway.com/) |
| New International Reader's Version (NIrV) | [API.Bible](https://api.bible/sign-up/starter) | [Bible Gateway](https://www.biblegateway.com/) |
| New Living Translation (NLT) | [NLT API](https://api.nlt.to/)<br>[API.Bible](https://api.bible/sign-up/starter) | [Bible Gateway](https://www.biblegateway.com/) |
| English Standard Version (ESV, ESVUK) | [ESV API](https://api.esv.org/)<br>[API.Bible](https://api.bible/sign-up/starter) | [Bible Gateway](https://www.biblegateway.com/) |
| New English Translation (NET) | [NET API](https://labs.bible.org/api_web_service)<br>[Free Use Bible API](https://bible.helloao.org/) | [Bible Gateway](https://www.biblegateway.com/) |
| New American Standard Bible (NASB, NASB1995) | [API.Bible](https://api.bible/sign-up/starter) | [Bible Gateway](https://www.biblegateway.com/) |
| Amplified Bible (AMP, AMPC) | [API.Bible](https://api.bible/sign-up/starter) | [Bible Gateway](https://www.biblegateway.com/) |
| Christian Standard Bible (CSB, CSBA, HCSB) | [API.Bible](https://api.bible/sign-up/starter) | [Bible Gateway](https://www.biblegateway.com/) |
| New King James Version (NKJV) | [API.Bible](https://api.bible/sign-up/starter) | [Bible Gateway](https://www.biblegateway.com/) |
| King James Version (KJV, AV) | [Free Use Bible API](https://bible.helloao.org/)<br>[DailyBible API](https://dailybible.ca/api-docs)<br>[API.Bible](https://api.bible/sign-up/starter) | [Bible Gateway](https://www.biblegateway.com/) |
| American Standard Version (ASV) | [Free Use Bible API](https://bible.helloao.org/)<br>[DailyBible API](https://dailybible.ca/api-docs) | [eBible.org](https://ebible.org/) |
| World English Bible (WEB, WEBP, WEBBE, WEBC) | [Free Use Bible API](https://bible.helloao.org/)<br>[API.Bible](https://api.bible/sign-up/starter) | [eBible.org](https://ebible.org/)<br>[Bible Gateway](https://www.biblegateway.com/) |
| Darby Translation (DARBY) | [Free Use Bible API](https://bible.helloao.org/)<br>[DailyBible API](https://dailybible.ca/api-docs) | [Bible Gateway](https://www.biblegateway.com/) |
| Douay-Rheims (DRA, DRC) | [Free Use Bible API](https://bible.helloao.org/)<br>[DailyBible API](https://dailybible.ca/api-docs) | [Bible Gateway](https://www.biblegateway.com/) |
| Geneva Bible (GNV) | [Free Use Bible API](https://bible.helloao.org/) | [Bible Gateway](https://www.biblegateway.com/) |
| Revised Standard Version (RSV, RSVCE) | — | [Bible Gateway](https://www.biblegateway.com/) |
| New Revised Standard Version (NRSV, NRSVA, NRSVCE, NRSVue) | — | [Bible Gateway](https://www.biblegateway.com/) |
| New American Bible Revised Edition (NABRE) | — | [USCCB Bible](https://bible.usccb.org/bible)<br>[Bible Gateway](https://www.biblegateway.com/) |
| Common English Bible (CEB) | [API.Bible](https://api.bible/sign-up/starter) | [Bible Gateway](https://www.biblegateway.com/) |
| Good News Translation (GNT, TEV) | [API.Bible](https://api.bible/sign-up/starter) | [Bible Gateway](https://www.biblegateway.com/) |
| Contemporary English Version (CEV) | [API.Bible](https://api.bible/sign-up/starter) | [Bible Gateway](https://www.biblegateway.com/) |
| Easy-to-Read Version (ERV) | [API.Bible](https://api.bible/sign-up/starter) | [Bible Gateway](https://www.biblegateway.com/) |
| The Message (MSG) | [API.Bible](https://api.bible/sign-up/starter) | [Bible Gateway](https://www.biblegateway.com/) |
| Lexham English Bible (LEB) | — | [Lexham](https://lexhamenglishbible.com/)<br>[Bible Gateway](https://www.biblegateway.com/) |
| Complete Jewish Bible (CJB) | — | [Bible Gateway](https://www.biblegateway.com/) |
| Tree of Life Version (TLV) | — | [Bible Gateway](https://www.biblegateway.com/) |
| Free Bible Version (FBV) | [Free Use Bible API](https://bible.helloao.org/) | — |
| Berean Standard Bible (BSB) | [Free Use Bible API](https://bible.helloao.org/) | [Berean Bible](https://berean.bible/) |
| Unlocked Literal Bible (ULB) | [Free Use Bible API](https://bible.helloao.org/) | [unfoldingWord](https://www.unfoldingword.org/) |
| Young's Literal Translation (YLT) | [Free Use Bible API](https://bible.helloao.org/) | [Bible Gateway](https://www.biblegateway.com/) |

## Need the details?

- [`data/translations.json`](data/translations.json) — rights holder, every known access route, caveats, source URLs, and machine-readable `access_links`.
- [`data/providers.json`](data/providers.json) — API provider sign-up, free plan, premium cost, commercial-use threshold, restrictions, and sources.
- [`schema/translation.schema.json`](schema/translation.schema.json) and [`schema/provider.schema.json`](schema/provider.schema.json) — field definitions for tools and agents.

## Licence

Registry structure and original summaries: [CC0-1.0](LICENSE). Bible translation text, names, logos, publisher metadata, trademarks, and upstream terms remain owned by their respective rights holders.
