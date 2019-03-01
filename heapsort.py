#!/usr/bin/env python
datas = [
    100, 6, 7, 21, 100, 87, 0, 23, 7, 2, 85, 12, 568, 807, 123, 68, 4, 9, 12,
    9, 123, 7690, 13, 760, 124, 679, 21
]


def sort(data):
    i = 0
    j = len(data) - 1
    x = data[0]
    while (i != j):
        while (data[j] >= x and j > i):
            j -= 1
        if j > i:
            data[i] = data[j]
            i += 1
        while (data[i] < x and j > i):
            i += 1
        if j > i:
            data[j] = data[i]
            j -= 1
    data[i] = x
    print(x, data)
    if i > 1:
        data[:i] = sort(data[:i])
    if len(data) - 1 > i:
        data[i + 1:] = sort(data[i + 1:])
    return data


data = datas


def sort2(l, r):
    l0 = l
    r0 = r
    x = data[l]
    while r > l:
        while data[r] >= x and r > l:
            r -= 1
        if r > l:
            data[l] = data[r]
            l += 1

        while data[l] < x and r > l:
            l += 1
        if r > l:
            data[r] = data[l]
            r -= 1
    data[l] = x

    if l > l0:
        sort2(l0, l)
    if r0 > r + 1:
        sort2(r + 1, r0)


heap = [0, 4,1, 2, 3456473,2,734,7456,12,47,4, 5, 6,137, 8685, 9, 10]
lh = len(heap)
res = []


def initHeap(heap, lh):
    haveChildNode = int(lh / 2) - 1
    for i in range(haveChildNode, -1, -1):
        max_c = heap[i * 2 + 1]
        if i * 2 + 2 <lh:
            max_c = max(heap[i * 2 + 1], heap[i * 2 + 2])
        d = i * 2 + 2
        if max_c == heap[i * 2 + 1]:
            d = i * 2 + 1
        if heap[d] > heap[i]:
            heap[d], heap[i] = heap[i], heap[d]
    res.append(heap[0])
    heap[0], heap[lh - 1] = heap[lh - 1], heap[0]
    if len(heap) > 1:
        initHeap(heap[:-1], lh - 1)

if __name__ == "__main__":
    initHeap(heap, lh)
