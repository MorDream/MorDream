<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=190&section=header&text=MorDream&fontSize=68&fontColor=ffffff&fontAlignY=42" width="100%" />

<p align="center">
  <b>机器人运动控制 | 强化学习 | 深度学习 | 硬件极客</b>
</p>
<p>
  <a href="https://x.com/MNetflex21939"><img src="https://img.shields.io/badge/Twitter-推特-blue" /></a>&emsp;
  <a href="https://space.bilibili.com/81380371/"><img src="https://img.shields.io/badge/Bilibili-B站-ff69b4" /></a>&emsp;
  <img src="https://komarev.com/ghpvc/?username=MorDream&label=Views&color=orange&style=flat" alt="访问量统计" />&emsp;
  <a href="https://wakatime.com/@MorDream"><img src="https://wakatime.com/badge/user/9f286187-7b92-44ef-bbfa-46acd3210eb6.svg" /></a>
</p>

</div>

---

## 💻 个人介绍 (About Me)

<div align="center">

  <p style="font-size: 16px; line-height: 1.7; max-width: 800px; margin: 0 auto;">
    我关注<b>让算法真正动起来</b>：从 IsaacGym 里的策略训练，到 MuJoCo 的仿真验证，再到真机上的关节指令。
    目前在<b>上海机器人产业技术研究院</b>做强化学习实习，负责四足机器人 Go2 的运动控制优化；
    同时在<b>华东理工大学</b>读人工智能，2026 年毕业。
  </p>

  <p style="margin-top: 18px;">
    <img src="https://img.shields.io/badge/Base-上海-0EA5E9?style=flat-square&logo=googlemaps&logoColor=white" />
    <img src="https://img.shields.io/badge/ECUST-人工智能-1E3A8A?style=flat-square" />
    <img src="https://img.shields.io/badge/SRIRI-强化学习实习-76B900?style=flat-square&logo=nvidia&logoColor=white" />
  </p>

</div>

---

## 🛠 技术矩阵 (Tech Stack)

<div align="center">

| 领域 | 技术栈 |
| :--- | :--- |
| 🤖 **机器人 / 仿真** | ROS2 · IsaacGym · IsaacLab · MuJoCo · legged_gym · rsl_rl · sim2sim / sim2real |
| 🧠 **强化学习 / 深度学习** | PPO · DQN · 奖励工程 · Diffusion (DDPM) · ViT · MoCo v2 · 对比学习 |
| 👁 **视觉 / 感知** | OpenCV 模板匹配 · ONNX Runtime · 多尺度特征融合 · 无监督异常检测 |
| 🏗 **工程 / 基础设施** | Docker · Linux · NAS · Flask · Git · ADB / scrcpy · Intel Arc XPU |
| 💻 **编程语言** | Python · C++ · MATLAB |

<br />

<img src="https://skillicons.dev/icons?i=python,cpp,c,pytorch,linux,matlab,docker,flask,git,github,vscode,latex,md,bash,nginx,ubuntu,anaconda,ps&perline=9" />

</div>

---

## 🚀 项目精选 (Featured Projects)

<div align="center">
  <sub>按投入深度排序 · 全部开源在我的 <a href="https://github.com/MorDream?tab=repositories">仓库列表</a></sub>
</div>

<br />

### ① [sim2sim](https://github.com/MorDream/sim2sim) · 四足机器人 Parkour 策略的仿真迁移

<img src="https://img.shields.io/github/stars/MorDream/sim2sim?style=flat-square&label=star&color=f5c542" />
<img src="https://img.shields.io/github/languages/top/MorDream/sim2sim?style=flat-square" />
<img src="https://img.shields.io/badge/IsaacGym-76B900?style=flat-square&logo=nvidia&logoColor=white" />
<img src="https://img.shields.io/badge/MuJoCo-4B8BBE?style=flat-square" />
<img src="https://img.shields.io/badge/sim2sim-✓-brightgreen?style=flat-square" />

策略在训练环境里跑通只是及格线，能在另一套物理引擎里站着才是本事。

- **打通 IsaacGym → MuJoCo 迁移链路**：策略经 JIT 导出为 `.pt`，改一行 `policy_path` 即可在 MuJoCo 复现，把 sim2sim 从一次性的调试动作变成可复用流程。
- **固化两套 Go2 基线**：平地任务（`go2_rough`）与野外多技能任务（`go2_field`，11 skills），配置分文件管理，便于对照实验。
- **保留实机链路**：仓库内含 `onboard_codes/` 上机部署代码与深度相机 pipeline 文档，覆盖到真机之前的最后一环。

<sub>📦 Python · PyTorch · legged_gym · rsl_rl · IsaacGym · MuJoCo</sub>

<br />

