#!/usr/bin/env python3
"""disk_sched - Disk scheduling simulation."""
import argparse

def fcfs(requests, head):
    total = 0; pos = head; order = list(requests)
    for r in order: total += abs(r - pos); pos = r
    return total, order

def sstf(requests, head):
    remaining = list(requests); total = 0; pos = head; order = []
    while remaining:
        closest = min(remaining, key=lambda r: abs(r - pos))
        total += abs(closest - pos); pos = closest
        order.append(closest); remaining.remove(closest)
    return total, order

def scan(requests, head, direction=1, max_cyl=199):
    left = sorted([r for r in requests if r < head], reverse=True)
    right = sorted([r for r in requests if r >= head])
    if direction == 1: order = right + [max_cyl] + left[::-1]
    else: order = left[::-1] + [0] + right
    total = 0; pos = head
    for r in order:
        if r in requests or r in (0, max_cyl): total += abs(r - pos); pos = r
    return total, [r for r in order if r in requests]

def cscan(requests, head, max_cyl=199):
    right = sorted([r for r in requests if r >= head])
    left = sorted([r for r in requests if r < head])
    order = right + [max_cyl, 0] + left
    total = 0; pos = head
    for r in order: total += abs(r - pos); pos = r
    return total, right + left

def main():
    p = argparse.ArgumentParser(description="Disk scheduling")
    p.add_argument("requests", nargs="+", type=int)
    p.add_argument("-H", "--head", type=int, default=50)
    p.add_argument("-a", "--algorithm", choices=["fcfs","sstf","scan","cscan","all"], default="all")
    args = p.parse_args()
    algos = {"fcfs": lambda: fcfs(args.requests, args.head),
             "sstf": lambda: sstf(args.requests, args.head),
             "scan": lambda: scan(args.requests, args.head),
             "cscan": lambda: cscan(args.requests, args.head)}
    if args.algorithm == "all":
        for name, fn in algos.items():
            total, order = fn()
            print(f"  {name:>5s}: {total:4d} total movement")
    else:
        total, order = algos[args.algorithm]()
        print(f"Total head movement: {total}")
        print(f"Order: {' -> '.join(map(str, order))}")

if __name__ == "__main__":
    main()
