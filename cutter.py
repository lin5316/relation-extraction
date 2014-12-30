#encoding=utf-8
import jieba
jieba.load_userdict("userdict.txt")
import jieba.posseg as pseg

class cutter:
    @staticmethod
    def is_ns_nt(last, cur):
        if last.flag != 'ns':
            return False
        if cur.flag != 'nt' and cur.word != u'政府':
            return False
        return True

    @staticmethod
    def is_eng_name(last,cur,nex):
        if last.flag != 'nr':
            return False
        if cur.word != '?':
            return False
        if nex.flag != 'nr':
            return False
        return True

    @staticmethod
    def cut(line):
        words = pseg.cut(line)
        buff_words = []

        i = 0
        for word in words:
            if (word.word == '\n'):
                continue

            if i > 0:
                if cutter.is_ns_nt(buff_words[i - 1], word):
                    buff_words[i - 1].word += word.word.encode('utf-8')
                    buff_words[i - 1].flag = 'nt'
                    continue

            if (i>1):
                if cutter.is_eng_name(buff_words[i-2],buff_words[i-1],word):
                    buff_words[i - 2].word += buff_words[i-1].word + word.word.encode('utf-8')
                    del buff_words[len(buff_words) - 1]
                    i = i - 1
                    continue

            if i > 0:
                new_word = word
                new_word.word = word.word.encode('utf-8')
                new_word.flag = word.flag
                buff_words.append(new_word)
                i += 1
            else:
                new_word = word
                new_word.word = word.word.encode('utf-8')
                new_word.flag = word.flag
                buff_words.append(new_word)
                i += 1

        return buff_words

