from cutter import cutter
import random

class feature_generator:
    def __init__(self):
        self.set_num_neighbors(2)
        self.set_attrs(["n","x","nr","v"])

    def set_num_neighbors(self, num_neighbors):
        self.num_neighbors = num_neighbors

    def set_attrs(self, attr_list):
        self.attrs = {}
        for i in range(len(attr_list)):
            self.attrs[attr_list[i]] = i + 1

    def get_feature_str(self, pos, idx, words):
        feature_str = ""
        for i in range(idx - self.num_neighbors, idx + self.num_neighbors + 1):
            if i == idx:
                continue

            pos += 1    
            if i < 0:
                continue
            if i >= len(words):
                break

            if words[i].flag in self.attrs:
                feature_str += " %d:1" % ((pos - 1) * (len(self.attrs) + 1) + self.attrs[words[i].flag] + 1 + 2)
            else:
                feature_str += " %d:1" % ((pos - 1) * (len(self.attrs) + 1) + len(self.attrs) + 1 + 1 + 2)

        return feature_str

    def get_feature_entity_strs(self, line, nrs = [], nts = [], isTrain = False):
        words = cutter.cut(line)
        feature_strs = ""
        '''
        for word in words:
            feature_strs += word.word + ("{%s}" % word.flag.encode('utf-8'))
        feature_strs += "\n"
        '''
        entity_strs = ""
        for i in range(len(words)):
            if words[i].flag != 'nr' and words[i].flag != 'nt':
                continue

            for j in range(i):
                if words[j].flag != 'nr' and words[j].flag != 'nt':
                    continue
                if words[i].flag == words[j].flag:
                    continue

                nr_idx = i
                nt_idx = j
                if words[i].flag == 'nt':
                    nr_idx = j
                    nt_idx = i

                p = 1
                if isTrain:
                    p = -1
                    for k in range(len(nrs)):
                        if (nrs[k].find(words[nr_idx].word)>=0) and (nts[k].find(words[nt_idx].word)>=0):
                            p = 1
                            break

                feature_strs += "%d 1:%d" % (p, nt_idx - nr_idx)
                #feature_strs += "%d 1:%f" % (p, (nt_idx - nr_idx) * 1.0 / len(words))
                feature_strs += " 2:%d 3:%d" %(nr_idx, nt_idx)
                feature_strs += self.get_feature_str(0, nr_idx, words)
                feature_strs += self.get_feature_str(2 * self.num_neighbors, nt_idx, words)
                feature_strs += "\n"
                entity_strs += words[nr_idx].word + " " + words[nt_idx].word + "\n"

        return feature_strs, entity_strs

    def get_feature_strs(self, line, nrs, nts):
        feature_strs, entity_strs = self.get_feature_entity_strs(line, nrs, nts, True)
        return feature_strs

