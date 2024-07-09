import sys

def main(arrays):
    flag = True
    for index, number in enumerate(arrays, start = 1):
       if number % 2 == 0:
           continue
       else:
           print(f"{index}" + "번째 숫자" + f"{number}" + "은 짝수가 아닙니다")
           flag = False
           break
    print(flag)

def extract_even_dict(arrays):
    even_dict = {"index": [], "number": []}
    for index, number in enumerate(arrays, start=1):
        if number % 2 == 0:
            even_dict["index"].append(index)
            even_dict["number"].append(number)
    print(even_dict)

def extract_even_set(arrays):
    even_set = set()
    for index, number in enumerate(arrays):
       if number % 2 == 0:
           even_set.add(number)
    print(even_set) 

def extract_even_list(arrays):
    even_list = []
    for index, number in enumerate(arrays):
       if number % 2 == 0:
           even_list.append(number)
    print(even_list)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python even_checker.py <1 2 3 5 6 7 8>")
        sys.exit(1)
    else:
        arrays = list(map(int, sys.argv[1:]))
        extract_even_list(arrays)