### ② [under_graduate](https://github.com/MorDream/under_graduate) · 半导体晶圆无监督缺陷检测（毕业设计）

<img src="https://img.shields.io/badge/ViT-FF9D00?style=flat-square" />
<img src="https://img.shields.io/badge/MoCo_v2-5C3EE8?style=flat-square" />
<img src="https://img.shields.io/badge/Anomaly_Detection-✓-brightgreen?style=flat-square" />
<img src="https://img.shields.io/badge/消融实验-进行中-yellow?style=flat-square" />

工业质检的痛点是「良品多、坏品少且形态未知」——没有足够异常样本，就只能做无监督。

- **自监督主干**：ViT 编码器 + MoCo v2 对比学习，只用正常样本训练；检测端用 PCA + Ledoit-Wolf 收缩协方差（参考 CFA, CVPR 2023）做马氏距离度量。
- **面向晶圆的改造**：多尺度特征融合解决微小缺陷被深层特征淹没的问题；定制数据增强保留晶圆图的物理语义，而非直接套用自然图像增强。
- **累积式消融设计**：Exp0 基线 → 多尺度 → CutPaste → 超球面约束 → SimpleNet 特征生成 → PatchCore 风格记忆库，逐模块验证独立增益（基线 AUROC 0.675，其余实验运行中）。
- **工程可复现**：一条命令切换 wafer / MVTec AD 数据集，自动适配 Intel Arc B580 (XPU) / CUDA / CPU 三档设备。

<sub>📦 PyTorch · ViT · 对比学习 · scikit-learn · OpenCV</sub>

<br />

### ③ [dqn_for_wzry](https://github.com/MorDream/dqn_for_wzry) · WZRY_AI Enhanced：DQN + CV 全自动闭环

<img src="https://img.shields.io/github/languages/top/MorDream/dqn_for_wzry?style=flat-square" />
<img src="https://img.shields.io/badge/DQN-EE4C2C?style=flat-square&logo=pytorch&logoColor=white" />
<img src="https://img.shields.io/badge/ONNX_Runtime-005CED?style=flat-square&logo=onnx&logoColor=white" />
<img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white" />

把「打一局游戏」拆成感知 → 决策 → 执行三段，然后全部自动化。

- **全流程闭环**：OpenCV 模板匹配识别活动弹窗、大厅入口、匹配确认与结算界面，配合 ADB 指令完成「启动 → 匹配 → 对局 → 结算」的无人循环。
- **学习侧实现**：DQN 智能体 + 经验回放 + 目标网络，scrcpy 实时截屏作为观测，ONNX Runtime 做前向推理加速。
- **容错处理**：针对网络波动重连、体力不足等状态加了检测与恢复逻辑，长跑不轻易卡死。

<sub>📦 Python · PyTorch · OpenCV · ONNX · ADB / scrcpy</sub>

<br />

### ④ [legged_robot](https://github.com/MorDream/legged_robot) · 运动控制环境的奖励工程改造

<img src="https://img.shields.io/github/languages/top/MorDream/legged_robot?style=flat-square" />
<img src="https://img.shields.io/badge/Reward_Design-✓-brightgreen?style=flat-square" />

强化学习调参的时间，八成花在奖励函数上，这个仓库就是那段摸索的记录。

- 在 `go2_config.py` 中增补多组奖励策略，并在 `legged_robot.py` 里完整实现对应奖励逻辑。
- 支持 go2 / go1 / a1 / anymal_b / anymal_c / cassie 多机型环境，奖励改动可横向对比。
- 设计参考 NP3O 的 Locomotion 方案，在步态稳定性与能耗之间做取舍。

<sub>📦 Python · PyTorch · IsaacGym · legged_gym</sub>

<br />

### 📚 更多项目

