# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'snapshot_form.ui'
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


from ..snapshot_form import ThumbnailWidget

from  . import resources_rc
from  . import resources_rc

class Ui_SnapshotForm(object):
    def setupUi(self, SnapshotForm):
        if not SnapshotForm.objectName():
            SnapshotForm.setObjectName(u"SnapshotForm")
        SnapshotForm.resize(500, 316)
        SnapshotForm.setMinimumSize(QSize(500, 0))
        SnapshotForm.setFocusPolicy(Qt.TabFocus)
        self.verticalLayout = QVBoxLayout(SnapshotForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.page_stack = QStackedWidget(SnapshotForm)
        self.page_stack.setObjectName(u"page_stack")
        self.snapshot_page = QWidget()
        self.snapshot_page.setObjectName(u"snapshot_page")
        self.verticalLayout_2 = QVBoxLayout(self.snapshot_page)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.header_frame = QFrame(self.snapshot_page)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"#header_frame {\n"
"border-style: solid;\n"
"border-radius: 3;\n"
"border-width: 1;\n"
"border-color: rgb(32,32,32);\n"
"}")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.header_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(80, 80))
        self.label_2.setMaximumSize(QSize(80, 80))
        self.label_2.setPixmap(QPixmap(u":/res/clock.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label = QLabel(self.header_frame)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.label)

        self.verticalLayout_2.addWidget(self.header_frame)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(4)
        self.comment_edit = QTextEdit(self.snapshot_page)
        self.comment_edit.setObjectName(u"comment_edit")
        self.comment_edit.setMinimumSize(QSize(0, 0))
        self.comment_edit.setMaximumSize(QSize(16777215, 120))
        self.comment_edit.setTabChangesFocus(True)

        self.gridLayout_2.addWidget(self.comment_edit, 1, 0, 1, 1)

        self.thumbnail_frame = QFrame(self.snapshot_page)
        self.thumbnail_frame.setObjectName(u"thumbnail_frame")
        self.thumbnail_frame.setMinimumSize(QSize(200, 120))
        self.thumbnail_frame.setMaximumSize(QSize(200, 120))
        self.thumbnail_frame.setStyleSheet(u"#thumbnail_frame {\n"
"border-style: solid;\n"
"border-color: rgb(32,32,32);\n"
"border-width: 1px;\n"
"border-radius: 3px;\n"
"background: rgb(117,117,117);\n"
"}")
        self.thumbnail_frame.setFrameShape(QFrame.StyledPanel)
        self.thumbnail_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.thumbnail_frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.thumbnail_widget = ThumbnailWidget(self.thumbnail_frame)
        self.thumbnail_widget.setObjectName(u"thumbnail_widget")
        self.thumbnail_widget.setMinimumSize(QSize(0, 0))
        self.thumbnail_widget.setMaximumSize(QSize(16777215, 16777215))
        self.thumbnail_widget.setFocusPolicy(Qt.NoFocus)
        self.thumbnail_widget.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.thumbnail_widget)

        self.gridLayout_2.addWidget(self.thumbnail_frame, 1, 1, 1, 1)

        self.label_3 = QLabel(self.snapshot_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setIndent(2)

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_4 = QLabel(self.snapshot_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setIndent(2)

        self.gridLayout_2.addWidget(self.label_4, 0, 1, 1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.cancel_btn = QPushButton(self.snapshot_page)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_5.addWidget(self.cancel_btn)

        self.snapshot_btn = QPushButton(self.snapshot_page)
        self.snapshot_btn.setObjectName(u"snapshot_btn")
        self.snapshot_btn.setMinimumSize(QSize(145, 0))

        self.horizontalLayout_5.addWidget(self.snapshot_btn)

        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.page_stack.addWidget(self.snapshot_page)
        self.status_page = QWidget()
        self.status_page.setObjectName(u"status_page")
        self.verticalLayout_5 = QVBoxLayout(self.status_page)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_5 = QSpacerItem(20, 61, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_5)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.status_icon = QLabel(self.status_page)
        self.status_icon.setObjectName(u"status_icon")
        self.status_icon.setMinimumSize(QSize(80, 80))
        self.status_icon.setMaximumSize(QSize(80, 80))
        self.status_icon.setPixmap(QPixmap(u":/res/success.png"))
        self.status_icon.setScaledContents(True)

        self.verticalLayout_4.addWidget(self.status_icon)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.horizontalLayout_8.addLayout(self.verticalLayout_4)

        self.verticalLayout_6 = QVBoxLayout()
#ifndef Q_OS_MAC
        self.verticalLayout_6.setSpacing(-1)
#endif
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, -1, -1, -1)
        self.status_title = QLabel(self.status_page)
        self.status_title.setObjectName(u"status_title")
        self.status_title.setStyleSheet(u"#status_title {\n"
"font-size: 24px;\n"
"}")

        self.verticalLayout_6.addWidget(self.status_title)

        self.status_details = QLabel(self.status_page)
        self.status_details.setObjectName(u"status_details")
        self.status_details.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.status_details.setWordWrap(False)
        self.status_details.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout_6.addWidget(self.status_details)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.history_btn = QPushButton(self.status_page)
        self.history_btn.setObjectName(u"history_btn")
        self.history_btn.setMinimumSize(QSize(195, 0))

        self.horizontalLayout_7.addWidget(self.history_btn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_7.setStretch(1, 1)

        self.verticalLayout_6.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)

        self.horizontalLayout_8.addLayout(self.verticalLayout_6)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.verticalLayout_5.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_6 = QSpacerItem(20, 61, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_6)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.close_btn = QPushButton(self.status_page)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_6.addWidget(self.close_btn)

        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.page_stack.addWidget(self.status_page)

        self.verticalLayout.addWidget(self.page_stack)

        QWidget.setTabOrder(self.comment_edit, self.cancel_btn)
        QWidget.setTabOrder(self.cancel_btn, self.snapshot_btn)
        QWidget.setTabOrder(self.snapshot_btn, self.close_btn)
        QWidget.setTabOrder(self.close_btn, self.history_btn)

        self.retranslateUi(SnapshotForm)

        self.page_stack.setCurrentIndex(1)
        self.snapshot_btn.setDefault(True)
        self.close_btn.setDefault(True)

        QMetaObject.connectSlotsByName(SnapshotForm)
    # setupUi

    def retranslateUi(self, SnapshotForm):
        SnapshotForm.setWindowTitle(QCoreApplication.translate("SnapshotForm", u"Form", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("SnapshotForm", u"A Snapshot creates a quick backup of your current\n"
"scene that you can easily go back to later.", None))
        self.label_3.setText(QCoreApplication.translate("SnapshotForm", u"Type in a Description:", None))
        self.label_4.setText(QCoreApplication.translate("SnapshotForm", u"Take a Screenshot:", None))
        self.cancel_btn.setText(QCoreApplication.translate("SnapshotForm", u"Cancel", None))
        self.snapshot_btn.setText(QCoreApplication.translate("SnapshotForm", u"Create Snapshot", None))
        self.status_icon.setText("")
        self.status_title.setText(QCoreApplication.translate("SnapshotForm", u"Success!", None))
        self.status_details.setText(QCoreApplication.translate("SnapshotForm", u"Snapshot Successfully Created.", None))
        self.history_btn.setText(QCoreApplication.translate("SnapshotForm", u"View Snapshot History...", None))
        self.close_btn.setText(QCoreApplication.translate("SnapshotForm", u"Close", None))
    # retranslateUi
