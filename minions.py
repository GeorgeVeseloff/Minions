from  collections import Counter

data = [10, 1, 1, 7, 9, 4, 9, 3, 3, 3, 8, 11]
n = 2
#Это временное, чтобы был какой-то инпут

def solutions(data, n):
  try:
    for i in data:
      if i == int(i):
        pass
  except ValueError:
    print('A list element is not int')
  if len(data) >= 100:
    raise ValueError('The list is too long')
  #на всякий случай проверяю, что нужный тип и длина списка
  jobs_count = Counter(data)
  #считаю, сколько вхождений одинаковых элементов
  filter_out_bad_jobs = {key: value for (key, value) in jobs_count.items() if value < n}
  #фильтрую значения, которые повторяются слишком часто
  good_jobs_unordered = filter_out_bad_jobs.keys()
  #оставляю только список из значений
  good_jobs_ordered = [i for i in data if i in good_jobs_unordered]
  #есть условие, что должен сохранится порядок списка и что работа на Python 2.7,
  #а в нем, вроде словари unordered
  return good_jobs_ordered

print(solutions(data, n))


