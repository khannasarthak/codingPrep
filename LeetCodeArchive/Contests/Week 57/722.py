# Need to take into consideration '\n' of commented multiline, rest all seems correct


class Solution(object):
    def removeComments(self, source):
        op= []
        multi = 0
        for c,i in enumerate(source):

            if '//' in i:
                op.append(i[:i.index('//')])
            elif '/*' in i and '*/' in i:
                if '"' in i and i.index('/*')<i.index('"'):
                    op.append(i[:i.index('/*')])
                else:
                    op.append(i[:i.index('/*')])
            elif '/*' in i and '*/' not in i:
                op.append(i[:i.index('/*')])
                multi=1
            elif '/*' not in i and '*/'  in i:
                if multi==1:
                    op.append(i[i.index('*/')+2:])
                multi=0
            elif multi==1 and '/*' not in i and '*/' not in i:
                continue
            else:
                op.append(i)



        final = []

        for c,i in enumerate(op):
            if i!='':
                final.append(i)
