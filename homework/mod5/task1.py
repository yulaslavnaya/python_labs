# Создать класс. Стек на структуре данных односвязный список.

class Node:
    """
    Вспомогательный класс для узлов списка
    """

    def __init__(self, data):
        self.data = data  # храним информацию
        self.pref = None  # ссылка на предыдущий узел


class Stack:
    """
    Основной класс для стека
    """

    def __init__(self):
        self.end = None  # ссылка на конец стека

    def pop(self):
        """
        Возвращение последнего элемента из списка с удалением его из списка
        """
        if self.end is None:
            raise IndexError("Стек пуст")

        val = self.end.data
        self.end = self.end.pref
        return val

    def push(self, val):
        """
        Добавление элемента val в конец списка
        """
        new_node = Node(val)
        new_node.pref = self.end
        self.end = new_node

    def print(self):
        """
        Вывод на печать содержимого стека
        """
        if self.end is None:
            print("Стек пуст")
            return

        current = self.end
        elements = []
        while current is not None:
            elements.append(str(current.data))
            current = current.pref

        print(" ".join(elements))


# Пример использования
if __name__ == "__main__":
    stack = Stack()

    # Добавляем элементы
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    # Печатаем стек
    print("Стек после добавления элементов:")
    stack.print()

    # Извлекаем элементы
    print(f"Извлеченный элемент: {stack.pop()}")

    # Печатаем после извлечения
    print("Стек после извлечения элементов:")
    stack.print()

    # Добавляем еще элемент
    stack.push(5)
    print("Стек после добавления 5:")
    stack.print()