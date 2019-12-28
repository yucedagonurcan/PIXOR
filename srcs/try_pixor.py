'''
CSE4088 Intorduction to Machine Learning Project Demo
Onur Can Yücedağ
Emre Erdem
Alperen Bayraktar
'''
import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
from run_kitti import *
sys.path.append('/opt/ros/kinetic/lib/python2.7/dist-packages')

def make_kitti_video():
     
    basedir = '/home/aw2/Development/PIXOR'
    date = '2011_09_26'
    drive = '0048'
    dataset = pykitti.raw(basedir, date, drive)
   
    videoname = "detection_{}_{}.mp4".format(date, drive)
    save_path = os.path.join(basedir, date, "{}_drive_{}_sync".format(date, drive), videoname)    
    run(dataset, save_path)
make_kitti_video()