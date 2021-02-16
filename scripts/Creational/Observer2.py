# define a generic observer type
class Observer():
    def update(self, subject) -> None:
        pass

class Subject:
    def __init__(self) -> None:
        self._observers: List[Observer] = []

    def attach(self, observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer) -> None:
        #pass
        self._observers.remove(observer)
        #with suppress(ValueError):
            #self._observers.remove(observer)

    def notify(self, modifier) -> None:
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)

class Data(Subject):
    def __init__(self, name: str = "") -> None:
        super().__init__()
        self.name = name
        self._data = 0

    @property
    def data(self) -> int:
        return self._data

    @data.setter
    def data(self, value: int) -> None:
        self._data = value
        self.notify(self)


class HexViewer:
    def update(self, subject: Data) -> None:
        print(f"HexViewer: Subject {subject.name} has data 0x{subject.data:x}")


class DecimalViewer:
    def update(self, subject: Data) -> None:
        print(f"DecimalViewer: Subject {subject.name} has data {subject.data}")


def main():
    # data
    data1 = Data('Data 1')
    data2 = Data('Data 2')
    #view
    view_dec = DecimalViewer()
    view_hex = HexViewer()
    # attachments for data1
    data1.attach(view_dec)
    data1.attach(view_hex)
    # attachments for data2
    data2.attach(view_hex)
    data2.attach(view_dec)
    
    # original values
    data1.data = 10
    print('--')
    # DecimalViewer: Subject Data 1 has data 10
    # HexViewer: Subject Data 1 has data 0xa
    data2.data = 15
    print('--')
    # HexViewer: Subject Data 2 has data 0xf
    # DecimalViewer: Subject Data 2 has data 15
    
    # changed values
    data1.data = 3
    print('--')
    # DecimalViewer: Subject Data 1 has data 3
    # HexViewer: Subject Data 1 has data 0x3
    data2.data = 5
    print('--')
    # HexViewer: Subject Data 2 has data 0x5
    # DecimalViewer: Subject Data 2 has data 5
    
    # Detach HexViewer from data1 and data2
    data1.detach(view_hex)
    data2.detach(view_dec)

    # original values
    data1.data = 10
    # DecimalViewer: Subject Data 1 has data 10
    data2.data = 15
    # DecimalViewer: Subject Data 2 has data 15
    
if __name__ == "__main__":
    main()