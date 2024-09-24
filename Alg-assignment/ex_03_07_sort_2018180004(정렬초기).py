the_list = [
        6,      82,      21,      58,      22,      54,      71,     215,      99,     227, 
       73,      24,      17,      44,     144,      78,      25,      66,      47,       3, 
       87,      33,     312,     242,      42,      61,     348,     346,      98,      92, 
       83,     100,      94,      40,       5,     458,     364,      26,      64,     735, 
       90,     489,      72,     504,      88,      97,     226,     218,     186,     168, 
]

def sort_bubble(arr):
  n = len(arr)
  print('-- Bubble', '-' * 60)
  print(f'before: {arr}')
  
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        
  print(f'after : {len(arr)=}, {arr}')

def sort_select(arr):
  n = len(arr)
  print('** Select', '*' * 60)
  print(f'before: {arr}')
  for i in range(n):
    min_idx = i
    for j in range(i+1, n):
      if arr[j] < arr[min_idx]:
        min_idx = j
        
      arr[i], arr[min_idx] = arr[min_idx], arr[i]
  print(f'after : {len(arr)=}, {arr}')

def sort_insert(arr):
  n = len(arr)
  print('== Insert', '=' * 60)
  print(f'before: {arr}')
  
  for i in range(1, n):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
      arr[j + 1] = arr[j]
      j -= 1
      arr[j+1] = key
  print(f'after : {len(arr)=}, {arr}')

def sort_shell(arr):
    n = len(arr)
    print('++ Shell', '+' * 60)
    print(f'before: {arr}')
  
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
          
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2  
    
    print(f'after : {len(arr)=}, {arr}')

def main():
  sort_bubble(the_list[:])
  sort_insert(the_list[:])
  sort_select(the_list[:])
  sort_shell(the_list[:])

if __name__ == '__main__':
  main()

