logs = [
    "2024-01-01 10:00:00 LOGIN_SUCCESS user=alice",
    "2024-01-01 10:01:00 LOGIN_FAILED user=bob",
    "2024-01-01 10:02:00 LOGIN_FAILED user=admin",
    "2024-01-01 10:03:00 LOGIN_SUCCESS user=carol",
]

for line in logs:
    if "LOGIN_FAILED" in line:
        print(line)