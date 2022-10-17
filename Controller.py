from PyQt6.QtCore import QObject, pyqtSlot


class Controller(QObject):
    def __init__(self, model):
        super().__init__()
        self._model = model
        self._operations_order = []

        self._resize_coefficient = 1

        self._move_x = 0
        self._move_y = 0
        self._move_z = 0

        self._shrink_x = 1
        self._shrink_y = 1
        self._shrink_z = 1

        self._rotate_axis = 0  # x:0 y:1 z:2
        self._rotate_angle = 0

        self._resize_flag = False
        self._move_flag = False
        self._shrink_flag = False
        self._rotate_flag = False

    # ================RESIZE===============
    @pyqtSlot(float)
    def resize_coefficient_changed(self, c):
        self._resize_coefficient = c

    @pyqtSlot()
    def resize_clicked(self):
        self._model.resize(self._resize_coefficient)
        self._model.emit_update_model_signal()

    # ================MOVE===============
    @pyqtSlot(float)
    def move_x_changed(self, mx):
        self._move_x = mx

    @pyqtSlot(float)
    def move_y_changed(self, my):
        self._move_y = my

    @pyqtSlot(float)
    def move_z_changed(self, mz):
        self._move_z = mz

    @pyqtSlot()
    def move_clicked(self):
        self._model.move(self._move_x, self._move_y, self._move_z)
        self._model.emit_update_model_signal()

    # ================ROTATE===============
    @pyqtSlot(float)
    def rotate_angle_changed(self, angle):
        self._rotate_angle = angle

    @pyqtSlot(int)
    def rotate_axis_changed(self, axis):
        self._rotate_axis = axis

    @pyqtSlot()
    def rotate_clicked(self):
        self._model.rotate(self._rotate_axis, self._rotate_angle)
        self._model.emit_update_model_signal()

    # ================SHRINK===============
    @pyqtSlot(float)
    def shrink_x_changed(self, mx):
        self._shrink_x = mx

    @pyqtSlot(float)
    def shrink_y_changed(self, my):
        self._shrink_y = my

    @pyqtSlot(float)
    def shrink_z_changed(self, mz):
        self._shrink_z = mz

    @pyqtSlot()
    def shrink_clicked(self):
        self._model.shrink(self._shrink_x, self._shrink_y, self._shrink_z)
        self._model.emit_update_model_signal()

    # ================APPLY===============
    @pyqtSlot(int)
    def resize_changed(self, flag):
        # self._resize_flag = flag
        if flag:
            self._operations_order.append("re")
        else:
            self._operations_order.remove("re")
        print(self._operations_order)

    @pyqtSlot(int)
    def rotate_changed(self, flag):
        # self._rotate_flag = flag
        if flag:
            self._operations_order.append("ro")
        else:
            self._operations_order.remove("ro")
        print(self._operations_order)
    @pyqtSlot(int)
    def move_changed(self, flag):
        # self._move_flag = flag
        if flag:
            self._operations_order.append("mv")
        else:
            self._operations_order.remove("mv")
        print(self._operations_order)

    @pyqtSlot(int)
    def shrink_changed(self, flag):
        # self._shrink_flag = flag
        if flag:
            self._operations_order.append("sh")
        else:
            self._operations_order.remove("sh")
        print(self._operations_order)

    @pyqtSlot()
    def apply_clicked(self):
        for elem in self._operations_order:
            if elem == "re":
                self._model.resize(self._resize_coefficient)
            if elem == "ro":
                self._model.rotate(self._rotate_axis, self._rotate_angle)
            if elem == "mv":
                self._model.move(self._move_x, self._move_y, self._move_z)
            if elem == "sh":
                self._model.shrink(self._shrink_x, self._shrink_y, self._shrink_z)
            self._model.emit_update_model_signal()

    # ================FILES===============
    @pyqtSlot(str)
    def file_picked(self, url):
        self._model.parse_for_url(url)

    @pyqtSlot(str)
    def texture_picked(self, url):
        self._model.set_texture(url)

    @pyqtSlot(str)
    def write_to_file(self, url):
        self._model.load_to_file(url)
