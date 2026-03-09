import datetime

# 定义每天的计划配置：(显示文字, 颜色, 训练部位)
PLAN = [
    ("Mon", "D32F2F", "Chest"),        # 0: 周一
    ("Tue", "F57C00", "Shoulder"),     # 1: 周二
    ("Wed", "1976D2", "Back"),         # 2: 周三
    ("Thu", "7B1FA2", "Arms"),         # 3: 周四
    ("Fri", "388E3C", "Legs_%26_Abs"), # 4: 周五
    ("Sat", "FFD700", "Abs"),          # 5: 周六
    ("Sun", "9E9E9E", "Rest")          # 6: 周日
]

def generate_badges():
    today = datetime.datetime.now().weekday()  # 获取今天周几 (0-6)
    badges = []
    
    for i, (day, color, part) in enumerate(PLAN):
        # 如果是今天，使用 for-the-badge 样式并加火苗图标
        if i == today:
            label = f"🔥_{day}-{part}"
            style = "for-the-badge"
        else:
            label = f"{day}-{part}"
            style = "flat-square"
            
        badge = f'<img src="https://img.shields.io/badge/{label}-{color}?style={style}" />'
        badges.append(badge)
    
    return "    " + "\n    ".join(badges)

def update_readme():
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    start_marker = ""
    end_marker = ""
    
    start_idx = content.find(start_marker) + len(start_marker)
    end_idx = content.find(end_marker)
    
    new_section = f'\n<p align="center" style="margin-top: 30px; margin-bottom: 30px;">\n{generate_badges()}\n</p>\n'
    
    new_content = content[:start_idx] + new_section + content[end_idx:]
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)

if __name__ == "__main__":
    update_readme()