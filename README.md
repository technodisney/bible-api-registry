# Bible API Registry

Machine-readable data for Bible translation access and Bible API provider conditions. This registry records sources, not legal advice; confirm the current upstream terms before shipping.

## English Bible translations

| Translation | Publisher / rights holder | Places it can be accessed | Caveats with access |
|---|---|---|---|
| New International Version (NIV, NIVUK) | Biblica; Zondervan/Hodder & Stoughton distribution | • Bible Gateway web<br>• API.Bible where authorised<br>• direct Biblica/HarperCollins licence | • Generally 500-verse quotation ceiling<br>• commercial NIV unavailable under API.Bible's published commercial plan |
| New International Reader's Version (NIrV) | Biblica / Zondervan | • Bible Gateway web<br>• API.Bible where authorised | • Copyrighted; written permission beyond standard quotation terms |
| New Living Translation (NLT) | Tyndale House Foundation / Tyndale House Publishers | • Official NLT API<br>• API.Bible<br>• Bible Gateway web | • Non-commercial API use; commercial rights require permission |
| English Standard Version (ESV, ESVUK) | Crossway / Good News Publishers | • Official ESV API<br>• API.Bible where authorised<br>• Bible Gateway web | • Official API is non-commercial and limits caching/display/query size |
| New English Translation (NET) | Biblical Studies Press | • Official NET API<br>• Free Use Bible API<br>• Bible Gateway web | • No key required for API, but text remains copyrighted |
| New American Standard Bible (NASB, NASB1995) | The Lockman Foundation | • API.Bible where authorised<br>• Bible Gateway web<br>• direct licence | • Copyrighted; no standalone public API identified |
| Amplified Bible (AMP, AMPC) | The Lockman Foundation | • API.Bible where authorised<br>• Bible Gateway web<br>• direct licence | • Copyrighted; attribution and permission requirements apply |
| Christian Standard Bible (CSB, CSBA, HCSB) | Holman Bible Publishers / Lifeway | • API.Bible where authorised<br>• Bible Gateway web<br>• direct licence | • CSB has a 1,000-verse basic quotation allowance subject to conditions; HCSB is superseded |
| New King James Version (NKJV) | Thomas Nelson / HarperCollins Christian Publishing | • API.Bible where authorised<br>• Bible Gateway web<br>• direct licence | • Copyrighted; permission beyond standard quotation limits |
| King James Version (KJV, AV) | Original public-domain text; Crown rights affect UK publication | • Free Use Bible API<br>• DailyBible API<br>• API.Bible<br>• Bible Gateway web<br>• self-host verified source | • Do not describe as public domain worldwide without noting UK Crown prerogative issues |
| American Standard Version (ASV) | Original Thomas Nelson edition; public domain in the US | • Free Use Bible API<br>• DailyBible API<br>• eBible.org<br>• self-host verified source | • Historical/public-domain source; verify jurisdiction and exact edition |
| World English Bible (WEB, WEBP, WEBBE, WEBC) | Rainbow Missions / eBible.org contributors | • Free Use Bible API<br>• eBible.org<br>• API.Bible<br>• Bible Gateway web<br>• self-host | • Select and label exact spelling/canon/divine-name variant |
| Darby Translation (DARBY) | John Nelson Darby original text | • Free Use Bible API<br>• DailyBible API<br>• Bible Gateway web<br>• self-host | • Historical text; modern notes/typesetting may be copyrighted |
| Douay-Rheims (DRA, DRC) | English College at Douay / Challoner revision | • Free Use Bible API<br>• DailyBible API<br>• Bible Gateway web<br>• self-host | • Original text is historical/public domain; modern editions may be copyrighted |
| Geneva Bible (GNV) | Original 1560/1599 text public domain | • Free Use Bible API<br>• Bible Gateway web<br>• self-host historical source | • Modern editions' notes, typesetting and spelling updates may be copyrighted |
| Revised Standard Version (RSV, RSVCE) | National Council of Churches / Friendship Press | • Bible Gateway web<br>• direct licensing | • Copyrighted; basic quotation limits do not grant full-text redistribution rights |
| New Revised Standard Version (NRSV, NRSVA, NRSVCE, NRSVue) | National Council of Churches; NRSVue developed with SBL | • Bible Gateway web<br>• direct NCC/Friendship Press licensing | • Copyrighted; NRSVue is the current revision |
| New American Bible Revised Edition (NABRE) | Confraternity of Christian Doctrine / USCCB | • USCCB reading site<br>• Bible Gateway web<br>• direct licensing | • Copyrighted US Catholic translation |
| Common English Bible (CEB) | United Methodist Publishing House / Abingdon Press | • API.Bible where authorised<br>• Bible Gateway web<br>• direct permission | • Larger use may incur fees |
| Good News Translation (GNT, TEV) | American Bible Society | • API.Bible<br>• Bible Gateway web<br>• direct ABS licensing | • Copyrighted; standard quotation rules apply |
| Contemporary English Version (CEV) | American Bible Society | • API.Bible<br>• Bible Gateway web<br>• direct ABS licensing | • Commercial/full-text use requires ABS permission |
| Easy-to-Read Version (ERV) | Bible League International | • API.Bible where authorised<br>• Bible Gateway web | • Copyrighted; hosting restrictions apply |
| The Message (MSG) | NavPress / The Navigators | • API.Bible where authorised<br>• Bible Gateway web<br>• direct licence | • Paraphrase; treat substantial/commercial use as permission-required |
| Lexham English Bible (LEB) | Logos / Faithlife | • Logos/Lexham channels<br>• Bible Gateway web | • Free electronic access does not imply unrestricted commercial republication |
| Complete Jewish Bible (CJB) | David H. Stern / Messianic Jewish Publishers | • Bible Gateway web<br>• direct publisher permission | • Copyrighted; uses Jewish ordering and Hebrew names |
| Tree of Life Version (TLV) | Messianic Jewish Family Bible Society | • Bible Gateway web<br>• direct publisher permission | • Copyrighted; Hebrew names and Jewish framing |
| Free Bible Version (FBV) | Free Bible Ministry | • Free Use Bible API<br>• source/licence metadata | • Read exact licence metadata before redistribution |
| Berean Standard Bible (BSB) | Berean Bible / Bible Hub | • Free Use Bible API<br>• Bible Hub/Berean sources | • Retain verified version/licence metadata |
| Unlocked Literal Bible (ULB) | unfoldingWord | • Free Use Bible API<br>• unfoldingWord resources | • Open-licence/source-oriented text; retain attribution/licence notices |
| Young's Literal Translation (YLT) | Robert Young original text | • Free Use Bible API<br>• Bible Gateway web<br>• self-host historical source | • Historical/public-domain text; unusual literal word order |

