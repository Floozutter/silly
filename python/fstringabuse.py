"""
A one-liner abuse of Python f-strings.
"""


print(f"""Squares: {
        ' '.join(map(
            lambda n: str( int(input(f'#{n + 1}: '))**2 ),
            range( int(input('# of #s to square: ')) )
        ))
}""")
