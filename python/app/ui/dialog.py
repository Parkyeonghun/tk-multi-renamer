# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(473, 250)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(473, 250))
        self.verticalLayout_7 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.path_layout = QtGui.QHBoxLayout()
        self.path_layout.setObjectName("path_layout")
        self.path_label = QtGui.QLabel(Dialog)
        self.path_label.setObjectName("path_label")
        self.path_layout.addWidget(self.path_label)
        self.path_lineEdit = QtGui.QLineEdit(Dialog)
        self.path_lineEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.path_lineEdit.setObjectName("path_lineEdit")
        self.path_layout.addWidget(self.path_lineEdit)
        self.path_btn = QtGui.QPushButton(Dialog)
        self.path_btn.setObjectName("path_btn")
        self.path_layout.addWidget(self.path_btn)
        self.verticalLayout_7.addLayout(self.path_layout)
        self.add_delete_layout = QtGui.QHBoxLayout()
        self.add_delete_layout.setObjectName("add_delete_layout")
        self.add_btn = QtGui.QPushButton(Dialog)
        self.add_btn.setObjectName("add_btn")
        self.add_delete_layout.addWidget(self.add_btn)
        self.delete_btn = QtGui.QPushButton(Dialog)
        self.delete_btn.setObjectName("delete_btn")
        self.add_delete_layout.addWidget(self.delete_btn)
        self.reset_btn = QtGui.QPushButton(Dialog)
        self.reset_btn.setObjectName("reset_btn")
        self.add_delete_layout.addWidget(self.reset_btn)
        self.verticalLayout_7.addLayout(self.add_delete_layout)
        self.scrollArea = QtGui.QScrollArea(Dialog)
        self.scrollArea.setEnabled(True)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 453, 104))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayoutWidget = QtGui.QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 451, 31))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.replace_box_layout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.replace_box_layout.setContentsMargins(0, 0, 0, 0)
        self.replace_box_layout.setObjectName("replace_box_layout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_7.addWidget(self.scrollArea)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.check_option_layout = QtGui.QVBoxLayout()
        self.check_option_layout.setObjectName("check_option_layout")
        self.folder_name_change_option_checkbox = QtGui.QCheckBox(Dialog)
        self.folder_name_change_option_checkbox.setObjectName("folder_name_change_option_checkbox")
        self.check_option_layout.addWidget(self.folder_name_change_option_checkbox)
        self.all_files_inside_folder_checkbox = QtGui.QCheckBox(Dialog)
        self.all_files_inside_folder_checkbox.setObjectName("all_files_inside_folder_checkbox")
        self.check_option_layout.addWidget(self.all_files_inside_folder_checkbox)
        self.horizontalLayout_5.addLayout(self.check_option_layout)
        self.btn_layout = QtGui.QVBoxLayout()
        self.btn_layout.setObjectName("btn_layout")
        self.space_change_to_underbar_btn = QtGui.QPushButton(Dialog)
        self.space_change_to_underbar_btn.setObjectName("space_change_to_underbar_btn")
        self.btn_layout.addWidget(self.space_change_to_underbar_btn)
        self.replace_cancel_btn_layout = QtGui.QHBoxLayout()
        self.replace_cancel_btn_layout.setObjectName("replace_cancel_btn_layout")
        self.replace_btn = QtGui.QPushButton(Dialog)
        self.replace_btn.setObjectName("replace_btn")
        self.replace_cancel_btn_layout.addWidget(self.replace_btn)
        self.cancel_btn = QtGui.QPushButton(Dialog)
        self.cancel_btn.setObjectName("cancel_btn")
        self.replace_cancel_btn_layout.addWidget(self.cancel_btn)
        self.btn_layout.addLayout(self.replace_cancel_btn_layout)
        self.horizontalLayout_5.addLayout(self.btn_layout)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.path_lineEdit, self.path_btn)
        Dialog.setTabOrder(self.path_btn, self.add_btn)
        Dialog.setTabOrder(self.add_btn, self.delete_btn)
        Dialog.setTabOrder(self.delete_btn, self.reset_btn)
        Dialog.setTabOrder(self.reset_btn, self.folder_name_change_option_checkbox)
        Dialog.setTabOrder(self.folder_name_change_option_checkbox, self.all_files_inside_folder_checkbox)
        Dialog.setTabOrder(self.all_files_inside_folder_checkbox, self.space_change_to_underbar_btn)
        Dialog.setTabOrder(self.space_change_to_underbar_btn, self.replace_btn)
        Dialog.setTabOrder(self.replace_btn, self.cancel_btn)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "The Current Sgtk Environment", None, QtGui.QApplication.UnicodeUTF8))
        self.path_label.setText(QtGui.QApplication.translate("Dialog", "Path", None, QtGui.QApplication.UnicodeUTF8))
        self.path_btn.setText(QtGui.QApplication.translate("Dialog", ">>>", None, QtGui.QApplication.UnicodeUTF8))
        self.add_btn.setText(QtGui.QApplication.translate("Dialog", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.delete_btn.setText(QtGui.QApplication.translate("Dialog", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.reset_btn.setText(QtGui.QApplication.translate("Dialog", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.folder_name_change_option_checkbox.setText(QtGui.QApplication.translate("Dialog", "All folder inside folder", None, QtGui.QApplication.UnicodeUTF8))
        self.all_files_inside_folder_checkbox.setText(QtGui.QApplication.translate("Dialog", "All files inside folder", None, QtGui.QApplication.UnicodeUTF8))
        self.space_change_to_underbar_btn.setText(QtGui.QApplication.translate("Dialog", "Space -> UnderBar", None, QtGui.QApplication.UnicodeUTF8))
        self.replace_btn.setText(QtGui.QApplication.translate("Dialog", "Replace", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_btn.setText(QtGui.QApplication.translate("Dialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

from . import resources_rc
