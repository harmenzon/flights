from datetime import datetime, timedelta

now = datetime.now()
next = now + timedelta(minutes=30)
next -= timedelta(minutes=next.minute % 30,
                  seconds=next.second,
                  microseconds=next.microsecond)
pause = (next - now).total_seconds()

print(now, next, pause)