def re_search_ex1(*args):
    total_sum = 0
    has_numbers = False

    try:
        for arg in args:
            if isinstance(arg, (int, float)):
                total_sum += arg
                has_numbers = True
            elif isinstance(arg, (list, tuple)):
                for item in arg:
                    if isinstance(item, (int, float)):
                        total_sum += item
                        has_numbers = True

        if not has_numbers:
            return 0

        with open('homework2.txt', 'w') as file:
            file.write(str(total_sum))

        return total_sum

    except Exception as e:
        print(f"에러 발생: {e}")
        return 0

# Test
re_search_ex1(1, 2, [3.5, 4], (5, 6), "문자")
