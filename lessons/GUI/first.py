from PyQt5 import QtWidgets, QtCore, QtGui, QtSvg, uic
import numpy
VALUE_ROLE = QtCore.Qt.UserRole

CELL_SIZE = 32


SVG_GRASS = QtSvg.QSvgRenderer('grass.svg')
SVG_WALL = QtSvg.QSvgRenderer('wall.svg')

def pixels_to_logical(x, y):
    return y // CELL_SIZE, x // CELL_SIZE


def logical_to_pixels(row, column):
    return column * CELL_SIZE, row * CELL_SIZE


class GridWidget(QtWidgets.QWidget):
    def __init__(self, array):
        super().__init__()  # musíme zavolat konstruktor předka
        self.array = array
        # nastavíme velikost podle velikosti matice, jinak je náš widget příliš malý
        size = logical_to_pixels(*array.shape)
        self.setMinimumSize(*size)
        self.setMaximumSize(*size)
        self.resize(*size)
        self.selected = None

    def paintEvent(self, event):
        rect = event.rect()  # získáme informace o překreslované oblasti

        # zjistíme, jakou oblast naší matice to představuje
        # nesmíme se přitom dostat z matice ven
        row_min, col_min = pixels_to_logical(rect.left(), rect.top())
        row_min = max(row_min, 0)
        col_min = max(col_min, 0)
        row_max, col_max = pixels_to_logical(rect.right(), rect.bottom())
        row_max = min(row_max + 1, self.array.shape[0])
        col_max = min(col_max + 1, self.array.shape[1])

        painter = QtGui.QPainter(self)  # budeme kreslit

        for row in range(row_min, row_max):
            for column in range(col_min, col_max):
                # získáme čtvereček, který budeme vybarvovat
                x, y = logical_to_pixels(row, column)


                rect = QtCore.QRectF(x, y, CELL_SIZE, CELL_SIZE)

                # podkladová barva pod poloprůhledné obrázky
                white = QtGui.QColor(255, 255, 255)
                painter.fillRect(rect, QtGui.QBrush(white))

                # trávu dáme všude, protože i zdi stojí na trávě
                SVG_GRASS.render(painter, rect)

                # zdi dáme jen tam, kam patří
                if self.array[row, column] < 0:
                    SVG_WALL.render(painter, rect)

                # šedá pro zdi, zelená pro trávu
                #if self.array[row, column] < 0:
                #    color = QtGui.QColor(115, 115, 115)
                #else:
                #    color = QtGui.QColor(0, 255, 0)

                # vyplníme čtvereček barvou
                #painter.fillRect(rect, QtGui.QBrush(color))

    def item_activated(self):
        for item in palette.selectedItems():
            print(item.data(VALUE_ROLE))

    def mousePressEvent(self, event):
        # převedeme klik na souřadnice matice
        row, column = pixels_to_logical(event.x(), event.y())

        # Pokud jsme v matici, aktualizujeme data
        if 0 <= row < self.array.shape[0] and 0 <= column < self.array.shape[1]:
            self.array[row, column] = self.selected

            # tímto zajistíme překreslení widgetu v místě změny:
            # (pro Python 3.4 a nižší volejte jen self.update() bez argumentů)
            self.update(*logical_to_pixels(row, column), CELL_SIZE, CELL_SIZE)


def main():
    app = QtWidgets.QApplication([])

    window = QtWidgets.QMainWindow()

    with open('main.ui') as f:
        uic.loadUi(f, window)

    window.show()


    # získáme paletu vytvořenou v Qt Designeru
    palette = window.findChild(QtWidgets.QListWidget, 'palette')

    item = QtWidgets.QListWidgetItem('Grass')  # vytvoříme položku
    icon = QtGui.QIcon('grass.svg')  # ikonu
    item.setIcon(icon)  # přiřadíme ikonu položce
    palette.addItem(item)  # přidáme položku do palety
    item.setData(VALUE_ROLE, -1)

    


    

    # mapa zatím nadefinovaná rovnou v kódu
    array = numpy.zeros((15, 20), dtype=numpy.int8)
    array[:, 5] = -1  # nějaká zeď

    # získáme oblast s posuvníky z Qt Designeru
    scroll_area = window.findChild(QtWidgets.QScrollArea, 'scrollArea')

    # dáme do ní náš grid
    grid = GridWidget(array)
    scroll_area.setWidget(grid)

    palette.itemSelectionChanged.connect(grid.item_activated)
    palette.setCurrentRow(1)




    return app.exec()

main()