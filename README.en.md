# 📅 Lunar Vegetarian Calendar Subscription

An auto-sync subscription calendar specially designed for people who need reminders for the 1st and 15th days of the lunar month (for vegetarian eating, Buddha worship, or lifestyle planning).

[简体中文](./README.md) | [繁體中文](./README.zh-Hant.md)

## 🌟 Features
- **Extensive Coverage**: Source data covers **2026 to 2999** (974 years in total, 24094 calendar events). With automated rolling updates, subscribers only load the latest 13-month window, balancing long-term coverage and device performance.
- **Ad-Free & Clean**: Only contains reminders for the 1st and 15th days of the lunar month, with zero ads or promotions.
- **Cross-Platform Support**: Supports Apple Calendar, Google Calendar, Outlook, and various built-in Android calendars.

---

## 🔗 Subscription Links

Please choose the appropriate subscription link based on your preferred language and platform:

### 1. Simplified Chinese Version
- **Apple Calendar One-click Subscription** (iOS / macOS / iPadOS):
  👉 [**Click here to subscribe**](webcal://raw.githubusercontent.com/HenryYannis/lunar-vegetarian-calendar/main/chuyi-shiwu-simplified.ics) (If it doesn't open, copy the link below and open it in Safari)
  ```text
  webcal://raw.githubusercontent.com/HenryYannis/lunar-vegetarian-calendar/main/chuyi-shiwu-simplified.ics
  ```
- **Universal Link** (for manual setup, e.g., Google Calendar / Outlook / Android calendars):
  ```text
  https://raw.githubusercontent.com/HenryYannis/lunar-vegetarian-calendar/main/chuyi-shiwu-simplified.ics
  ```

### 2. Traditional Chinese Version
- **Apple Calendar One-click Subscription** (iOS / macOS / iPadOS):
  👉 [**Click here to subscribe**](webcal://raw.githubusercontent.com/HenryYannis/lunar-vegetarian-calendar/main/chuyi-shiwu-traditional.ics) (If it doesn't open, copy the link below and open it in Safari)
  ```text
  webcal://raw.githubusercontent.com/HenryYannis/lunar-vegetarian-calendar/main/chuyi-shiwu-traditional.ics
  ```
- **Universal Link** (for manual setup, e.g., Google Calendar / Outlook / Android calendars):
  ```text
  https://raw.githubusercontent.com/HenryYannis/lunar-vegetarian-calendar/main/chuyi-shiwu-traditional.ics
  ```

---

## 🛠️ Subscription Tutorials by Platform

### 📱 Apple Devices (iPhone / iPad)
1. Directly click the **Click here to subscribe** link above, and the system will automatically prompt you to subscribe. If clicking has no response, copy the link in the code block below, paste it in Safari, and open it.
2. Alternatively, manually add: go to **Settings -> Calendar -> Accounts -> Add Account -> Other -> Add Subscribed Calendar**, paste the universal subscription link in the "Server" field, and save.

### 💻 Mac
1. Open the built-in **Calendar** app.
2. Click **File -> New Calendar Subscription** in the top menu bar.
3. Paste the subscription link, click **Subscribe**, and set the "Location" to **iCloud** (for cross-device sync) or **On My Mac**.

### 🌐 Google Calendar
1. Sign in to the [Google Calendar Web version](https://calendar.google.com/).
2. On the left sidebar next to "Other calendars", click **"+" -> "From URL"**.
3. Paste the universal subscription link and click **Add calendar**.

### 🤖 Android Devices (Xiaomi, Huawei, OPPO, vivo, etc.)
You can usually import via URL by opening the built-in Calendar app and tapping "Add Calendar/Subscribe Calendar" under settings or account management. If your system calendar does not support direct URL import, it is recommended to add the link to your associated Google or Outlook account first, and then enable sync for that account in your phone's calendar settings.

## 📂 Project Structure

```text
├── .github/workflows/
│   └── update-feeds.yml     # GitHub Actions workflow for automated rolling updates
├── scripts/
│   ├── generate_feeds.py    # Python script to extract rolling 13-month calendar from database (no deps)
│   └── generate_all_sources.py # One-time generation script for the 2026-2999 source database (requires tyme4py)
├── sources/
│   ├── chuyi-shiwu-simplified-all.ics # Complete 2026-2999 Simplified Chinese database (6.4MB)
│   └── chuyi-shiwu-traditional-all.ics # Complete 2026-2999 Traditional Chinese database (6.4MB)
├── chuyi-shiwu-simplified.ics  # Simplified Chinese calendar feed (subscription target, auto-updated, ~7.8KB)
├── chuyi-shiwu-traditional.ics # Traditional Chinese calendar feed (subscription target, auto-updated, ~7.8KB)
├── LICENSE                     # MIT License file
└── README.en.md                # Project documentation
```

---

## 📄 License
This project is licensed under the [MIT License](LICENSE).

---

## ❤️ Credits and Disclaimer
The raw calendar data of this project is calculated, compiled, and generated based on the open-source calendar library [tyme](https://github.com/6tail/tyme4py). If you find it helpful, please star this project and share it with other vegetarian and traditional culture enthusiasts!
