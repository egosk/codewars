# In this kata you have to create all permutations of an input string and remove duplicates, if present.
# This means, you have to shuffle all letters from the input in all possible orders.
# # Examples:
# # permutations('a'); # ['a']
# # permutations('ab'); # ['ab', 'ba']
# # permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']

def permutations(string):
    results_list = []

    def perm(string, position, length):
        if position == length:
            results_list.append(''.join(string))
        for i in range(position, len(string)):
            string[i], string[position] = string[position], string[i]
            perm(string, position + 1, length)
            string[i], string[position] = string[position], string[i]

    string = list(string) # because strings are immutable
    perm(string, 0, len(string))

    #remove duplicates
    results_list = list(set(results_list))

    return results_list





print(permutations('aabb'))