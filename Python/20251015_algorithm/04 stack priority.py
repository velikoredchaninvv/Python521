# Уровень               b                 3: Продвинутый
# Задача: создайте программу, которая симулирует систему управления задачами.
# Задачи организуются в виде стека.
# Реализуйте возможность добавления задач с приоритетами (обычная и высокая).
# Задачи с высокой приоритетностью должны выполняться первыми, но обычные задачи сохраняются в порядке добавления.

# Часть 1 — Требования и дизайн (кратко)
# У нас есть задачи двух типов: обычная и высокий приоритет.  
# Требование: высокие задачи выполняются первыми. Обычные задачи сохраняют порядок добавления.  
# Слово «стек» в условии можно интерпретировать так: система оперирует «выполнением сверху», но при этом обычные задачи не должны ломать порядок добавления. Поэтому удобна гибридная схема:
# Храним два контейнера:

# high_stack — стек для задач высокого приоритета (LIFO).  
# normal_queue — очередь для обычных задач (FIFO).
# При получении следующей задачи: если есть задачи в high_stack — берём оттуда (pop). Иначе — берём из normal_queue (popleft).

# Итог: высокие задачи "вырвут" выполнение вперёд, при этом обычные задачи выполняются в порядке поступления.

from collections import deque
import itertools
from dataclasses import dataclass

@dataclass
class Task:
    id: int
    decription: str
    priority: str # high or #normal

class TaskManager:
    def __init__(self):
        self._high_stack = [] # LIFO
        self._normal_queue = deque() # FIFO
        self._id_gen = itertools.count(1)

    def add_task(self, description: str, priority: str = 'normal') -> Task:
        task = Task(next(self._id_gen), description, priority)
        if priority == 'high':
            self._high_stack.append(task) # hight - в стек, выполняемся первым в LIFO
        else:
            self._normal_queue.append(task) # normal - в очередь FIFO
        return task
    
    def get_next(self) -> Task | None:
        if self._high_stack:
            return self._high_stack.pop()
        if self._normal_queue:
            return self._normal_queue.popleft()
        return None
    
    def peek_next(self) -> Task | None:
        if self._high_stack:
            return self._high_stack[-1]
        if self._normal_queue:
            return self._normal_queue[0]
        return None
    
    def is_empty(self) -> bool:
        return not (self._high_stack or self._normal_queue)
    
    def list_all(self):
        # для отладки: сначала high (От верхушки к дну), затем normal в порядке очереди
        return list(reversed(self._high_stack)) + list(self._normal_queue)
    
tm = TaskManager()
tm.add_task('Задача А') # normal
tm.add_task('Задача Б') # normal
tm.add_task('Срочная 1', priority="high") # high
tm.add_task('Срочная 2', priority="high") # high

# Выполнение:
print(tm.get_next().description) # -> "Срочная 2" (LIFO внутри high)
print(tm.get_next().description) # -> "Срочная 1"
print(tm.get_next().description) # -> "Задача А" (FIFO среди normal)

# Ключевые замечания:
# Высокие задачи выполняются первыми, и среди высоких — последний добавленный выполняется первым (стек).  
# Обычные задачи сохраняют порядок добавления (очередь).  
# Операции добавления/извлечения — O(1).