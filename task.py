import os
import shutil
import logging
entries = os.listdir('E:/')
logging.basicConfig(filename="task.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

#print(entries)
for i in entries:
    if i==entries[0]:
        print(i)
        continue
    inp = "E:/"+i
    if os.path.isfile(inp):
        n, e = os.path.splitext(i)
        e=e[1:]
        if e=="docx" or e=="pdf":
            e="docx and pdf"
        if e=="mkv" or e=="png":
            e="mkv and png"
        print(e,i)
        folder = "Result/"+e
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(folder+" is created succesfully.")
            logger.info(folder+" is created succesfully.")
        dest=folder+"/"+i
        src="E:/"+i
        if shutil.copy(src,dest):
            print("Sucess")
            logger.info(i+" is added into "+folder+" succesfully.")
        else:
            print("Failed")
            logger.info(i+" adding into "+folder+" is failed.")