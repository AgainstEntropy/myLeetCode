# 字符串解码
# Decode String


class Solution:
    def decodeString(self, s: str) -> str:
        res = ""

        time_stack = []
        str_stack = []

        idx = 0
        while idx < len(s):
            if s[idx].isdigit():
                time, idx = self.get_next_num(s, idx)
                time_stack.append(time)

            if s[idx] == "[":
                idx += 1
                string, idx = self.get_next_str(s, idx)
                str_stack.append(string)

            if s[idx] == "]":
                time = time_stack.pop()
                string = str_stack.pop()
                if len(str_stack) == 0:
                    res += string * time
                else:
                    str_stack[-1] += string * time
                idx += 1
                continue

            if s[idx].isalpha():
                string, idx = self.get_next_str(s, idx)
                if len(str_stack) == 0:
                    res += string
                else:
                    str_stack[-1] += string

        return res

    @staticmethod
    def get_next_num(s: str, idx: int) -> tuple[int, int]:
        num = ""
        while idx < len(s) and s[idx].isdigit():
            num += s[idx]
            idx += 1

        return int(num), idx

    @staticmethod
    def get_next_str(s: str, idx: int) -> tuple[int, int]:
        string = ""
        while idx < len(s) and s[idx].isalpha():
            string += s[idx]
            idx += 1

        return string, idx


if __name__ == "__main__":
    test_cases = [
        ("3[z]2[2[y]pq4[2[jk]e1[f]]]ef", "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"),
        ("2[2[a]]", "aaaa"),
        ("3[z]2[2[a]]", "zzzaaaa"),
        ("3[a]2[bc]", "aaabcbc"),
        ("3[a2[c]]", "accaccacc"),
        ("2[abc]3[cd]ef", "abcabccdcdcdef"),
    ]

    for s, expected in test_cases:
        res = Solution().decodeString(s)
        print(f"decodeString({s}) = {res}, answer is {res == expected}")
