#!/usr/bin/env python3
"""Disk scheduling — FCFS, SSTF, SCAN, C-SCAN."""
import sys

def fcfs(requests, head):
    total = 0; pos = head; order = []
    for r in requests:
        total += abs(r - pos); pos = r; order.append(r)
    return total, order

def sstf(requests, head):
    total = 0; pos = head; remaining = list(requests); order = []
    while remaining:
        closest = min(remaining, key=lambda r: abs(r - pos))
        total += abs(closest - pos); pos = closest
        remaining.remove(closest); order.append(closest)
    return total, order

def scan(requests, head, max_cyl=199):
    total = 0; pos = head; order = []
    left = sorted([r for r in requests if r < head], reverse=True)
    right = sorted([r for r in requests if r >= head])
    for r in right: total += abs(r - pos); pos = r; order.append(r)
    if right: total += abs(max_cyl - pos); pos = max_cyl
    for r in left: total += abs(r - pos); pos = r; order.append(r)
    return total, order

def cscan(requests, head, max_cyl=199):
    total = 0; pos = head; order = []
    right = sorted([r for r in requests if r >= head])
    left = sorted([r for r in requests if r < head])
    for r in right: total += abs(r - pos); pos = r; order.append(r)
    if left:
        total += (max_cyl - pos) + max_cyl; pos = 0
        for r in left: total += abs(r - pos); pos = r; order.append(r)
    return total, order

if __name__ == "__main__":
    head = int(sys.argv[1]) if len(sys.argv) > 1 else 53
    requests = [98, 183, 37, 122, 14, 124, 65, 67]
    print(f"Requests: {requests}")
    print(f"Head at: {head}\n")
    for name, algo in [("FCFS", fcfs), ("SSTF", sstf), ("SCAN", scan), ("C-SCAN", cscan)]:
        total, order = algo(requests, head)
        print(f"  {name:>6}: seek={total:>4} | {order}")
