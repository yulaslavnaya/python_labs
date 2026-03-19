# Создать класс. Очередь на структуре данных двусвязный список.

class Node:
    """
    Вспомогательный класс для узлов списка
    """

    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел
        self.pref = None  # Ссылка на предыдущий узел


class Queue:
    """
    Основной класс
    """

    def __init__(self):
        self.start = None  # ссылка на начало очереди
        self.end = None  # ссылка на конец очереди

    def pop(self):
        """
        Возвращаем элемент val из начала списка с удалением из списка
        """
        if self.start is None:
            raise IndexError("Очередь пуста")

        val = self.start.data

        # Если в очереди только один элемент
        if self.start == self.end:
            self.start = None
            self.end = None
        else:
            self.start = self.start.nref
            self.start.pref = None

        return val

    def push(self, val):
        """
        Добавление элемента val в конец списка
        """
        new_node = Node(val)

        # Если очередь пуста
        if self.end is None:
            self.start = new_node
            self.end = new_node
        else:
            new_node.pref = self.end
            self.end.nref = new_node
            self.end = new_node

    def insert(self, n, val):
        """
        Вставить элемент val между элементами с номерами n-1 и n
        """
        if n < 0:
            raise IndexError("Индекс не может быть отрицательным")

        # Вставка в начало (перед первым элементом)
        if n == 0:
            new_node = Node(val)
            new_node.nref = self.start
            if self.start is not None:
                self.start.pref = new_node
            self.start = new_node
            if self.end is None:  # если очередь была пуста
                self.end = new_node
            return

        # Поиск позиции для вставки
        current = self.start
        index = 0

        while current is not None and index < n - 1:
            current = current.nref
            index += 1

        # Проверка, что дошли до нужной позиции
        if current is None:
            # Если дошли до конца, добавляем в конец
            if index == n - 1:
                self.push(val)
            else:
                raise IndexError("Индекс выходит за границы очереди")
            return

        # Вставка между current и current.nref
        new_node = Node(val)
        new_node.pref = current
        new_node.nref = current.nref

        if current.nref is not None:
            current.nref.pref = new_node
        current.nref = new_node

        # Если вставляли перед последним элементом, обновляем end
        if new_node.nref is None:
            self.end = new_node

    def print(self):
        """
        Вывод на печать содержимого очереди
        """
        if self.start is None:
            print("Очередь пуста")
            return

        current = self.start
        elements = []
        while current is not None:
            elements.append(str(current.data))
            current = current.nref

        print(" ".join(elements))


# Пример использования
if __name__ == "__main__":
    queue = Queue()

    # Добавляем элементы
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)

    # Печатаем очередь
    print("Очередь после добавления элементов:")
    queue.print()

    # Извлекаем элемент из начала
    print(f"Извлеченный элемент: {queue.pop()}")

    # Печатаем после извлечения
    print("Очередь после извлечения:")
    queue.print()

    # Вставляем элемент
    queue.insert(1, 5)  # вставить между элементами с индексами 0 и 1
    print("Очередь после вставки 5 на позицию 1:")
    queue.print()

    # Вставляем в начало
    queue.insert(0, 6)
    print("Очередь после вставки 6 в начало:")
    queue.print()

    # Вставляем в конец
    queue.insert(5, 7)
    print("Очередь после вставки 7 в конец:")
    queue.print()
