import datetime
import os

def update_readme():
    # 1. 路径安全检查
    if not os.path.exists("README.md"):
        print("❌ 错误：找不到 README.md")
        return

    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    # 2. 锚点定义 (必须与 README 中的注释完全一致)
    start_marker = ""
    end_marker = ""

    if start_marker not in content or end_marker not in content:
        print(f"❌ 错误：在 README 中找不到指定的锚点！")
        return

    # 3. 获取北京时间 (UTC+8) 确保高亮准确
    tz_beijing = datetime.timezone(datetime.timedelta(hours=8))
    today = datetime.datetime.now(tz_beijing).weekday()
    
    # 4. 配置训练计划
    plan = [
        ("Mon", "D32F2F", "Chest"),
        ("Tue", "F57C00", "Shoulder"),
        ("Wed", "1976D2", "Back"),
        ("Thu", "7B1FA2", "Arms"),
        ("Fri", "388E3C", "Legs_%26_Abs"),
        ("Sat", "FFD700", "Abs"),      # 满足你练腹的需求
        ("Sun", "9E9E9E", "Rest")
    ]

    # 5. 生成 HTML 代码块
    badges = []
    for i, (day, color, part) in enumerate(plan):
        # 当天高亮逻辑
        if i == today:
            label = f"🔥_{day}-{part}"
            style = "for-the-badge"
        else:
            label = f"{day}-{part}"
            style = "flat-square"
            
        badge = f'      <img src="https://img.shields.io/badge/{label}-{color}?style={style}" />'
        badges.append(badge)

    # 组合成完整的 HTML 段落
    new_html_block = (
        "\n"
        '  <p align="center" style="margin-top: 30px; margin-bottom: 30px;">\n'
        + "\n".join(badges) +
        "\n  </p>\n"
    )

    # 6. 【核心修复】：切片替换逻辑，确保旧内容被彻底移除
    start_idx = content.find(start_marker) + len(start_marker)
    end_idx = content.find(end_marker)
    
    # 拼接：锚点前内容 + 新 HTML + 锚点后内容
    new_content = content[:start_idx] + new_html_block + content[end_idx:]

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)
    
    print(f"✅ 成功更新！今日计划: {plan[today][2]}")

if __name__ == "__main__":
    update_readme()
