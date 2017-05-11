import c4d
from c4d import gui

def main():
    doc = c4d.documents.GetActiveDocument() # Get active document
    objs = doc.GetObjects() # Get a list of all objects in the top level of the OM hierarchy
    objsTags = {}
    i = 0
    maxWidth = 0
    for obj in (objs):
        if "PrintMe" in obj.GetName():
            index = obj.GetName().replace("printChildren: ", "")
            i += 1
            objTags = {}
            op = obj.GetDown()
            j = 0
            while op:
                pos = op.GetRelPos()
                name = op.GetName()
                if pos.x > maxWidth:
                    maxWidth = pos.x
                tag = {
                    'x' : pos.x,
                    'y' : pos.y,
                    'z' : pos.z,
                }
                objTags[name] = tag
                op = op.GetNext()
                j += 1
            objsTags[str(index)] = objTags
    objsTags.update({'maxWidth':maxWidth})
    print objsTags

    target = open('~/Desktop', 'w')
    target.write(objsTags)
    target.close()

if __name__=='__main__':
    main()