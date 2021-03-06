# coding: utf-8
'''Internationalization'''

class I18N:
    def __init__(self, language):
        if language == 'chi': self._resourceLagChi()
        elif language == 'eng': self._resourceLagEng()
        elif language == 'jap': self._resourceLagJap()
    
    def _resourceLagChi(self):
        self.title = '百变小T'
        self.engine = '选择引擎'
        self.labChi = '中文'
        self.labEng = '英文'
        self.labJap = '日文'
        self.labTrans = '切换语言'
        self.labQuit = '退出'
        self.labStart = '开始'
        self.labTab1 = '图片转文字'
        self.labTab2 = 'PDF转文字'
        self.labTab3 = '横转竖'
        self.inBut = '输入图片'
        self.inButTab2 = '输入文件'
        self.outBut = '输出到'
        self.printScrBut = '截图'
        self.transBut = '转换'
        self.iptBut = '从截图中转换'
        self.printOptFrm = '文字输出'
        self.lang_chi = '中文'
        self.lang_eng = '英文'
        self.lang_jap = '日文'
        self.lang_tra = '繁体中文'
        self.lang_math = '公式'
        self.label_tab = '选择图片包含的语言：'
        self.cleanBut = '清空'
        self.input_tab3 = '输入'
        self.output_tab3 = '输出'
        self.width = '调整每列的字数'
        self.labTab4 = '关键句提取'
        self.numOfSen = '关键句数'
    def _resourceLagEng(self):
        self.title = '百变小T'
        self.engine = 'Select Engine'
        self.labChi = 'Chinese'
        self.labEng = 'English'
        self.labJap = 'Japanese'
        self.labTrans = 'Change Language'
        self.labQuit = 'Quit'
        self.labStart = 'Start'
        self.labTab1 = 'Img2Txt'
        self.labTab2 = 'PDF2Txt'
        self.labTab3 = 'H2V'
        self.inBut = 'Import Image'
        self.inButTab2 = 'Import File'
        self.outBut = 'Save to'
        self.printScrBut = 'ScreenShot'
        self.transBut = 'Transform'
        self.iptBut = 'Transform from ScreenShot'
        self.printOptFrm = 'Text Preview'
        self.lang_chi = 'Chinese'
        self.lang_tra = 'Traditional Chinese'
        self.lang_eng = 'English'
        self.lang_jap = 'Japanese'
        self.lang_math = 'Math Equation'
        self.label_tab = 'Language: ：'   
        self.cleanBut = 'Clean'    
        self.input_tab3 = 'Input'
        self.output_tab3 = 'Output' 
        self.width = 'Words per column'
        self.labTab4 = 'Summary'
        self.numOfSen = 'Lines of Sentences'
    def _resourceLagJap(self):
        self.title = '百变小T'
        self.engine = 'Select Engine'
        self.labChi = '中国語'
        self.labEng = '英語'
        self.labJap = '日本語'
        self.labTrans = '言語を選択する'
        self.labQuit = '閉じる'
        self.labStart = '始め'
        self.labTab1 = '映像転送文字'
        self.labTab2 = 'PDF転送文字'
        self.labTab3 = '方向を変える'
        self.inBut = '画像を導入する'
        self.inButTab2 = '文書を導入する'
        self.outBut = '保存から'
        self.printScrBut = 'キャプチャー'
        self.transBut = 'へんかん'
        self.iptBut = 'スクリーンショットから切り替える'
        self.printOptFrm = 'ぷれびゅー'
        self.lang_chi = '中国語'
        self.lang_eng = '英語'
        self.lang_jap = '日本語'
        self.lang_tra = '食べログ'
        self.lang_math = '数学の公式'
        self.label_tab = '言語: ：'   
        self.cleanBut = '空'       
        self.input_tab3 = '入力'
        self.output_tab3 = '出力'
        self.width='列ごとの文字数'
        self.labTab4 = '要旨'
        self.numOfSen = '重要文数'