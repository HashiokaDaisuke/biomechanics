import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation


fig = plt.figure()
ax = plt.axes()


def update(frame_cnt):
    plt.cla()# 現在描写されているグラフを消去
    radi = frame_cnt * 0.02
    L, W, H = 1,2,3
    
    c10 = patches.Circle(xy=(-W-H, H-W), radius=radi, fc='#ff731c', ec='none')
    c11 = patches.Circle(xy=(H, H), radius=radi, fc='#ff731c', ec='none')
    c12 = patches.Circle(xy=(L, H+L+H), radius=radi, fc='#ff731c', ec='none')
    r10 = patches.Rectangle(xy=(-(L+W+H)*5, H), width=(L+W+H)*50, height=-(L+W+H)*50, ec='none', fc='white')
    
    c20 = patches.Circle(xy=(-W, -W), radius=radi, fc='#ff731c', ec='none')
    r20 = patches.Rectangle(xy=(-W, H), width=(L+W+H)*50, height=-(L+W+H)*50, ec='none', fc='white')
    
    c1 = patches.Circle(xy=(0, 0), radius=radi, fc='#ff731c', ec='none')
    c2 = patches.Circle(xy=(L, -L), radius=radi, fc='#ff731c', ec='none')
    c3 = patches.Circle(xy=(-2*W-L, -L), radius=radi, fc='#ff731c', ec='none')
    r1 = patches.Rectangle(xy=(0, 0), width=(L+W+H)*5, height=-(L+W+H)*5, ec='none', fc='white')
    r2 = patches.Rectangle(xy=(-W, 0), width=-(L+W+H)*5, height=-(L+W+H)*5, ec='none', fc='white')
    r3 = patches.Rectangle(xy=(-W, H), width=-(L+W+H)*5, height=(L+W+H)*5, ec='none', fc='white')
    r4 = patches.Rectangle(xy=(0, H), width=(L+W+H)*5, height=(L+W+H)*5, ec='none', fc='white')
    r5 = patches.Rectangle(xy=(L+W, -(L+W+H)*5), width=(L+W+H)*50, height=(L+W+H)*50, ec='none', fc='white')
    r6 = patches.Rectangle(xy=(-(L+W+H)*5, -L), width=(L+W+H)*50, height=-(L+W+H)*5, ec='none', fc='white')
    r7 = patches.Rectangle(xy=(-L-W, -(L+W+H)*5), width=-(L+W+H)*50, height=(L+W+H)*50, ec='none', fc='white')
    r8 = patches.Rectangle(xy=(-(L+W+H)*5, H+L), width=(L+W+H)*50, height=(L+W+H)*50, ec='none', fc='white')
    
    
    points = [[0, 0], [0, -L], [-W, -L], [-W, 0], [-W-L, 0], [-W-L, H], [-W, H], [-W, H+L], [0, H+L], [0, H], [L+W, H], [W+L, 0]]

    p1 = patches.Polygon(xy=points, closed=True, ec='k', fc='none')
    
    ax.add_patch(c10)
    ax.add_patch(c11)
    ax.add_patch(c12)
    ax.add_patch(r10)
    
    ax.add_patch(c20)
    ax.add_patch(r20)
    
    ax.add_patch(c1)
    ax.add_patch(c2)
    ax.add_patch(c3)
    ax.add_patch(r1)
    ax.add_patch(r2)
    ax.add_patch(r3)
    ax.add_patch(r4)
    ax.add_patch(r5)
    ax.add_patch(r6)
    ax.add_patch(r7)
    ax.add_patch(r8)
    
    ax.add_patch(p1)
    
    
    plt.axis('scaled')
    ax.set_aspect('equal')
    ax.set_xlim(-L-W-1, L+W+1)
    ax.set_ylim(-L-1, H+L+1)
    
    plt.title(f'frame{frame_cnt}')


def main():
    ani = animation.FuncAnimation(fig, update, interval=10,frames=int(1/0.01*3))
    #plt.show()

    ani.save("output.mp4", writer="ffmpeg", fps=30, dpi=300)
    
if __name__ == "__main__":
    main()