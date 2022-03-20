# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(521, 448)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addcfg_btn = QtWidgets.QPushButton(self.centralwidget)
        self.addcfg_btn.setObjectName("addcfg_btn")
        self.horizontalLayout.addWidget(self.addcfg_btn)
        self.savecfg_btn = QtWidgets.QPushButton(self.centralwidget)
        self.savecfg_btn.setObjectName("savecfg_btn")
        self.horizontalLayout.addWidget(self.savecfg_btn)
        self.delcfg_btn = QtWidgets.QPushButton(self.centralwidget)
        self.delcfg_btn.setObjectName("delcfg_btn")
        self.horizontalLayout.addWidget(self.delcfg_btn)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.cfgselect_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.cfgselect_combobox.setObjectName("cfgselect_combobox")
        self.gridLayout.addWidget(self.cfgselect_combobox, 0, 1, 1, 1)
        self.config_label = QtWidgets.QLabel(self.centralwidget)
        self.config_label.setObjectName("config_label")
        self.gridLayout.addWidget(self.config_label, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.src_tgt_layout = QtWidgets.QGridLayout()
        self.src_tgt_layout.setObjectName("src_tgt_layout")
        self.target_label = QtWidgets.QLabel(self.centralwidget)
        self.target_label.setObjectName("target_label")
        self.src_tgt_layout.addWidget(self.target_label, 2, 0, 1, 1)
        self.target_btn = QtWidgets.QPushButton(self.centralwidget)
        self.target_btn.setObjectName("target_btn")
        self.src_tgt_layout.addWidget(self.target_btn, 2, 2, 1, 1)
        self.target_line = QtWidgets.QLineEdit(self.centralwidget)
        self.target_line.setObjectName("target_line")
        self.src_tgt_layout.addWidget(self.target_line, 2, 1, 1, 1)
        self.src_label = QtWidgets.QLabel(self.centralwidget)
        self.src_label.setObjectName("src_label")
        self.src_tgt_layout.addWidget(self.src_label, 1, 0, 1, 1)
        self.src_line = QtWidgets.QLineEdit(self.centralwidget)
        self.src_line.setObjectName("src_line")
        self.src_tgt_layout.addWidget(self.src_line, 1, 1, 1, 1)
        self.src_btn = QtWidgets.QPushButton(self.centralwidget)
        self.src_btn.setObjectName("src_btn")
        self.src_tgt_layout.addWidget(self.src_btn, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.src_tgt_layout)
        self.filter_listw = QtWidgets.QListWidget(self.centralwidget)
        self.filter_listw.setObjectName("filter_listw")
        self.verticalLayout.addWidget(self.filter_listw)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.addfilter_btn = QtWidgets.QPushButton(self.centralwidget)
        self.addfilter_btn.setObjectName("addfilter_btn")
        self.horizontalLayout_2.addWidget(self.addfilter_btn)
        self.editfilter_btn = QtWidgets.QPushButton(self.centralwidget)
        self.editfilter_btn.setObjectName("editfilter_btn")
        self.horizontalLayout_2.addWidget(self.editfilter_btn)
        self.delfilter_btn = QtWidgets.QPushButton(self.centralwidget)
        self.delfilter_btn.setObjectName("delfilter_btn")
        self.horizontalLayout_2.addWidget(self.delfilter_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.overwrite_check = QtWidgets.QCheckBox(self.centralwidget)
        self.overwrite_check.setObjectName("overwrite_check")
        self.verticalLayout.addWidget(self.overwrite_check)
        self.backup_btn = QtWidgets.QPushButton(self.centralwidget)
        self.backup_btn.setObjectName("backup_btn")
        self.verticalLayout.addWidget(self.backup_btn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 521, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.cfgselect_combobox, self.addcfg_btn)
        MainWindow.setTabOrder(self.addcfg_btn, self.delcfg_btn)
        MainWindow.setTabOrder(self.delcfg_btn, self.src_line)
        MainWindow.setTabOrder(self.src_line, self.src_btn)
        MainWindow.setTabOrder(self.src_btn, self.target_line)
        MainWindow.setTabOrder(self.target_line, self.target_btn)
        MainWindow.setTabOrder(self.target_btn, self.backup_btn)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addcfg_btn.setStatusTip(_translate("MainWindow", "Make a new configuration..."))
        self.addcfg_btn.setText(_translate("MainWindow", "Add..."))
        self.savecfg_btn.setStatusTip(_translate("MainWindow", "Save the open configuration."))
        self.savecfg_btn.setText(_translate("MainWindow", "Save"))
        self.delcfg_btn.setStatusTip(_translate("MainWindow", "Delete the open configuration..."))
        self.delcfg_btn.setText(_translate("MainWindow", "Delete..."))
        self.cfgselect_combobox.setStatusTip(_translate("MainWindow", "Select a configuration."))
        self.config_label.setText(_translate("MainWindow", "Configuration"))
        self.target_label.setText(_translate("MainWindow", "Target directory"))
        self.target_btn.setStatusTip(_translate("MainWindow", "Open file browser..."))
        self.target_btn.setText(_translate("MainWindow", "Select..."))
        self.target_line.setStatusTip(_translate("MainWindow", "The directory to which files will be copied."))
        self.src_label.setText(_translate("MainWindow", "Source directory"))
        self.src_line.setStatusTip(_translate("MainWindow", "The directory under which files will be copied."))
        self.src_btn.setStatusTip(_translate("MainWindow", "Open file browser..."))
        self.src_btn.setText(_translate("MainWindow", "Select..."))
        self.addfilter_btn.setStatusTip(_translate("MainWindow", "Add a new filter..."))
        self.addfilter_btn.setText(_translate("MainWindow", "Add filter..."))
        self.editfilter_btn.setStatusTip(_translate("MainWindow", "Edit the selected filter..."))
        self.editfilter_btn.setText(_translate("MainWindow", "Edit filter..."))
        self.delfilter_btn.setStatusTip(_translate("MainWindow", "Delete the selected filter..."))
        self.delfilter_btn.setText(_translate("MainWindow", "Delete filter..."))
        self.overwrite_check.setStatusTip(_translate("MainWindow", "Overwrite files that already exist during the backup."))
        self.overwrite_check.setText(_translate("MainWindow", "Overwrite already existing files?"))
        self.backup_btn.setStatusTip(_translate("MainWindow", "Start the backup..."))
        self.backup_btn.setText(_translate("MainWindow", "Start Backup"))
