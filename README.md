# 📅 农历初一十五（食斋/吃素）订阅日历

专门为有农历初一、十五吃素/食斋、礼佛或作息规划需求的人群设计的自动同步订阅日历。

[English](./README.en.md) | [繁體中文](./README.zh-Hant.md)

## 🌟 特色
- **超长跨度**：源数据精细覆盖 **2026 年至 2999 年**（共 974 年，24094 个日历事件）。通过云端自动更新，订阅用户仅加载最近 13 个月的滚动数据，兼顾时间跨度与设备性能。
- **纯净无感**：只包含初一和十五的事件提醒，绝无任何额外推广或垃圾广告信息。
- **全平台支持**：支持 Apple Calendar、Google Calendar、Outlook 以及各种安卓系统自带日历。

---

## 🔗 订阅链接

请根据您的设备和平台，选择下方对应的订阅方式：

- **Apple 设备一键订阅** (iOS / macOS / iPadOS)：
  👉 [**点击此链接一键订阅**](webcal://raw.githubusercontent.com/HenryYannis/lunar-vegetarian-calendar/main/chuyi-shiwu-simplified.ics)（如点击无反应，请复制下方链接在 Safari 浏览器中打开）
  ```text
  webcal://raw.githubusercontent.com/HenryYannis/lunar-vegetarian-calendar/main/chuyi-shiwu-simplified.ics
  ```
- **通用订阅链接** (用于手动添加，如 Google Calendar / Outlook / 安卓日历)：
  ```text
  https://raw.githubusercontent.com/HenryYannis/lunar-vegetarian-calendar/main/chuyi-shiwu-simplified.ics
  ```

---

## 🛠️ 各平台订阅教程

### 📱 苹果设备 (iPhone / iPad)
1. 直接点击上方的 **点击此链接一键订阅**，系统会自动弹出日历订阅请求。如果点击没有反应，请复制下方代码框中的链接，粘贴在 iPhone 的 Safari 浏览器中打开。
2. 或者手动添加：在 iPhone 上打开 **「设置」 -> 「日历」 -> 「帐户」 -> 「添加帐户」 -> 「其他」 -> 「添加已订阅的日历」**，将通用订阅链接粘贴到「服务器」处并保存。

### 💻 苹果电脑 (Mac)
1. 打开 Mac 自带的 **「日历」** 应用。
2. 点击顶部菜单栏的 **「文件」 -> 「新建日历订阅」**。
3. 粘贴上述订阅链接，点击「订阅」，并将「位置」设置为「iCloud」（可多端自动同步）或「我的 Mac」。

### 🌐 谷歌日历 (Google Calendar)
1. 登录 [Google 日历网页版](https://calendar.google.com/)。
2. 在左侧列表的「其他日历」旁，点击 **「+」 -> 「通过网址添加」**。
3. 粘贴通用订阅链接，点击「添加日历」即可。

### 🤖 安卓设备 (小米 / 华为 / OPPO / vivo 等)
通常可以通过系统自带的日历应用，点击「设置」或「帐户管理」中的「添加日历/订阅日历」通过 URL 导入。若系统日历不支持 URL，建议先将链接导入到关联的 Google / Outlook 帐户中，然后在手机日历中开启该帐户的同步。

## 📂 项目结构

```text
├── .github/workflows/
│   └── update-feeds.yml     # GitHub Actions 自动裁剪与更新日历的云端工作流
├── scripts/
│   ├── generate_feeds.py    # 用于从主库中提取 13 个月滚动日历的裁剪脚本（无依赖）
│   └── generate_all_sources.py # 使用 tyme4py 重新生成 2026-2999 年主数据库的一键脚本
├── sources/
│   ├── chuyi-shiwu-simplified-all.ics # 2026-2999 年简中完整日历主库（6.4MB）
│   └── chuyi-shiwu-traditional-all.ics # 2026-2999 年繁中完整日历主库（6.4MB）
├── chuyi-shiwu-simplified.ics  # 根目录简中日历文件（订阅入口，自动滚动更新，约 7.8KB）
├── chuyi-shiwu-traditional.ics # 根目录繁中日历文件（订阅入口，自动滚动更新，约 7.8KB）
├── LICENSE                     # MIT 开源协议文件
└── README.md                   # 项目说明文档
```

---

## 📄 开源协议
本项目基于 [MIT License](LICENSE) 开源。

---

## ❤️ 鸣谢与声明
本项目的日历原始数据基于开源历法库 [tyme](https://github.com/6tail/tyme4py) 计算、整理并生成。如果您觉得好用，欢迎 Star 关注本项目，并分享给身边的素食与传统文化爱好者！
