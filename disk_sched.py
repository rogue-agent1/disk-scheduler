#!/usr/bin/env python3
"""Disk scheduling algorithms (FCFS, SSTF, SCAN, C-SCAN) — zero-dep."""

def fcfs(requests, head):
    total=0; pos=head; order=[]
    for r in requests: total+=abs(r-pos); order.append(r); pos=r
    return total, order

def sstf(requests, head):
    total=0; pos=head; remaining=list(requests); order=[]
    while remaining:
        nearest=min(remaining,key=lambda r:abs(r-pos))
        total+=abs(nearest-pos); pos=nearest; order.append(nearest); remaining.remove(nearest)
    return total, order

def scan(requests, head, max_cyl=199):
    total=0; pos=head; order=[]
    left=sorted([r for r in requests if r<head],reverse=True)
    right=sorted([r for r in requests if r>=head])
    for r in right: total+=abs(r-pos); pos=r; order.append(r)
    if right: total+=abs(max_cyl-pos); pos=max_cyl
    for r in left: total+=abs(r-pos); pos=r; order.append(r)
    return total, order

def cscan(requests, head, max_cyl=199):
    total=0; pos=head; order=[]
    right=sorted([r for r in requests if r>=head])
    left=sorted([r for r in requests if r<head])
    for r in right: total+=abs(r-pos); pos=r; order.append(r)
    if left:
        total+=abs(max_cyl-pos)+max_cyl; pos=0
        for r in left: total+=abs(r-pos); pos=r; order.append(r)
    return total, order

if __name__=="__main__":
    requests=[98,183,37,122,14,124,65,67]
    head=53
    print(f"Requests: {requests}, Head: {head}")
    for name,fn in [("FCFS",fcfs),("SSTF",sstf),("SCAN",scan),("C-SCAN",cscan)]:
        total,order=fn(requests,head)
        print(f"  {name:>6}: total={total:>3} moves, order={order}")