## Bible API providers

| Provider | Sign-up | Free tier | Premium cost | Required when | Caveats |
|---|---|---|---|---|---|
| API.Bible | Account, app approval, and API key | Starter: $0; open-access Bibles plus up to 3 selected copyrighted Bibles; non-commercial | Pro from US$29/month; commercial per-translation licences publicly start around US$10/month | Any monetised use or licensed copyrighted edition required for commercial use | • 500 consecutive verses/request<br>• free tier forbids ads, subscriptions, freemium and in-app purchases<br>• copyrighted content cannot train generative AI/LLMs without written consent<br>• cached content must be refreshed at least every 30 days<br>• commercial NIV is unavailable through its published plan |
| ESV API | Free account and API key | Free for qualifying non-commercial use | No public API price; contact Crossway for expanded commercial licensing | Commercial or beyond-standard use | • 500 verses/query, cache, and display maximum<br>• 5,000/day; 1,000/hour; 60/minute<br>• copyright notice and ESV.org link required<br>• text cannot be modified<br>• Crossway can revoke access |
| NLT API | API key | Non-commercial access | No public self-service commercial price | Commercial or expanded use | • 500 verses/request and 5,000 requests/day documented for authenticated access<br>• copyright quotation limits still apply |
| NET Bible API | None | Free passage API | No published tier; commercial rights require permission | Commercial publication or product use beyond copyright terms | • Underlying NET text is copyrighted<br>• passage lookup only; no documented rate limit<br>• follow NET copyright terms |
| Bible Brain | API-key application with intended-use details | Free for qualifying non-commercial access | No public price; contact FCBH | Commercial, restricted-content, or special licensing needs | • end users must receive content free by default<br>• no proxy distribution network<br>• offline download is not generally permitted<br>• translation-specific upstream terms and faith guidelines apply |
| Digital Bible Library | Free account; organisation workflow for controlled content | Open-access/public-domain/Creative Commons content | No public standard price; rights-holder agreements vary | Controlled/copyrighted source content or organisation workflows | • licensing and content-management platform, not merely a passage API<br>• access depends on identity, organisation permissions, and per-edition licences |
| Bible Gateway API | No public self-service process documented | No public developer tier advertised | No public pricing | Treat production access as partnership/licence-gated | • technical access-token documentation exists<br>• do not rely on web scraping<br>• confirm authorisation and rights in writing |
| Free Use Bible API | None | No key or stated usage limits | None advertised | Never, per published provider model | • retain and inspect the metadata/licence for each edition<br>• provider claims commercial and modification freedom; verify provenance for high-risk production decisions |
| DailyBible API | None | Free public-domain catalogue | None advertised | Never for published public-domain editions | • small catalogue; not a broad licensed-translation provider<br>• be respectful with request volume |

## Data files

- [`data/translations.json`](data/translations.json) — one record per translation or closely related edition family.
- [`data/providers.json`](data/providers.json) — provider signup, pricing, commercial-use and restriction records.
- [`schema/translation.schema.json`](schema/translation.schema.json) and [`schema/provider.schema.json`](schema/provider.schema.json) — JSON schemas.

## Sources and contributions

Every record must include at least one first-party source URL. A public lookup endpoint does not, by itself, grant redistribution, commercial, offline-caching, derivative-work, embedding/RAG, or model-training rights.

## Licence

Registry structure and original summaries: [CC0-1.0](LICENSE). Bible translation text, names, logos, publisher metadata, trademarks, and upstream terms remain owned by their respective rights holders.
