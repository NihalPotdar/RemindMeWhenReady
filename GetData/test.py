def find_max_pair(numbers):
    max_nums = [max(numbers[0], numbers[1]), min(numbers[0], numbers[1])]
    for i in range(2, len(numbers)):
        if max_nums[0] < numbers[i]:
            max_nums[1] = max_nums[0]
            max_nums[0] = numbers[i]
        elif max_nums[1] < numbers[i]:
            max_nums[1] = numbers[i]
    return max_nums[0]*max_nums[1]

if __name__ == "__main__":
    print(find_max_pair([1, 1, 2,2]))