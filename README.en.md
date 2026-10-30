[简体中文](./README.md) | [繁體中文](./README.zh-Hant.md) | **English**

# Lunar Vegetarian Calendar

A subscribable calendar of the 1st and 15th days of each Chinese lunar month, updated automatically, with a reminder the evening before. Made for people who eat vegetarian or worship on those days.

[![CI](https://github.com/henryyannis/lunar-vegetarian-calendar/actions/workflows/ci.yml/badge.svg)](https://github.com/henryyannis/lunar-vegetarian-calendar/actions/workflows/ci.yml)
[![Update Calendar Feeds](https://github.com/henryyannis/lunar-vegetarian-calendar/actions/workflows/update-feeds.yml/badge.svg)](https://github.com/henryyannis/lunar-vegetarian-calendar/actions/workflows/update-feeds.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## What it is

- An `.ics` subscription calendar with only the lunar 1st (初一) and 15th (十五) of each month. No ads, nothing else.
- Each one is an all-day event (titled 农历初一 / 农历十五) marked as free, so it doesn't block your time.
- Each event has an alert at 20:00 the evening before: "明天农历初一，记得吃素" ("Tomorrow is the lunar 1st, remember to eat vegetarian").
- There are two versions, Simplified and Traditional Chinese. The dates are the same; only the text differs. Event text is in Chinese in both.
- The data covers 2026 to 2100 (1856 events). Lunar calculations get less reliable the further out they go, and common Gregorian–lunar conversion tables generally stop around 2100, so the data stops there.
- The subscription file only holds about 14 months (from the 1st of last month to the end of the same month next year) and rolls forward every month, so your device doesn't load decades of events.
- Works with Apple Calendar, Google Calendar, Outlook, and most built-in Android calendars.

## Subscription links

### Simplified Chinese

- One-click subscribe on Apple devices: [GitHub](webcal://raw.githubusercontent.com/HenryYannis/lunar-vegetarian-calendar/main/chuyi-shiwu-simplified.ics) | [China CDN](webcal://cdn.jsdelivr.net/gh/HenryYannis/lunar-vegetarian-calendar@main/chuyi-shiwu-simplified.ics)
- Universal link (for Google, Outlook, Android, or adding manually):
  ```text
  https://raw.githubusercontent.com/HenryYannis/lunar-vegetarian-calendar/main/chuyi-shiwu-simplified.ics
  ```
- China CDN link (use this if the link above doesn't load from mainland China):
  ```text
  https://cdn.jsdelivr.net/gh/HenryYannis/lunar-vegetarian-calendar@main/chuyi-shiwu-simplified.ics
  ```

### Traditional Chinese

- One-click subscribe on Apple devices: [GitHub](webcal://raw.githubusercontent.com/HenryYannis/lunar-vegetarian-calendar/main/chuyi-shiwu-traditional.ics) | [China CDN](webcal://cdn.jsdelivr.net/gh/HenryYannis/lunar-vegetarian-calendar@main/chuyi-shiwu-traditional.ics)
- Universal link:
  ```text
  https://raw.githubusercontent.com/HenryYannis/lunar-vegetarian-calendar/main/chuyi-shiwu-traditional.ics
  ```
- China CDN link:
  ```text
  https://cdn.jsdelivr.net/gh/HenryYannis/lunar-vegetarian-calendar@main/chuyi-shiwu-traditional.ics
  ```

The GitHub and China CDN links serve the same content. The CDN link goes through jsDelivr, which caches files, so it may update a few hours later than GitHub.

## How to subscribe

Menu names may differ slightly between system versions.

### Apple (iPhone / iPad / Mac)

- **One-click**: open one of the one-click links above on your device and confirm. If nothing happens, use the manual steps below.
- **iPhone / iPad, manually**: go to **Settings → Calendar** (on iOS 18 and later, **Settings → Apps → Calendar**) **→ Accounts → Add Account → Other → Add Subscribed Calendar**, paste the universal link into **Server**, and save.
- **Mac**: open the **Calendar** app, choose **File → New Calendar Subscription**, paste the universal link, and click **Subscribe**. Set **Location** to **iCloud** to sync to your other Apple devices.
- If **Remove Alerts** is ticked when you subscribe, untick it, or you won't get the evening-before alert.

### Google Calendar

1. Open [Google Calendar](https://calendar.google.com/) in a computer browser (the mobile app can't add calendars by URL).
2. Next to **Other calendars** on the left, click **+ → From URL**.
3. Paste the universal link and click **Add calendar**. It then shows up in the Google Calendar app on your phone too.

Google Calendar ignores alerts embedded in subscribed calendars, and decides on its own how often to refresh a subscription.

### Outlook

- **Outlook on the web / new Outlook**: open the calendar → **Add calendar → Subscribe from web**, paste the universal link, give it a name, and click **Import**.
- **Classic Outlook (Windows)**: in the calendar view, choose **Add Calendar → From Internet**, paste the universal link, and confirm.

### Android (Xiaomi, Huawei, OPPO, vivo, etc.)

In the built-in calendar app, look for **Add calendar / Subscribe to calendar** under settings or account management, and paste the universal link. If your calendar can't subscribe by URL, add the link to your Google or Outlook account first, then turn on sync for that account in your phone's calendar.

## How it updates

- The GitHub Actions workflow `update-feeds.yml` runs at 00:00 UTC on the 1st of every month (08:00 Beijing time). It also runs when `sources/` or `scripts/` change on main, and when triggered manually.
- It cuts the new 14-month window out of the full source files in `sources/`, writes the two subscription files in the repository root, and runs a self-check: file format (RFC 5545), plus a check with the pinned tyme4py version that every date really is a lunar 1st or 15th. If the check fails, nothing is committed.
- Every run writes the run time to `last-updated.txt` and commits it, so the repository has activity every month and GitHub doesn't disable the schedule after 60 days of inactivity.
- The subscription files ask calendar apps to refresh once a day (`REFRESH-INTERVAL` / `X-PUBLISHED-TTL` of 1 day). How often an app actually refreshes is up to the app.

## Build locally

```bash
pip install -r requirements.txt           # pinned tyme4py

python scripts/generate_feeds.py          # cut the 14-month window from sources/ (standard library only)
python scripts/check_feeds.py             # self-check the feeds (verifies lunar dates when tyme4py is installed)
python scripts/generate_all_sources.py    # regenerate the 2026-2100 source files if needed (requires tyme4py)

pip install icalendar
python tests/validate_ics.py              # parse every .ics with icalendar and verify dates (same as CI)
```

CI (`ci.yml`) runs on every push to main and every pull request: syntax check, parse and verify the committed `.ics` files, generate the rolling feeds, self-check, and verify the generated feeds again.

<details>
<summary>Project structure</summary>

```text
├── .github/
│   ├── ISSUE_TEMPLATE/          # Issue templates
│   └── workflows/
│       ├── ci.yml               # Push and PR checks: syntax check, parse .ics, generate and self-check
│       └── update-feeds.yml     # Monthly job that generates and commits the feeds
├── scripts/
│   ├── check_feeds.py           # Feed self-check (verifies lunar dates when tyme4py is installed)
│   ├── generate_feeds.py        # Cuts the 14-month rolling feed from the source files (standard library only)
│   └── generate_all_sources.py  # Regenerates the 2026-2100 source files with tyme4py
├── sources/
│   ├── chuyi-shiwu-simplified-all.ics   # Full 2026-2100 Simplified Chinese source (~700KB)
│   └── chuyi-shiwu-traditional-all.ics  # Full 2026-2100 Traditional Chinese source (~700KB)
├── tests/
│   └── validate_ics.py          # Parses every .ics with icalendar and checks the source dates are complete
├── chuyi-shiwu-simplified.ics   # Simplified Chinese feed (rolls forward automatically, ~11KB)
├── chuyi-shiwu-traditional.ics  # Traditional Chinese feed (rolls forward automatically, ~11KB)
├── last-updated.txt             # Time of the latest monthly run
├── requirements.txt             # Pins tyme4py so an algorithm update can't silently shift dates
├── SECURITY.md                  # How to report security problems
└── LICENSE                      # MIT License
```

</details>

## FAQ

**What's the difference between the Simplified and Traditional versions?**
Only the text (event titles, alerts, calendar name). The dates are identical. Subscribe to one.

**Why didn't I get the evening-before alert?**
On Apple devices, check whether **Remove Alerts** was ticked when subscribing. Google Calendar doesn't support alerts in subscribed calendars. Outlook and Apple Calendar do.

**What time is the alert?**
20:00 the day before, in your device's local time.

**Will it show me as busy?**
No, the events are marked as free.

**What about after 2100?**
The data currently ends in 2100, for the reason above.

**Found a wrong date or a broken file?**
Open an issue for wrong dates. For security problems such as a tampered file or a hijacked link, report privately as described in [SECURITY.md](SECURITY.md).

## Credits

The calendar data is calculated with the open-source calendar library [tyme4py](https://github.com/6tail/tyme4py). If you find it useful, a star or a share is welcome.

## License

[MIT](LICENSE) © Henry Yannis
