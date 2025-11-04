import random
import math
from datetime import datetime

try:
    from zoneinfo import ZoneInfo
    _tz = ZoneInfo("America/New_York")
except Exception:
    _tz = None

def get_lucky_number(r=(1, 100)):
    a, b = r
    if a > b:
        a, b = b, a
    nums = list(range(a, b + 1))

    now = datetime.now(_tz) if _tz else datetime.now()
    seed = int(now.strftime("%Y%m%d"))
    r = random.Random(seed)

    day = now.day
    month = now.month
    wday = now.isoweekday()
    hour = now.hour or 24
    minute = now.minute or 60
    digits_sum = sum(int(x) for x in now.strftime("%Y%m%d%H%M"))

    bases = [day, month, wday, hour, minute, digits_sum % (b - a + 1) or 1]
    center = sum(bases) / len(bases)
    scale = max(1.0, (b - a) / 8.0)

    weights = []
    for n in nums:
        w = 1.0 + math.exp(-abs(n - center) / scale)
        w += 0.25 * sum(1 for base in bases if base and n % base == 0)
        last_digit = int(str(n)[-1])
        w += 0.2 if last_digit == day % 10 else 0.0
        w += 0.2 if last_digit == month % 10 else 0.0
        w += 0.1 * (str(day) in str(n))
        w += 0.1 * (str(month) in str(n))
        weights.append(w)

    return r.choices(nums, weights=weights, k=1)[0]