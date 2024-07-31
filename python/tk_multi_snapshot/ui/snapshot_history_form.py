# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'snapshot_history_form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from tank.platform.qt import QtCore
for name, cls in QtCore.__dict__.items():
    if isinstance(cls, type): globals()[name] = cls

from tank.platform.qt import QtGui
for name, cls in QtGui.__dict__.items():
    if isinstance(cls, type): globals()[name] = cls


from ..snapshot_list_view import SnapshotListView

from  . import resources_rc

class Ui_SnapshotHistoryForm(object):
    def setupUi(self, SnapshotHistoryForm):
        if not SnapshotHistoryForm.objectName():
            SnapshotHistoryForm.setObjectName(u"SnapshotHistoryForm")
        SnapshotHistoryForm.resize(541, 735)
        self.verticalLayout = QVBoxLayout(SnapshotHistoryForm)
        self.verticalLayout.setSpacing(-1)
        self.verticalLayout.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header_frame = QFrame(SnapshotHistoryForm)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"#header_frame {\n"
"border-style: solid;\n"
"border-radius: 3;\n"
"border-width: 1;\n"
"border-color: rgb(32,32,32);\n"
"}")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.header_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(80, 80))
        self.label_3.setMaximumSize(QSize(80, 80))
        self.label_3.setPixmap(QPixmap(u":/res/clock.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.label = QLabel(self.header_frame)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.label)

        self.verticalLayout.addWidget(self.header_frame)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.snapshot_list = SnapshotListView(SnapshotHistoryForm)
        self.snapshot_list.setObjectName(u"snapshot_list")
        self.snapshot_list.setStyleSheet(u"#snapshot_list {\n"
"background-color: rgb(255, 128, 0);\n"
"}")

        self.horizontalLayout.addWidget(self.snapshot_list)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.snapshot_btn = QPushButton(SnapshotHistoryForm)
        self.snapshot_btn.setObjectName(u"snapshot_btn")

        self.horizontalLayout_2.addWidget(self.snapshot_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.close_btn = QPushButton(SnapshotHistoryForm)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_2.addWidget(self.close_btn)

        self.restore_btn = QPushButton(SnapshotHistoryForm)
        self.restore_btn.setObjectName(u"restore_btn")
        self.restore_btn.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_2.addWidget(self.restore_btn)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(SnapshotHistoryForm)
        self.close_btn.clicked.connect(SnapshotHistoryForm.close)

        QMetaObject.connectSlotsByName(SnapshotHistoryForm)
    # setupUi

    def retranslateUi(self, SnapshotHistoryForm):
        SnapshotHistoryForm.setWindowTitle(QCoreApplication.translate("SnapshotHistoryForm", u"Form", None))
        self.label_3.setText("")
        self.label.setText(QCoreApplication.translate("SnapshotHistoryForm", u"The list below shows all the snapshots of the currently open work file.  You can go back to a previous version by selecting it and clicking Restore.", None))
        self.snapshot_btn.setText(QCoreApplication.translate("SnapshotHistoryForm", u"New Snapshot...", None))
        self.close_btn.setText(QCoreApplication.translate("SnapshotHistoryForm", u"Close", None))
        self.restore_btn.setText(QCoreApplication.translate("SnapshotHistoryForm", u"Restore", None))
    # retranslateUi
