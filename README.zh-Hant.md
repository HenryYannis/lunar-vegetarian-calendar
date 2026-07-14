# 📅 農曆初一十五（食齋/吃素）訂閱日曆

專門為有農曆初一、十五吃素/食齋、禮佛或作息規劃需求的人群設計的自動同步訂閱日曆。

[简体中文](./README.md) | [English](./README.en.md)

## 🌟 特色
- **超長跨度**：源數據精細覆蓋 **2026 年至 2999 年**（共 974 年，24094 個日曆事件）。透過雲端自動更新，訂閱用戶僅載入最近 13 個月的滾動數據，兼顧時間跨度與設備效能。
- **純淨無感**：只包含初一和十五的事件提醒，絕無任何額外推廣或垃圾廣告訊息。
- **全平台支援**：支援 Apple Calendar、Google Calendar、Outlook 以及各種安卓系統自帶日曆。

---

## 🔗 訂閱連結

請根據您的設備和平台，選擇下方對應的訂閱方式：

- **Apple 設備一鍵訂閱** (iOS / macOS / iPadOS)：
  👉 [**點擊此連結一鍵訂閱**](webcal://raw.githubusercontent.com/HenryYannis/lunar-vegetarian-calendar/main/chuyi-shiwu-traditional.ics)（如點擊無反應，請複製下方連結在 Safari 瀏覽器中打開）
  ```text
  webcal://raw.githubusercontent.com/HenryYannis/lunar-vegetarian-calendar/main/chuyi-shiwu-traditional.ics
  ```
- **通用訂閱連結** (用於手動新增，如 Google Calendar / Outlook / 安卓行事曆)：
  ```text
  https://raw.githubusercontent.com/HenryYannis/lunar-vegetarian-calendar/main/chuyi-shiwu-traditional.ics
  ```

---

## 🛠️ 各平台訂閱教學

### 📱 蘋果設備 (iPhone / iPad)
1. 直接點擊上方的 **點擊此連結一鍵訂閱**，系統會自動彈出日曆訂閱請求。如果點擊沒有反應，請複製下方程式碼方块中的連結，貼在 iPhone 的 Safari 瀏覽器中打開。
2. 或者手動新增：在 iPhone 上打開 **「設定」 -> 「日曆」 -> 「帳號」 -> 「新增帳號」 -> 「其他」 -> 「新增已訂閱的日曆」**，將通用訂閱連結貼到「伺服器」處並儲存。

### 💻 蘋果電腦 (Mac)
1. 打開 Mac 自帶的 **「行事曆」** 應用程式。
2. 點擊頂部選單列的 **「檔案」 -> 「新建日曆訂閱」**。
3. 貼上上述訂閱連結，點擊「訂閱」，並將「位置」設定為「iCloud」（可多端自動同步）或「我的 Mac」。

### 🌐 谷歌日曆 (Google Calendar)
1. 登入 [Google 日曆網頁版](https://calendar.google.com/)。
2. 在左側列表的「其他日曆」旁，點擊 **「+」 -> 「透過網址新增」**。
3. 貼上通用訂閱連結，點擊「新增日曆」即可。

### 🤖 安卓設備 (小米 / 華為 / OPPO / vivo 等)
通常可以透過系統內建的日曆應用程式，點擊「設定」或「帳號管理」中的「新增日曆/訂閱日曆」透過 URL 匯入。若系統日曆不支援 URL，建議先將連結匯入到關聯的 Google / Outlook 帳號中，然後在手機日曆中開啟該帳號的同步。

## 📂 專案結構

```text
├── .github/workflows/
│   └── update-feeds.yml     # GitHub Actions 自動剪裁與更新日曆的雲端工作流
├── scripts/
│   ├── generate_feeds.py    # 用於從主庫中提取 13 個月滾動日曆的剪裁腳本（無相依性）
│   └── generate_all_sources.py # 使用 tyme4py 重新生成 2026-2999 年主資料庫的一鍵腳本
├── sources/
│   ├── chuyi-shiwu-simplified-all.ics # 2026-2999 年簡中完整日曆主庫（6.4MB）
│   └── chuyi-shiwu-traditional-all.ics # 2026-2999 年繁中完整日曆主庫（6.4MB）
├── chuyi-shiwu-simplified.ics  # 根目錄簡中日曆檔案（訂閱入口，自動滾動更新，約 7.8KB）
├── chuyi-shiwu-traditional.ics # 根目錄繁中日曆檔案（訂閱入口，自動滾動更新，約 7.8KB）
├── LICENSE                     # MIT 開源協議檔案
└── README.zh-Hant.md           # 專案說明文件
```

---

## 📄 開源協議
本項目基於 [MIT License](LICENSE) 開源。

---

## ❤️ 鳴謝與聲明
本項目的日曆原始數據基於開源歷法庫 [tyme](https://github.com/6tail/tyme4py) 計算、整理並生成。如果您覺得好用，歡迎 Star 關注本項目，並分享給身邊的素食與傳統文化愛好者！
