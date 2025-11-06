#!/usr/bin/env python3
import os, subprocess, datetime, random, sys

GIT_NAME  = "Fake Dev"
GIT_EMAIL = "fake@example.com"
FILE      = "filler.txt"

# monthly activity profile:
# month -> (min_commits_per_day, max_commits_per_day)
PROFILE = {
    1: (0,1),  # Jan slow
    2: (0,1),  # Feb slow
    3: (1,3),  # Mar warming up
    4: (2,4),  # Apr
    5: (3,6),  # May busy
    6: (3,6),  # Jun busy
    7: (2,4),  # Jul still active
    8: (1,3),  # Aug slowing
    9: (2,4),  # Sep busy again
    10:(3,6),  # Oct VERY active
    11:(2,4),  # Nov
    12:(1,3),  # Dec relaxed
}

START = datetime.date(2024,1,1)
END   = datetime.date(2024,12,31)

def sh(cmd, env=None): subprocess.check_call(cmd, shell=True, env=env)

def ensure_repo():
    if not os.path.isdir(".git"): sh("git init")
    sh(f'git config user.name "{GIT_NAME}"')
    sh(f'git config user.email "{GIT_EMAIL}"')

def init_commit():
    open(FILE,"a").close()
    try: sh(f'git add {FILE} && git commit -m "init"')
    except: pass

def iso(dt): return dt.strftime("%Y-%m-%dT%H:%M:%S")

def main():
    if os.path.isdir(".git"):
        try:
            c = int(subprocess.check_output("git rev-list --count HEAD",shell=True))
        except: c = 0
        if c>5:
            print("abort — too many existing commits already")
            sys.exit(1)

    ensure_repo()
    init_commit()

    day = START
    while day<=END:
        lo, hi = PROFILE[day.month]
        commits_today = random.randint(lo, hi)

        for _ in range(commits_today):
            seconds = random.randint(0,86399)
            dt = datetime.datetime.combine(day, datetime.time()) + datetime.timedelta(seconds=seconds)
            stamp = iso(dt)
            with open(FILE,"a") as f: f.write(stamp+"\n")
            env = os.environ.copy()
            env["GIT_AUTHOR_DATE"]=stamp
            env["GIT_COMMITTER_DATE"]=stamp
            sh(f'git add {FILE} && git commit -m "filler {day}"', env=env)

        day += datetime.timedelta(days=1)

    print("done — commits created following monthly profile")

if __name__=="__main__":
    main()
