import datetime
import os

def update_readme():
    if not os.path.exists("README.md"):
        print("❌ 错误：找不到 README.md")
        return

    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    start_marker = ""
    end_marker = ""

    if start_marker not in content or end_marker not in content:
        print(f"❌ 错误：在 README 中找不到锚点！")
        print(f"当前文件前100个字符: {content[:100]}")
        return

    # 获取北京时间周几
    today = (datetime.datetime.utcnow() + datetime.timedelta(hours=8)).weekday()
    
    # 重新构建内容 (严格按照你刚才发的 HTML 格式)
    plan = [
        ("Mon", "D32F2F", "Chest"), ("Tue", "F57C00", "Shoulder"),
        ("Wed", "1976D2", "Back"), ("Thu", "7B1FA2", "Arms"),
        ("Fri", "388E3C", "Legs_%26_Abs"), ("Sat", "FFD700", "Rest"),
        ("Sun", "9E9E9E", "Rest")
    ]

    badges = []
    for i, (day, color, part) in enumerate(plan):
        style = "for-the-badge" if i == today else "flat-square"
        label = f"🔥_{day}-{part}" if i == today else f"{day}-{part}"
        badges.append(f'      <img src="https://img.shields.io/badge/{label}-{color}?style={style}" />')

    new_html = '\n  <p align="center" style="margin-top: 30px; margin-bottom: 30px;">\n' + \
               '\n'.join(badges) + \
               '\n  </p>\n'

    # 替换逻辑
    start_idx = content.find(start_marker) + len(start_marker)
    end_idx = content.find(end_marker)
    new_content = content[:start_idx] + new_html + content[end_idx:]

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("✅ 成功：README 已更新！")

if __name__ == "__main__":
    update_readme()
