[简体中文](./README.md) | **繁體中文** | [English](./README.en.md)

# 農曆初一十五訂閱日曆

農曆初一、十五的訂閱日曆，自動更新，前一晚提醒，適合吃素、食齋、禮佛的人使用。

[![CI](https://github.com/henryyannis/lunar-vegetarian-calendar/actions/workflows/ci.yml/badge.svg)](https://github.com/henryyannis/lunar-vegetarian-calendar/actions/workflows/ci.yml)
[![Update Calendar Feeds](https://github.com/henryyannis/lunar-vegetarian-calendar/actions/workflows/update-feeds.yml/badge.svg)](https://github.com/henryyannis/lunar-vegetarian-calendar/actions/workflows/update-feeds.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## 這是什麼

- 一個 `.ics` 訂閱日曆，只包含每個農曆初一和十五，沒有廣告或其他內容。
- 每個初一、十五是一個全天事件（標題「農曆初一」「農曆十五」），不佔用忙碌時間。
- 每個事件帶一個前一天晚上 20:00 的提醒：「明天農曆初一，記得吃素」。
- 分簡體和繁體兩個版本，日期相同，只是文字不同。
- 資料涵蓋 2026 年至 2100 年（共 1856 個事件）。農曆越往後推算越不可靠，常見的公曆農曆對照表一般也只到 2100 年，所以只做到這裡。
- 訂閱檔案只放最近約 14 個月（上個月 1 日到明年同月月底），每月自動往後滾動，裝置上不會堆積幾十年的資料。
- 支援 Apple 行事曆、Google 日曆、Outlook 和大多數安卓手機內建的日曆。

## 訂閱連結

### 簡體版

- Apple 裝置一鍵訂閱：[GitHub 源](webcal://raw.githubusercontent.com/HenryYannis/lunar-vegetarian-calendar/main/chuyi-shiwu-simplified.ics) ｜ [國內加速](webcal://cdn.jsdelivr.net/gh/HenryYannis/lunar-vegetarian-calendar@main/chuyi-shiwu-simplified.ics)
- 通用連結（Google、Outlook、安卓或手動新增時使用）：
  ```text
  https://raw.githubusercontent.com/HenryYannis/lunar-vegetarian-calendar/main/chuyi-shiwu-simplified.ics
  ```
- 國內加速連結（中國大陸打不開上面的連結時使用）：
  ```text
  https://cdn.jsdelivr.net/gh/HenryYannis/lunar-vegetarian-calendar@main/chuyi-shiwu-simplified.ics
  ```

### 繁體版

- Apple 裝置一鍵訂閱：[GitHub 源](webcal://raw.githubusercontent.com/HenryYannis/lunar-vegetarian-calendar/main/chuyi-shiwu-traditional.ics) ｜ [國內加速](webcal://cdn.jsdelivr.net/gh/HenryYannis/lunar-vegetarian-calendar@main/chuyi-shiwu-traditional.ics)
- 通用連結：
  ```text
  https://raw.githubusercontent.com/HenryYannis/lunar-vegetarian-calendar/main/chuyi-shiwu-traditional.ics
  ```
- 國內加速連結：
  ```text
  https://cdn.jsdelivr.net/gh/HenryYannis/lunar-vegetarian-calendar@main/chuyi-shiwu-traditional.ics
  ```

GitHub 源和國內加速內容相同。國內加速走 jsDelivr CDN，有快取，更新可能比 GitHub 晚幾個小時。

## 各平台訂閱方法

不同系統版本的選單名稱可能略有差異。

### Apple（iPhone / iPad / Mac）

- **一鍵訂閱**：在裝置上點上面的「一鍵訂閱」連結，依提示確認即可。點了沒反應時，用下面的手動方法。
- **iPhone / iPad 手動新增**：打開「設定」→「行事曆」（iOS 18 起為「設定」→「App」→「行事曆」）→「帳號」→「加入帳號」→「其他」→「加入訂閱的行事曆」，把通用連結貼到「伺服器」，儲存。
- **Mac**：打開「行事曆」App，選單列選「檔案」→「新增行事曆訂閱」，貼上通用連結，按「訂閱」。「位置」選「iCloud」可以同步到其他 Apple 裝置。
- 訂閱時如果勾選了「移除提醒」，請取消勾選，否則收不到前一晚的提醒。

### Google 日曆

1. 在電腦瀏覽器打開 [Google 日曆](https://calendar.google.com/)（手機 App 不能透過網址新增）。
2. 左側「其他日曆」旁點「+」→「透過網址新增」。
3. 貼上通用連結，點「新增日曆」。新增後手機上的 Google 日曆也會同步顯示。

Google 日曆會忽略訂閱日曆自帶的提醒，也由它自己決定多久重新整理一次訂閱。

### Outlook

- **Outlook 網頁版 / 新版 Outlook**：打開行事曆 →「新增行事曆」→「從網路訂閱」，貼上通用連結，取個名字，點「匯入」。
- **傳統版 Outlook（Windows）**：行事曆檢視裡選「新增行事曆」→「從網際網路」，貼上通用連結，確認。

### 安卓（小米、華為、OPPO、vivo 等）

在系統內建的日曆裡找「設定」或「帳號管理」中的「新增日曆 / 訂閱日曆」，貼上通用連結。如果系統日曆不支援網址訂閱，可以先把連結新增到 Google 或 Outlook 帳號，再在手機日曆裡開啟這個帳號的同步。

## 如何更新

- GitHub Actions 工作流程 `update-feeds.yml` 每月 1 日 00:00 UTC（北京時間 08:00）執行一次；`sources/` 或 `scripts/` 在 main 上有改動時、或手動觸發時也會執行。
- 它從 `sources/` 的完整主庫裁出新的 14 個月窗口，生成根目錄的兩個訂閱檔案，再執行自檢：檢查檔案格式（RFC 5545），並用固定版本的 tyme4py 逐個核對確實是農曆初一或十五。自檢不通過就不提交。
- 每次執行都會把執行時間寫入 `last-updated.txt` 並提交，保證倉庫每月都有活動，GitHub 不會因為 60 天無活動而停用排程。
- 訂閱檔案建議用戶端每天重新整理一次（`REFRESH-INTERVAL` / `X-PUBLISHED-TTL` 為 1 天），實際重新整理頻率由各日曆 App 決定。

## 本機建置

```bash
pip install -r requirements.txt           # 固定版本的 tyme4py

python scripts/generate_feeds.py          # 從 sources/ 裁出 14 個月滾動窗口（只用標準庫）
python scripts/check_feeds.py             # 自檢訂閱檔案（裝了 tyme4py 時核對農曆日期）
python scripts/generate_all_sources.py    # 需要時重新生成 2026-2100 年主庫（需要 tyme4py）

pip install icalendar
python tests/validate_ics.py              # 用 icalendar 解析全部 .ics 並核對日期（與 CI 相同）
```

CI（`ci.yml`）在推送到 main 和每個 Pull Request 時執行：語法檢查、解析並核對已提交的 `.ics`、生成滾動日曆、自檢、再次核對生成結果。

<details>
<summary>專案結構</summary>

```text
├── .github/
│   ├── ISSUE_TEMPLATE/          # Issue 範本
│   └── workflows/
│       ├── ci.yml               # 推送和 PR 檢查：語法檢查、解析 .ics、生成並自檢
│       └── update-feeds.yml     # 每月自動生成並提交訂閱檔案
├── scripts/
│   ├── check_feeds.py           # 訂閱檔案自檢（裝了 tyme4py 時核對農曆日期）
│   ├── generate_feeds.py        # 從主庫裁出 14 個月滾動日曆（只用標準庫）
│   └── generate_all_sources.py  # 用 tyme4py 重新生成 2026-2100 年主庫
├── sources/
│   ├── chuyi-shiwu-simplified-all.ics   # 2026-2100 年簡體完整主庫（約 700KB）
│   └── chuyi-shiwu-traditional-all.ics  # 2026-2100 年繁體完整主庫（約 700KB）
├── tests/
│   └── validate_ics.py          # 用 icalendar 解析全部 .ics，核對主庫日期完整
├── chuyi-shiwu-simplified.ics   # 簡體訂閱檔案（自動滾動更新，約 11KB）
├── chuyi-shiwu-traditional.ics  # 繁體訂閱檔案（自動滾動更新，約 11KB）
├── last-updated.txt             # 每次月更執行寫入的時間
├── requirements.txt             # 固定 tyme4py 版本，避免演算法升級讓日期悄悄變化
├── SECURITY.md                  # 安全問題回報方式
└── LICENSE                      # MIT 授權條款
```

</details>

## 常見問題

**簡體版和繁體版有什麼區別？**
只有文字不同（標題、提醒、日曆名稱），日期完全一樣。選一個訂閱就夠了。

**為什麼沒收到前一晚的提醒？**
Apple 裝置請檢查訂閱時是否勾選了「移除提醒」。Google 日曆不支援訂閱日曆自帶的提醒。Outlook 和 Apple 行事曆支援。

**提醒是幾點？**
裝置當地時間前一天 20:00。

**會佔用我的忙碌時間嗎？**
不會，事件標記為「空閒」。

**2100 年以後怎麼辦？**
目前資料只到 2100 年，原因見上文。

**發現日期不對或檔案異常？**
日期錯誤請提 Issue；檔案被竄改、連結被劫持等安全問題請依 [SECURITY.md](SECURITY.md) 私下回報。

## 鳴謝

日曆資料由開源曆法庫 [tyme4py](https://github.com/6tail/tyme4py) 計算生成。覺得好用歡迎 Star，也歡迎分享給需要的人。

## 授權條款

[MIT](LICENSE) © Henry Yannis
