"""
A Morse code decoder.

Made for /r/badcode's Bad Code Coding Challenge #29.
Link: https://www.reddit.com/r/badcode/comments/ew2nn2
"""


morse = lambda code: "".join(
        map(
            lambda dits_and_dahs: {
                "/"     : " ",
                ".-"    : "A", "-..."  : "B", "-.-."  : "C", "-.."   : "D",
                "."     : "E", "..-."  : "F", "--."   : "G", "...."  : "H",
                ".."    : "I", ".---"  : "J", "-.-"   : "K", ".-.."  : "L",
                "--"    : "M", "-."    : "N", "---"   : "O", ".--."  : "P",
                "--.-"  : "Q", ".-."   : "R", "..."   : "S", "-"     : "T",
                "..-"   : "U", "...-"  : "V", ".--"   : "W", "-..-"  : "X",
                "-.--"  : "Y", "--.."  : "Z", ".----" : "1", "..---" : "2",
                "...--" : "3", "....-" : "4", "....." : "5", "-...." : "6",
                "--..." : "7", "---.." : "8", "----." : "9", "-----" : "0"
                }[dits_and_dahs],
            code.split(" ")
        )
)
