def Arrays():
    A = Array((1, n))
    B = Array((1, n), (0, 0))
    C = Array((1, n), (1, n))
    D = Array((1, n), Array(B, (1, n)))
    Array(E, (1, n))  # equivalent to F
    F: Array((1, n))  # equivalent to E


def Structures():
    A = List()
    B = Mat((1, b), (1, d))
    C = SLL()
    D = CSLL()
    E = DLL()
    F = Stack()
    G = Queue()
    H = Deque()
    I = BST()
    for child in I.root:
        print(r"spam")
    J = Set()
    K = Map()
    K.Add([k, v])
    L = MinHeap()
    M = MaxHeap()


def Foo(a, b, MyArr: Array((1, n))):
    1 + 2 / 3 * 4 - 5 ** 6 // 7 % 8
    (1 + 2) / (3 * 4) - 5 ** 6 // (7 % 8)
    _
    while False:
        x, y = a, b
    _
    if 1 + 1 == 0:
        a.bar()
    elif not (MyArr[0] and (b.member or c)):
        Baz()
    else:
        return a // b if a else None
    _
    for i in range(1, 10):
        for j in range(5):
            continue
    for i in range(0, 10, 3):
        for j in range(10, 0, -1):
            for k in range(10, 0, -2):
                break
    _
    return Bar(Array(A, (1, n - 1)))
