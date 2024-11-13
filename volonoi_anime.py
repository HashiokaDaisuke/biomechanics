import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation


fig = plt.figure()
ax = plt.axes()


def update(frame_cnt):
    plt.cla()# 現在描写されているグラフを消去
    radi = frame_cnt * 0.05
    L, W, H = 1,2,3
    c1 = patches.Circle(xy=(0, 0), radius=radi, fc='#ff731c', ec='none')
    c2 = patches.Circle(xy=(-W, -W), radius=radi, fc='#ff731c', ec='none')
    c3 = patches.Circle(xy=(L, -L), radius=radi, fc='#ff731c', ec='none')
    c4 = patches.Circle(xy=(-2*W-L, -L), radius=radi, fc='#ff731c', ec='none')
    r1 = patches.Rectangle(xy=(0, 0), width=(L+W+H)*5, height=-(L+W+H)*5, ec='none', fc='white')
    r2 = patches.Rectangle(xy=(-L, 0), width=-(L+W+H)*5, height=-(L+W+H)*5, ec='none', fc='white')
    r3 = patches.Rectangle(xy=(-L, H), width=-(L+W+H)*5, height=(L+W+H)*5, ec='none', fc='white')
    r4 = patches.Rectangle(xy=(0, H), width=(L+W+H)*5, height=(L+W+H)*5, ec='none', fc='white')
    r5 = patches.Rectangle(xy=(L+W, -(L+W+H)*5), width=(L+W+H)*50, height=(L+W+H)*50, ec='k', fc='white')
    r6 = patches.Rectangle(xy=(-(L+W+H)*5, -L), width=(L+W+H)*50, height=-(L+W+H)*5, ec='k', fc='white')
    r7 = patches.Rectangle(xy=(-L-W, -(L+W+H)*5), width=-(L+W+H)*50, height=(L+W+H)*50, ec='k', fc='white')
    r8 = patches.Rectangle(xy=(-(L+W+H)*5, H+L), width=(L+W+H)*50, height=(L+W+H)*50, ec='k', fc='white')
    ax.add_patch(c1)
    ax.add_patch(c2)
    ax.add_patch(c3)
    ax.add_patch(c4)
    ax.add_patch(r1)
    ax.add_patch(r2)
    ax.add_patch(r3)
    ax.add_patch(r4)
    ax.add_patch(r5)
    ax.add_patch(r6)
    ax.add_patch(r7)
    ax.add_patch(r8)
    
    
    plt.axis('scaled')
    ax.set_aspect('equal')
    ax.set_xlim(-L-W-1, L+W+1)
    ax.set_ylim(-L-1, H+L+1)

def main():
    ani = animation.FuncAnimation(fig, update, interval=100)
    plt.show()
    
if __name__ == "__main__":
    main()