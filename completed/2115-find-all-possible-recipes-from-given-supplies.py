# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies
"""
This was a fun problem to think through. I took the iterative approach where we
try to cook at least one of the recipes at a time for each loop. If we were able
to make at least one, then we continue the iterations in the main while loop.

There is a more efficient, optimal solution where we use graphs but this is what I came
up with and I'm happy with it :)
"""

from typing import TypedDict


class Solution:
    def findAllRecipes(
        self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]
    ) -> list[str]:
        # Turn the supplies list into a set so that we can have quick lookups
        supply_set: set[str] = set(supplies)

        res: list[str] = []
        continue_loop = True
        while continue_loop:
            continue_loop = False
            for i, recipe in enumerate(recipes):
                # No need to try check the same recipe again if we have
                # already proven we can cook it
                if recipe in supply_set:
                    continue

                # Check if we have each of the ingredients for the
                # current reciple by checking the supply set
                can_cook = True
                for ing in ingredients[i]:
                    if ing not in supply_set:
                        can_cook = False

                # We can count this recipe as a supply if we can cook it
                if can_cook:
                    res.append(recipe)
                    supply_set.add(recipe)
                    continue_loop = True

        return res


class TestCaseType(TypedDict):
    recipes: list[str]
    ingredients: list[list[str]]
    supplies: list[str]


if __name__ == "__main__":
    test_case_1: TestCaseType = {
        "recipes": ["sandwich", "burger", "bread"],
        "ingredients": [
            ["bread", "meat"],
            ["sandwich", "meat", "bread"],
            ["yeast", "flour"],
        ],
        "supplies": ["yeast", "flour", "meat"],
    }  # ["bread","sandwich","burger"]

    cls = Solution()
    ans = cls.findAllRecipes(**test_case_1)
    print("-----")
    print(ans)
