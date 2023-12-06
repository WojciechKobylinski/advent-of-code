import sys

def solve(times, records):
    MAX_TIME = max(times)
    speedingDistances = [0] * (MAX_TIME+1)

    speed = 0
    for i in range(MAX_TIME):
        speedingDistances[i] = speedingDistances[i-1]+speed
        speed += 1
    
    WAYS = 1
    for i, time in enumerate(times):
        ways = 0
        record = records[i]
        for speedingMillis, speedingDistance in enumerate(range(MAX_TIME)):
            if speedingMillis > time:
                break
            distance = speedingDistance + (time - speedingMillis - 1) * speedingMillis
            if (distance > record):
                ways += 1
        WAYS *= ways
    return WAYS

print(solve([7, 15, 30], [9, 40, 200]))
print(solve([35, 93, 73, 66], [212, 2060, 1201, 1044]))
print(solve([71530], [940200]))
print(solve([35937366], [212206012011044]))