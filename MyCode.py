from itertools import combinations, permutations, repeat
from operator import xor
print(
    next(
        map(
            lambda a: ' '.join(
                map(
                    str,
                    a[0]
                )
            ),
            filter(
                lambda a: all(
                    map(
                        lambda b: xor(
                            *map(
                                lambda c: c in combinations(
                                    a[0],
                                    2
                                ),
                                b,
                            )
                        ),
                        a[1]
                    )
                ),
                (
                    lambda a, b: zip(
                        permutations(a),
                        repeat(b)
                    )
                )
                (
                    *(
                        lambda k, n: (
                            range(
                                1,
                                k + 1
                            ),
                            tuple(
                                map(
                                    lambda i: i[:2],
                                    i[2:],
                                    map(
                                        lambda _: tuple(
                                            map(
                                                int,
                                                input().split()
                                            )
                                        ),
                                        range(n)
                                    )
                                )
                            )
                        )
                    )
                    (
                        *map(
                            int,
                            input().split()
                        )
                    )
                )
            )
        ), 0
    )
)
