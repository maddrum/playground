class A:
    pass


class B:
    pass


class C:
    pass


class D:
    pass


class E:
    pass


class F:
    pass


class G:
    pass


class K1(G, C, F):
    pass


class K2(A, B, E):
    pass


class K3(A, F):
    pass


class K4(F, E):
    pass


class M(K1, K2, K3, K4):
    pass


print(M.__mro__)
