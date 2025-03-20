def get_sum(length = 20, symbol = ' - '):
    result = symbol * length
    return result
def generate_string(length = 20, symbol = " - "):
    result = get_sum(length, symbol)
    print(result)
generate_string()
generate_string(10, '+')
generate_string(15,'#')
generate_string(5, '*')