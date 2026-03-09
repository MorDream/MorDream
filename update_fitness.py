import datetime
import time

# 强制使用北京时间 (UTC+8)
def get_beijing_weekday():
    # 获取当前 UTC 时间并加 8 小时
    beijing_time = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
    return beijing_time.weekday()

def generate_badges():
    today = get_beijing_weekday() # 使用校准后的北京时间
    badges = []
    
    # 增加一个时间戳参数 ?t=xxx 绕过 GitHub 缓存
    timestamp = int(time.time())
    
    for i, (day, color, part) in enumerate(PLAN):
        if i == today:
            label = f"🔥_{day}-{part}"
            style = "for-the-badge"
        else:
            label = f"{day}-{part}"
            style = "flat-square"
            
        # 在 URL 最后加上 &t={timestamp} 骗过缓存
        badge = f'<img src="https://img.shields.io/badge/{label}-{color}?style={style}&t={timestamp}" />'
        badges.append(badge)
    
    return "    " + "\n    ".join(badges)