MODULUS = int(1e9 + 7)


def rabin_karp(text, pattern):
    result = []
    pattern_value = 0
    for char in pattern:
        pattern_value *= 10
        pattern_value += ord(char)
        pattern_value %= MODULUS
    current_substring_value = 0
    for i in range(len(pattern)):
        current_substring_value *= 10
        current_substring_value += ord(text[i])
        current_substring_value %= MODULUS

    if text[:len(pattern)] == pattern:
        result.append(0)
    for j in range(1, len(text) - len(pattern) + 1):
        current_substring_value -= ord(text[j - 1]) * (10 ** (len(pattern) - 1))
        current_substring_value *= 10
        current_substring_value += ord(text[j + len(pattern) - 1])
        current_substring_value %= MODULUS
        if current_substring_value == pattern_value and text[j:j+len(pattern)] == pattern:
            result.append(j)

    return tuple(result)


if __name__ == "__main__":
    print("Input string:")
    text = input()
    print("Input pattern:")
    pattern = input()
    result = rabin_karp(text, pattern)
    print("Pattern found at:")
    for index in result:
        print(f"{index}-{index + len(pattern) - 1}", end=" ")
