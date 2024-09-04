b_link = [0] * 16 #配列の初期化
b_link[0]=BodyLink(0, '', .0) # 0のときストップ
b_link[1]=BodyLink(1, 'Hip', .187)
b_link[2]=BodyLink(2, 'Chest', .302)
b_link[3]=BodyLink(3, 'Head', .069)
b_link[4]=BodyLink(4, 'RUArm', .027)
b_link[5]=BodyLink(5, 'RFArm', .016)
b_link[6]=BodyLink(6, 'RHand', .006)
b_link[7]=BodyLink(7, 'LUArm', .027)
b_link[8]=BodyLink(8, 'LFArm', .016)
b_link[9]=BodyLink(9, 'LHand', .006)
b_link[10]=BodyLink(10, 'RThigh', .110)
b_link[11]=BodyLink(11, 'RShin', .051)
b_link[12]=BodyLink(12, 'RFoot', .011)
b_link[13]=BodyLink(13, 'LThigh', .110)
b_link[14]=BodyLink(14, 'LShin', .051)
b_link[15]=BodyLink(15, 'LFoot', .011)

class BodyLink:
    