# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QPlainTextEdit

from videotrans.configure import config
from videotrans.util import tools


class Ui_sttform(object):
    def setupUi(self, sttform):
        self.has_done = False
        sttform.setObjectName("sttform")
        sttform.setWindowModality(QtCore.Qt.NonModal)
        sttform.resize(500, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(sttform.sizePolicy().hasHeightForWidth())
        sttform.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(sttform)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(sttform)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(100, 35))
        self.label.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")

        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.stt_url = QtWidgets.QLineEdit(sttform)
        self.stt_url.setMinimumSize(QtCore.QSize(0, 35))
        self.stt_url.setObjectName("stt_url")

        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.stt_url)
        self.verticalLayout.addLayout(self.formLayout_2)

        # sk
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.formLayout_3.setFormAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.formLayout_3.setObjectName("formLayout_3")
        self.labelkey = QtWidgets.QLabel(sttform)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelkey.sizePolicy().hasHeightForWidth())
        self.labelkey.setSizePolicy(sizePolicy)
        self.labelkey.setMinimumSize(QtCore.QSize(100, 35))
        self.labelkey.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.labelkey.setObjectName("label")

        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelkey)
        self.stt_model = QtWidgets.QComboBox(sttform)
        self.stt_model.addItems([
            "tiny",
            "tiny.en",
            "base",
            "base.en",
            "small",
            "small.en",
            "medium",
            "medium.en",
            "large-v1",
            "large-v2",
            "large-v3",
            "distil-whisper-small.en",
            "distil-whisper-medium.en",
            "distil-whisper-large-v2",
            "distil-whisper-large-v3",
        ])
        self.stt_model.setObjectName("stt_model")

        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.stt_model)
        self.verticalLayout.addLayout(self.formLayout_3)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.set = QtWidgets.QPushButton(sttform)
        self.set.setMinimumSize(QtCore.QSize(0, 35))
        self.set.setObjectName("set")

        self.test = QtWidgets.QPushButton(sttform)
        self.test.setMinimumSize(QtCore.QSize(0, 30))
        self.test.setObjectName("test")

        self.ask = QtWidgets.QPushButton(sttform)
        self.ask.setCursor(QtCore.Qt.PointingHandCursor)
        self.ask.setMinimumSize(QtCore.QSize(0, 40))
        self.ask.setStyleSheet("""background-color:transparent""")
        self.ask.clicked.connect(lambda: tools.open_url(title='stt'))
        self.verticalLayout_2.addWidget(self.ask)

        self.layout_btn = QtWidgets.QHBoxLayout()
        self.layout_btn.setObjectName("layout_btn")

        self.layout_btn.addWidget(self.set)
        self.layout_btn.addWidget(self.test)

        self.verticalLayout_2.addLayout(self.layout_btn)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(sttform)
        QtCore.QMetaObject.connectSlotsByName(sttform)

    def retranslateUi(self, sttform):
        sttform.setWindowTitle("stt语音识别API" if config.defaulelang == 'zh' else 'stt Speech Recognition API')

        self.label.setText('stt API')
        self.labelkey.setText('选择使用的模型' if config.defaulelang == 'zh' else 'Select model')
        tips = """该项目地址 https://github.com/jianchang512/stt"""
        if config.defaulelang != 'zh':
            tips = '''The project at https://github.com/jianchang512/stt'''
        self.ask.setText(tips)
        self.ask.setToolTip("点击打开stt项目主页" if config.defaulelang=='zh' else 'Click to open stt webpage')
        self.stt_url.setPlaceholderText('Api url')
        self.set.setText('保存' if config.defaulelang == 'zh' else 'Save')
        self.test.setText('测试连通性' if config.defaulelang == 'zh' else 'Test')