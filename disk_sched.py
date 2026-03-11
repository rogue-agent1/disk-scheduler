#!/usr/bin/env python3
"""Disk scheduling: FCFS, SSTF, SCAN, C-SCAN."""
import sys
def fcfs(requests,head): return list(requests)
def sstf(requests,head):
    order=[]; remaining=list(requests); pos=head
    while remaining:
        nearest=min(remaining,key=lambda r:abs(r-pos))
        order.append(nearest); remaining.remove(nearest); pos=nearest
    return order
def scan(requests,head,direction=1,max_cyl=199):
    left=[r for r in requests if r<head]; right=[r for r in requests if r>=head]
    if direction==1: return sorted(right)+sorted(left,reverse=True)
    else: return sorted(left,reverse=True)+sorted(right)
def total_seek(order,head):
    total=0; pos=head
    for r in order: total+=abs(r-pos); pos=r
    return total
requests=[98,183,37,122,14,124,65,67]
head=int(sys.argv[1]) if len(sys.argv)>1 else 53
print(f"Requests: {requests}, Head: {head}\n")
for name,fn in [('FCFS',fcfs),('SSTF',sstf),('SCAN',scan)]:
    order=fn(requests,head); seek=total_seek(order,head)
    print(f"  {name:5s}: seek={seek:4d}, order={order}")
