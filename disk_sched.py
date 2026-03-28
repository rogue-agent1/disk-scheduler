#!/usr/bin/env python3
"""disk_sched - Disk scheduling algorithm simulator."""
import sys
def fcfs(requests, head):
    total=0; order=[head]; pos=head
    for r in requests: total+=abs(r-pos); pos=r; order.append(r)
    return total, order
def sstf(requests, head):
    total=0; order=[head]; pos=head; remaining=list(requests)
    while remaining:
        closest=min(remaining, key=lambda r:abs(r-pos))
        total+=abs(closest-pos); pos=closest; order.append(closest); remaining.remove(closest)
    return total, order
def scan(requests, head, direction=1, max_cyl=199):
    total=0; order=[head]; pos=head
    left=[r for r in requests if r<head]; right=[r for r in requests if r>=head]
    left.sort(reverse=True); right.sort()
    if direction==1:
        for r in right: total+=abs(r-pos); pos=r; order.append(r)
        if left:
            total+=abs(max_cyl-pos); pos=max_cyl
            for r in left: total+=abs(r-pos); pos=r; order.append(r)
    else:
        for r in left: total+=abs(r-pos); pos=r; order.append(r)
        if right:
            total+=pos; pos=0
            for r in right: total+=abs(r-pos); pos=r; order.append(r)
    return total, order
if __name__=="__main__":
    requests=[98,183,37,122,14,124,65,67]
    head=int(sys.argv[1]) if len(sys.argv)>1 else 53
    print(f"Requests: {requests}, Head: {head}")
    for name,fn in [("FCFS",lambda r,h:fcfs(r,h)),("SSTF",lambda r,h:sstf(r,h)),("SCAN",lambda r,h:scan(r,h))]:
        total,order=fn(requests,head)
        print(f"\n{name}: total movement={total}")
        print(f"  Order: {' -> '.join(map(str,order))}")
