**简体中文** | [繁體中文](./README.zh-Hant.md) | [English](./README.en.md)

# 农历初一十五订阅日历

农历初一、十五的订阅日历，自动更新，前一晚提醒，适合吃素、食斋、礼佛的人使用。

[![CI](https://github.com/henryyannis/lunar-vegetarian-calendar/actions/workflows/ci.yml/badge.svg)](https://github.com/henryyannis/lunar-vegetarian-calendar/actions/workflows/ci.yml)
[![Update Calendar Feeds](https://github.com/henryyannis/lunar-vegetarian-calendar/actions/workflows/update-feeds.yml/badge.svg)](https://github.com/henryyannis/lunar-vegetarian-calendar/actions/workflows/update-feeds.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## 这是什么

- 一个 `.ics` 订阅日历，只包含每个农历初一和十五，没有广告或其他内容。
- 每个初一、十五是一个全天事件（标题「农历初一」「农历十五」），不占用忙碌时间。
- 每个事件带一个前一天晚上 20:00 的提醒：「明天农历初一，记得吃素」。
- 分简体和繁体两个版本，日期相同，只是文字不同。
- 数据覆盖 2026 年至 2100 年（共 1856 个事件）。农历越往后推算越不可靠，常见的公历农历对照表一般也只到 2100 年，所以只做到这里。
- 订阅文件只放最近约 14 个月（上个月 1 日到明年同月月底），每月自动往后滚动，设备上不会堆积几十年的数据。
- 支持 Apple 日历、Google 日历、Outlook 和大多数安卓手机自带的日历。

## 订阅链接

### 简体版

- Apple 设备一键订阅：[GitHub 源](webcal://raw.githubusercontent.com/HenryYannis/lunar-vegetarian-calendar/main/chuyi-shiwu-simplified.ics) ｜ [国内加速](webcal://cdn.jsdelivr.net/gh/HenryYannis/lunar-vegetarian-calendar@main/chuyi-shiwu-simplified.ics)
- 通用链接（Google、Outlook、安卓或手动添加时使用）：
  ```text
  https://raw.githubusercontent.com/HenryYannis/lunar-vegetarian-calendar/main/chuyi-shiwu-simplified.ics
  ```
- 国内加速链接（中国大陆打不开上面的链接时使用）：
  ```text
  https://cdn.jsdelivr.net/gh/HenryYannis/lunar-vegetarian-calendar@main/chuyi-shiwu-simplified.ics
  ```

### 繁体版

- Apple 设备一键订阅：[GitHub 源](webcal://raw.githubusercontent.com/HenryYannis/lunar-vegetarian-calendar/main/chuyi-shiwu-traditional.ics) ｜ [国内加速](webcal://cdn.jsdelivr.net/gh/HenryYannis/lunar-vegetarian-calendar@main/chuyi-shiwu-traditional.ics)
- 通用链接：
  ```text
  https://raw.githubusercontent.com/HenryYannis/lunar-vegetarian-calendar/main/chuyi-shiwu-traditional.ics
  ```
- 国内加速链接：
  ```text
  https://cdn.jsdelivr.net/gh/HenryYannis/lunar-vegetarian-calendar@main/chuyi-shiwu-traditional.ics
  ```

GitHub 源和国内加速内容相同。国内加速走 jsDelivr CDN，有缓存，更新可能比 GitHub 晚几个小时。

## 各平台订阅方法

不同系统版本的菜单名称可能略有差异。

### Apple（iPhone / iPad / Mac）

- **一键订阅**：在设备上点上面的「一键订阅」链接，按提示确认即可。点了没反应时，用下面的手动方法。
- **iPhone / iPad 手动添加**：打开「设置」→「日历」（iOS 18 起为「设置」→「App」→「日历」）→「账户」→「添加账户」→「其他」→「添加已订阅的日历」，把通用链接粘贴到「服务器」，存储。
- **Mac**：打开「日历」App，菜单栏选「文件」→「新建日历订阅」，粘贴通用链接，点「订阅」。「位置」选「iCloud」可以同步到其他 Apple 设备。
- 订阅时如果勾选了「移除提醒」，请取消勾选，否则收不到前一晚的提醒。

### Google 日历

1. 在电脑浏览器打开 [Google 日历](https://calendar.google.com/)（手机 App 不能通过网址添加）。
2. 左侧「其他日历」旁点「+」→「通过网址添加」。
3. 粘贴通用链接，点「添加日历」。添加后手机上的 Google 日历也会同步显示。

Google 日历会忽略订阅日历自带的提醒，也由它自己决定多久刷新一次订阅。

### Outlook

- **Outlook 网页版 / 新版 Outlook**：打开日历 →「添加日历」→「从 Web 订阅」，粘贴通用链接，起个名字，点「导入」。
- **经典版 Outlook（Windows）**：日历视图里选「添加日历」→「来自 Internet」，粘贴通用链接，确认。

### 安卓（小米、华为、OPPO、vivo 等）

在系统自带的日历里找「设置」或「账户管理」中的「添加日历 / 订阅日历」，粘贴通用链接。如果系统日历不支持网址订阅，可以先把链接添加到 Google 或 Outlook 账户，再在手机日历里打开这个账户的同步。

## 如何更新

- GitHub Actions 工作流 `update-feeds.yml` 每月 1 日 00:00 UTC（北京时间 08:00）运行一次；`sources/` 或 `scripts/` 在 main 上有改动时、或手动触发时也会运行。
- 它从 `sources/` 的完整主库裁出新的 14 个月窗口，生成根目录的两个订阅文件，再运行自检：检查文件格式（RFC 5545），并用固定版本的 tyme4py 逐个核对确实是农历初一或十五。自检不通过就不提交。
- 每次运行都会把运行时间写入 `last-updated.txt` 并提交，保证仓库每月都有活动，GitHub 不会因为 60 天无活动而停用定时任务。
- 订阅文件建议客户端每天刷新一次（`REFRESH-INTERVAL` / `X-PUBLISHED-TTL` 为 1 天），实际刷新频率由各日历 App 决定。

## 本地构建

```bash
pip install -r requirements.txt           # 固定版本的 tyme4py

python scripts/generate_feeds.py          # 从 sources/ 裁出 14 个月滚动窗口（只用标准库）
python scripts/check_feeds.py             # 自检订阅文件（装了 tyme4py 时核对农历日期）
python scripts/generate_all_sources.py    # 需要时重新生成 2026-2100 年主库（需要 tyme4py）

pip install icalendar
python tests/validate_ics.py              # 用 icalendar 解析全部 .ics 并核对日期（CI 同款）
```

CI（`ci.yml`）在推送到 main 和每个 Pull Request 时运行：语法检查、解析并核对已提交的 `.ics`、生成滚动日历、自检、再次核对生成结果。

<details>
<summary>项目结构</summary>

```text
├── .github/
│   ├── ISSUE_TEMPLATE/          # Issue 模板
│   └── workflows/
│       ├── ci.yml               # 推送和 PR 检查：语法检查、解析 .ics、生成并自检
│       └── update-feeds.yml     # 每月自动生成并提交订阅文件
├── scripts/
│   ├── check_feeds.py           # 订阅文件自检（装了 tyme4py 时核对农历日期）
│   ├── generate_feeds.py        # 从主库裁出 14 个月滚动日历（只用标准库）
│   └── generate_all_sources.py  # 用 tyme4py 重新生成 2026-2100 年主库
├── sources/
│   ├── chuyi-shiwu-simplified-all.ics   # 2026-2100 年简体完整主库（约 700KB）
│   └── chuyi-shiwu-traditional-all.ics  # 2026-2100 年繁体完整主库（约 700KB）
├── tests/
│   └── validate_ics.py          # 用 icalendar 解析全部 .ics，核对主库日期完整
├── chuyi-shiwu-simplified.ics   # 简体订阅文件（自动滚动更新，约 11KB）
├── chuyi-shiwu-traditional.ics  # 繁体订阅文件（自动滚动更新，约 11KB）
├── last-updated.txt             # 每次月更运行写入的时间
├── requirements.txt             # 固定 tyme4py 版本，避免算法升级让日期悄悄变化
├── SECURITY.md                  # 安全问题报告方式
└── LICENSE                      # MIT 协议
```

</details>

## 常见问题

**简体版和繁体版有什么区别？**
只有文字不同（标题、提醒、日历名称），日期完全一样。选一个订阅就够了。

**为什么没收到前一晚的提醒？**
Apple 设备请检查订阅时是否勾选了「移除提醒」。Google 日历不支持订阅日历自带的提醒。Outlook 和 Apple 日历支持。

**提醒是几点？**
设备当地时间前一天 20:00。

**会占用我的忙碌时间吗？**
不会，事件标记为「空闲」。

**2100 年以后怎么办？**
目前数据只到 2100 年，原因见上文。

**发现日期不对或文件异常？**
日期错误请提 Issue；文件被篡改、链接被劫持等安全问题请按 [SECURITY.md](SECURITY.md) 私下报告。

## 鸣谢

日历数据由开源历法库 [tyme4py](https://github.com/6tail/tyme4py) 计算生成。觉得好用欢迎 Star，也欢迎分享给需要的人。

## 许可证

[MIT](LICENSE) © 2026 程小宝
