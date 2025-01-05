# https://leetcode.com/problems/count-palindromic-subsequences/
"""
Unable to complete the full solution since this current approach hits the
python error below for large input strings:
    RecursionError: maximum recursion depth exceeded while calling a Python object
"""


class Solution:
    def __init__(self):
        self.cache = {}
        self.MOD = 10**9 + 7

    def countPalindromes(self, s: str) -> int:
        def dfs(index: int, curr_str: str):
            if (index, curr_str) in self.cache:
                return self.cache[(index, curr_str)]

            if index == len(s) or len(curr_str) == 5:
                return 1 if len(curr_str) == 5 and curr_str == curr_str[::-1] else 0

            # Include the current character
            include_count = dfs(index=index + 1, curr_str=f"{curr_str}{s[index]}")

            # Exclude the current character
            exclude_count = dfs(index=index + 1, curr_str=curr_str)

            possible = sum([include_count, exclude_count]) % self.MOD

            self.cache[(index, curr_str)] = possible

            return possible

        return dfs(0, "")


if __name__ == "__main__":
    test_case_1 = "103301"  # 2
    test_case_2 = "0000000"  # 21
    test_case_3 = "9999900000"  # 2
    test_case_4 = (
        "860541882150049565264570080576616956096301490343878067643643586593533755093695"
        "3460983267851033849056"  # 877061
    )
    test_case_5 = (
        "83442916668894914094207330006189460171140132617988103107251008660151377160824985"
        "307077423765371162907520065917846046091286013222982100669116617407024118404043960"
        "2947172771370250698164883019111165547638355854072130822569402255612615322556156032"
        "6161461290077069954469664967657768858482552465558624688277405960969374138903164655"
        "82584262484641006261488982205716744776314836491664500525181934254666576901238032903"
        "339515932987576827366695554790319818344895693331246389489449982552334754372161220763"
        "5142732696070653828079690365687432085697081882554406178691853068683606591990361534118"
        "725331604509219309284072420086484259958072817436999534982318154003099524486189761107"
        "0645491077083180918622789308145917615659340931775390483461087000188185670905434"
        "46782089621905705609441418152912610304353013792257734834934914898722727455535"
        "8115987907656811325839827716087415182068305919550858967866318887150738101980351538"
        "5065241554301460600750495548004172227175929337872840924304879046962889208400025"
        "0575111493747741686010"
    )

    cls = Solution()
    ans = cls.countPalindromes(test_case_4)
    print("-----")
    print(ans)
