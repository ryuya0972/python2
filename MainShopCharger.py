from StudentCard import StudentCard
from PIL import Image
import gensim

class MainShopCharger:

    # 学籍番号で指定した学生証を取得する
    def insertStudentCard(self, studentId):
        self.insertedStudentCard = StudentCard.getStudentCard(studentId)
    
    # 挿入している学生証にお金をチャージする
    def chargeMoney(self, money):
        if self.insertedStudentCard is not None:
            self.insertedStudentCard.setAccountBalance(self.insertedStudentCard.getAccountBalance() + money)
            self.printAccountBalance()
        else:
            print('学生証が挿入されていません')
    
    # コンソールに学生名と残高を表示する
    def printAccountBalance(self):
        print('残高を表示します')
        print('学生名: ' + self.insertedStudentCard.getStudentName())
        print('残高: ' + str(self.insertedStudentCard.getAccountBalance()))

    # コンソールに最新チャージ年月日を表示する
    def printChargeDate(self):
        chargeDate = self.insertedStudentCard.getChargeDate()
        if chargeDate is not None:
            print('最新チャージ年月日: ' + str(chargeDate))
        else:
            print('この学生証はチャージされていません')
    
    # コンソールに画像と自由テキストを表示する
    def printStudentImageText(self):
        print('画像と自由テキストを表示します')
        im = self.insertedStudentCard.getStudentImage()
        text = self.insertedStudentCard.getStudentText()
        im.show()
        print('自由テキスト: ' + text)
    
    # 自由テキストに含まれる類似ワードを検索する
    def searchSimilarWord(self):
        # モデルの読み込み
        KAMERIO_MODEL = 'wiki.model'
        model = gensim.models.Word2Vec.load(KAMERIO_MODEL)
        # 学生の名前 + 学生の自由テキストを取得し，/ で分割する
        studentName = self.insertedStudentCard.getStudentName()
        studentText = self.insertedStudentCard.getStudentText().split('/')
        # 類似度の閾値を設定
        threshold = 0.5
        # 類似度の計算 + 類似度の高いワードを表示する
        print()
        print('----- ' + studentName + 'の自由テキストと類似度の高いワード -----')
        for card in StudentCard.studentCardList:
            if card.getStudentName() == studentName:
                continue
            otherStudentText = card.getStudentText().split('/')
            for s_text in studentText:
                for o_text in otherStudentText:
                    similarity = model.similarity(s_text, o_text)
                    if similarity > threshold:
                        print()
                        print('similarity = ' + str(similarity))
                        print(studentName + ': ' + s_text + ', ' + card.getStudentName() + ': ' + o_text)
    
    # main メソッド
    def main(self):
        # 画像と自由テキストの設定
        im1   = Image.open('images/im1.jpg')  # 画像: 食べ物の写真
        text1 = '情報/テニス/寿司/日本'          # 自由テキスト: 学科/スポーツ/食べ物/国
        im2   = Image.open('images/im2.jpg')
        text2 = '機械/野球/ピザ/アメリカ'
        im3   = Image.open('images/im3.jpg')
        text3 = '化学/サッカー/スコーン/イギリス'

        # 学生証インスタンスの作成
        studentCard1 = StudentCard(0, 'Haruto', im1, text1)
        studentCard2 = StudentCard(1, 'Liam',   im2, text2)
        studentCard3 = StudentCard(2, 'Olivia', im3, text3)
        
        # エラー処理の表示: 学生証未挿入
        self.chargeMoney(200)
        # 学生証 1 枚目の挿入とチャージ
        self.insertStudentCard(0)
        # 加算
        self.chargeMoney(1000)
        # 引き出し
        self.chargeMoney(-300)
        # 最新チャージ年月日の表示
        self.printChargeDate()
        # 画像と自由テキストの表示
        self.printStudentImageText()
        # 学生証 2 枚目の挿入とチャージ
        self.insertStudentCard(1)
        # エラー処理の表示; 学生証未チャージ
        self.printChargeDate()
        # 加算
        self.chargeMoney(500)
        # 引き出し
        self.chargeMoney(-1000)
        # 類似キーワードの検索
        self.searchSimilarWord()


if __name__ == '__main__':
    mainInstance = MainShopCharger()
    mainInstance.insertedStudentCard = None  # インスタンス変数: 挿入されている学生証
    mainInstance.main()
