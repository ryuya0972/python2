import datetime
from PIL import Image

class StudentCard:
    # クラス変数
    studentCardList = []  # 存在する学生証のリスト

    # 学籍番号, 学生名, 画像, 自由テキスト, 初期残高(¥0)を設定 + 学生証のインスタンスをリストに追加
    # 最新チャージ年月日の記録用フィールド chargeDate
    def __init__(self, studentId, studentName, studentImage, studentText):
        self.studentId = studentId
        self.studentName = studentName
        self.studentImage = studentImage
        self.studentText = studentText
        self.accountBalance = 0
        self.studentCardList.append(self)
        self.chargeDate = None
    
    # 残高 accountBalance の値を取り出すための getter
    def getAccountBalance(self):
        return self.accountBalance
    
    # 残高 accountBalance の値を設定するための setter
    # 最新チャージ年月日を更新
    def setAccountBalance(self, accountBalance):
        self.accountBalance = accountBalance
        self.chargeDate = datetime.date.today()
    
    # 学生証を取得するための getter
    @classmethod
    def getStudentCard(cls, studentId):
        return cls.studentCardList[studentId]
    
    # 学生名を取得するための getter
    def getStudentName(self):
        return self.studentName
    
    # 登録画像を取得するための getter
    def getStudentImage(self):
        return self.studentImage

    # 自由テキストを取得するための getter
    def getStudentText(self):
        return self.studentText
    
    # 最新チャージ年月日を取得するための getter
    def getChargeDate(self):
        return self.chargeDate
