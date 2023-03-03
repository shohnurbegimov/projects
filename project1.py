import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLineEdit,QLabel,QPushButton,QListWidget,QHBoxLayout,QVBoxLayout
from backend import Code

class Baza(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.core = Code()
        self.table()
        


    def table(self):    
        self.setFixedSize(500,600)
        self.h1_box = QHBoxLayout()
        self.h2_box = QHBoxLayout()
        self.h3_box = QHBoxLayout()
        self.h4_box = QHBoxLayout()
        self.h5_box = QHBoxLayout()
        

        self.v_box =QVBoxLayout()
        self.setLayout(self.v_box)
        self.v_box.addLayout(self.h1_box)
        self.v_box.addLayout(self.h2_box)
        self.v_box.addLayout(self.h3_box)
        self.v_box.addLayout(self.h4_box)
        self.v_box.addLayout(self.h5_box)
        

        self.line_1 = QLineEdit()
        self.line_2 = QLineEdit()
        self.line_3 = QLineEdit()
        self.add_product = QPushButton('Add Product')
        self.h1_box.addWidget(self.line_1)
        self.h1_box.addWidget(self.line_2)
        self.h1_box.addWidget(self.line_3)
        self.h1_box.addWidget(self.add_product)



        self.product_label = QLabel("Product")
        self.price_label = QLabel('Price')
        self.amount_labal = QLabel('Amount')
        self.h2_box.addWidget(self.product_label)
        self.h2_box.addWidget(self.price_label)
        self.h2_box.addWidget(self.amount_labal)


        self.list1 = QListWidget()
        self.list2 = QListWidget()
        self.list3 = QListWidget()
        self.h3_box.addWidget(self.list1)
        self.h3_box.addWidget(self.list2)
        self.h3_box.addWidget(self.list3)
        self.getall()

           



        self.line_search = QLineEdit()
        self.btn_search = QPushButton('Search')
        self.get_product = QPushButton('Get all product')
        self.h4_box.addWidget(self.line_search)
        self.h4_box.addWidget(self.btn_search)
        self.h4_box.addWidget(self.get_product)
        

        self.delete_label = QLabel("Product")
        self.delete_line = QLineEdit()
        self.btn_delete = QPushButton('Delete')
        self.h5_box.addWidget(self.delete_label)
        self.h5_box.addWidget(self.delete_line)
        self.h5_box.addWidget(self.btn_delete)


        self.add_product.clicked.connect(self.onAddProduct)
        self.btn_delete.clicked.connect(self.delete)
        self.btn_search.clicked.connect(self.search)
        self.get_product.clicked.connect(self.getall)

        self.show()

    def onAddProduct(self):
        
        product = self.line_1.text()
        price = self.line_2.text()
        amount = self.line_3.text()
        self.core.addProduct(product,int(price),int(amount)) 
        self.line_1.clear()
        self.line_2.clear()
        self.line_3.clear()
        self.list1.addItem(product)
        self.list2.addItem(price)
        self.list3.addItem(amount)
        
    def getall(self):
        for i in range(len(self.core.getAll())):
            self.list1.addItem(self.core.getAll()[i][1])
            self.list2.addItem(str(self.core.getAll()[i][2]))
            self.list3.addItem(str(self.core.getAll()[i][3])) 

    def delete(self):
         
        self.core.deleteProduct(self.delete_line.text())
        self.list1.clear()
        self.list2.clear()
        self.list3.clear()
        self.getall()    
        self.delete_line.clear() 

    def search(self):
        res = self.core.searcProduct(self.line_search.text()  ) 
        self.list1.clear()
        self.list2.clear()
        self.list3.clear()
        self.list1.addItem(res[0][1])
        self.list2.addItem(str(res[0][2]))
        self.list3.addItem(str(res[0][3]))
        self.line_search.clear()
         


app = QApplication([])
win = Baza()
app.exec_()
sys.exit()