| 项目 | 一句话说明 | 技术 |
| :--- | :--- | :--- |
| **[py_wol](https://github.com/MorDream/py_wol)** | 局域网远程唤醒工具，Web 界面一键扫描 / 保存 / 唤醒 NAS 与 ITX 主机，已发布 Docker 镜像 | `Flask` `Docker` `UDP` |
| **[diffusion-for-MINST](https://github.com/MorDream/diffusion-for-MINST)** | 单文件从零实现 DDPM，在 MNIST 上完成训练与采样 | `PyTorch` `Diffusion` |
| **[hermes-pet](https://github.com/MorDream/hermes-pet)** ★2 | 把 OpenPet 桌宠接进 Hermes Agent：事件钩子、看门狗、定时巡检、WSL 路径修复 | `Shell` `Agent Skill` |
| **[hermes-nailong-skin](https://github.com/MorDream/hermes-nailong-skin)** ★3 | Hermes Agent 主题皮肤 + 角色扮演提示词工程，写进 agent memory 开机自加载 | `YAML` `Prompt` |
| **[agent-learning-plan](https://github.com/MorDream/agent-learning-plan----hello-agent)** | 跟着《Hello-Agents》系统啃 Agent 原理，并沉淀自己的实现代码 | `Python` `LLM` |

---

## 🛰 个人历程 (The Journey)

<div align="center">
  <table border="0" width="100%">
    <tr>
      <td width="22%" align="center"><b>2025 - 至今</b></td>
      <td><b>上海机器人产业技术研究院 (SRIRI)</b><br/>强化学习实习生 · 四足机器人 Go2 运动控制优化 · Parkour 策略 sim2sim 迁移</td>
    </tr>
    <tr>
      <td width="22%" align="center"><b>2026</b></td>
      <td><b>毕业设计</b><br/>半导体晶圆无监督缺陷检测 · ViT + MoCo v2 · 累积式消融实验</td>
    </tr>
    <tr>
      <td width="22%" align="center"><b>2022 - 2026</b></td>
      <td><b>华东理工大学 (ECUST)</b><br/>人工智能 · 算法与硬件边界的持续探索</td>
    </tr>
  </table>
</div>

---

## 🤖 AI Agent 工作流 (Agentic Workflow)

<div align="center">
  <p style="max-width: 820px; margin: 0 auto; line-height: 1.8;">
    <i>把 AI Agent 当作「结对工程师」，而不是代码补全器。</i><br/>
    习惯先让 Agent 读仓库、拆任务、跑测试，再看它产出的 diff ——
    在机器人算法与强化学习项目里，它替我接走了环境踩坑、实验脚本编排和文档同步这些体力活，
    我负责定义问题、审阅结果与最终判断。
  </p>
</div>

<br />

<div align="center">
  <table border="0" width="95%">
    <tr>
      <td align="center" width="25%">🧭 <b>规划</b><br/><sub>需求拆解 · 方案对比<br/>上下文调研</sub></td>
      <td align="center" width="25%">⚙️ <b>编码</b><br/><sub>多文件重构 · 脚本生成<br/>跨语言迁移</sub></td>
      <td align="center" width="25%">🧪 <b>验证</b><br/><sub>跑单测 · 复现报错<br/>日志归因</sub></td>
      <td align="center" width="25%">🚀 <b>交付</b><br/><sub>提交规范 · 文档同步<br/>实验归档</sub></td>
    </tr>
  </table>
</div>

<br />

<div align="center">
  <img src="https://img.shields.io/badge/WorkBuddy-6C5CE7?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Claude_Code-D97757?style=for-the-badge&logo=anthropic&logoColor=white" />
  <img src="https://img.shields.io/badge/Cursor-111111?style=for-the-badge&logo=cursor&logoColor=white" />
  <img src="https://img.shields.io/badge/GitHub_Copilot-1F6FEB?style=for-the-badge&logo=githubcopilot&logoColor=white" />
  <img src="https://img.shields.io/badge/OpenAI_Codex-412991?style=for-the-badge&logo=openai&logoColor=white" />
  <img src="https://img.shields.io/badge/Gemini_CLI-4285F4?style=for-the-badge&logo=googlegemini&logoColor=white" />
</div>

<br />

<div align="center">
  <table border="0" width="85%">
    <tr>
      <td align="center" width="50%" height="80">
        <b>🪄 上下文优先</b><br/>
        <sub>给足背景与约束，<br/>而不是丢一句需求就等结果</sub>
      </td>
      <td align="center" width="50%">
        <b>🔍 可验证优先</b><br/>
        <sub>让 Agent 自己跑测试，<br/>用输出说话而不是用自信说话</sub>
      </td>
    </tr>
    <tr>
      <td align="center" height="80">
        <b>🧩 小步提交</b><br/>
        <sub>每步都可回滚，<br/>拒绝不可控的大块 diff</sub>
      </td>
      <td align="center">
        <b>🧠 人类兜底</b><br/>
        <sub>架构决策与最终 Review<br/>始终由人把关</sub>
      </td>
    </tr>
  </table>
</div>

<br />

<div align="center">
  <sub>不止于用 —— 也动手改造 Agent 本身：<a href="https://github.com/MorDream/hermes-pet">hermes-pet</a> 给它接上桌宠，<a href="https://github.com/MorDream/hermes-nailong-skin">hermes-nailong-skin</a> 给它换上皮囊。</sub>
</div>

---

## 📈 活跃度 (Contributions)

<div align="center">

  <img src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=MorDream&theme=radical" width="33%" />
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=MorDream&theme=radical" width="33%" />
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=MorDream&theme=radical" width="33%" />

  <br /><br />

  <img src="https://github-readme-streak-stats.herokuapp.com/?user=MorDream&theme=tokyonight&hide_border=true" width="100%" />

</div>

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=soft&color=gradient&customColorList=12&height=3" width="100%" />
</div>

## 🐍 活跃度矩阵 (Contribution Snake)

<div align="center">
  <img src="https://raw.githubusercontent.com/MorDream/MorDream/output/github-contribution-grid-snake.svg" alt="Snake animation" width="100%" />
</div>

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=soft&color=gradient&customColorList=12&height=3" width="100%" />
</div>

## 🎯 目标 (Goals)

<div align="center">
  <table border="0" width="85%">
    <tr>
      <td align="center" width="50%" height="90">
        <b>🎯 近期</b><br/>
        <sub>把晶圆检测的消融实验跑完，<br/>补上从 0.675 到可用的那一段</sub>
      </td>
      <td align="center" width="50%">
        <b>🧭 长期</b><br/>
        <sub>探索强化学习与硬件的结合点，<br/>做能在物理世界跑通的策略</sub>
      </td>
    </tr>
    <tr>
      <td align="center" height="90">
        <b>📖 持续</b><br/>
        <sub>系统补齐 Agent 与具身智能的理论，<br/>不止停留在调包</sub>
      </td>
      <td align="center">
        <b>🌱 开源</b><br/>
        <sub>把踩过的坑写成文档，<br/>让下一个人少走一遍</sub>
      </td>
    </tr>
  </table>
</div>

---

## 🎨 生活灵感 (Life & Interests)

<div align="center">
  <table border="0">
    <tr>
      <td align="center">📸 <b>摄影</b><br/><small>捕捉工业纹理</small></td>
      <td width="40"></td>
      <td align="center">🏗️ <b>ITX</b><br/><small>极限空间美学</small></td>
      <td width="40"></td>
      <td align="center">🚴 <b>骑行</b><br/><small>破风中的思考</small></td>
    </tr>
    <tr height="20"></tr>
    <tr>
      <td align="center">🏋️ <b>健身</b><br/><small>自律即是自由</small></td>
      <td width="40"></td>
      <td align="center">🐈 <b>撸猫</b><br/><small>碳基生物疗愈</small></td>
      <td width="40"></td>
      <td align="center">🎵 <b>音乐</b><br/><small>逻辑的共鸣</small></td>
    </tr>
  </table>
</div>

<h4>健身计划</h4>
<!-- FITNESS:START -->
  <p align="center" style="margin-top: 30px; margin-bottom: 30px;">
      <img src="https://img.shields.io/badge/Mon-Chest-D32F2F?style=flat-square" />
      <img src="https://img.shields.io/badge/Tue-Shoulder-F57C00?style=flat-square" />
      <img src="https://img.shields.io/badge/Wed-Back-1976D2?style=flat-square" />
      <img src="https://img.shields.io/badge/Thu-Arms-7B1FA2?style=flat-square" />
      <img src="https://img.shields.io/badge/Fri-Legs_%26_Abs-388E3C?style=flat-square" />
      <img src="https://img.shields.io/badge/🔥_Sat-Abs-FFD700?style=for-the-badge" />
      <img src="https://img.shields.io/badge/Sun-Rest-9E9E9E?style=flat-square" />
  </p>
<!-- FITNESS:END -->

<div align="center">
  <div style="margin-top: 20px;">
    <img src="./image/README/942035114-2064762205.suf.jpg" width="300" style="border-radius: 10px; margin-bottom: 12px;" />
    <p style="margin-bottom: 10px;"><b>🐈 撸猫时刻</b></p>
    <img src="https://img.shields.io/badge/Status-Purring-ff69b4?style=flat-square" />
    <img src="https://img.shields.io/badge/Energy-100%25-brightgreen?style=plastic" />
  </div>
</div>

---

## 📞 联系我 (Contact Me)

<div align="center">
  <p>对机器人、强化学习，或者任何「让代码动起来」的事感兴趣，都欢迎聊聊。</p>
  <p>
    <a href="https://x.com/MNetflex21939" target="_blank"><img src="https://img.shields.io/badge/Twitter-1DA1F2?style=flat&logo=twitter&logoColor=white" /></a>&emsp;
    <a href="https://space.bilibili.com/81380371/" target="_blank"><img src="https://img.shields.io/badge/Bilibili-FF69B4?style=flat&logo=bilibili&logoColor=white" /></a>&emsp;
    <a href="https://wakatime.com/@MorDream" target="_blank"><img src="https://img.shields.io/badge/WakaTime-000000?style=flat&logo=wakatime&logoColor=white" /></a>&emsp;
    <a href="https://github.com/MorDream" target="_blank"><img src="https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white" /></a>
  </p>
</div>

<br />

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=120&section=footer" width="100%" />
  <p style="margin-top: 16px; font-size: 14px; color: #666;">© 2026 MorDream · Keep the policy running.</p>
</div>
