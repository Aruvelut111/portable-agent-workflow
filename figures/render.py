"""Render original conceptual figures. No network, project input, or image generation.

Usage: python figures/render.py
Outputs: SVG, PDF and PNG beside this script.
Only this publication's three named figures are overwritten.
"""
from pathlib import Path
import re

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

OUT = Path(__file__).resolve().parent
INK = '#23313A'
MUTED = '#4B5860'
BLUE = '#006699'
TEAL = '#00664F'
LIGHT = '#F3F6F8'
LINE = '#8B969D'

STYLE = {
    'font.family': 'DejaVu Sans',
    'font.size': 10,
    'text.color': INK,
    'svg.fonttype': 'path',
    'pdf.fonttype': 42,
    'savefig.facecolor': 'white',
}

def canvas(title, subtitle):
    fig, ax = plt.subplots(figsize=(11.6, 6.6), dpi=180)
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    ax.set(xlim=(0, 116), ylim=(0, 66), aspect='equal')
    ax.axis('off')
    label(ax, 4, 62.1, title, size=17, weight='bold')
    label(ax, 4, 58.3, subtitle, size=10.1, color=MUTED)
    return fig, ax

def label(ax, x, y, text, size=11, color=INK, ha='left', weight='normal'):
    return ax.text(x, y, text, fontsize=size, color=color, ha=ha, va='center',
                   fontweight=weight, linespacing=1.45)

def box(ax, x, y, w, h, title, body='', color=INK, fill='white', size=11.3):
    ax.add_patch(Rectangle((x, y), w, h, linewidth=1.0, edgecolor=color,
                           facecolor=fill, zorder=2))
    if body:
        label(ax, x+w/2, y+h*0.70, title, size=size, color=color,
              weight='bold', ha='center')
        label(ax, x+w/2, y+h*0.29, body, size=9.0, color=MUTED, ha='center')
    else:
        label(ax, x+w/2, y+h/2, title, size=size, color=color, ha='center')

def arrow(ax, points, color=INK, dashed=False, both=False):
    for i,(start,end) in enumerate(zip(points,points[1:])):
        final=i==len(points)-2
        ax.add_patch(FancyArrowPatch(start,end,arrowstyle='<->' if both and final else '-|>' if final else '-',
                        mutation_scale=10, linewidth=1.05, color=color,
                        linestyle=(0,(4,3)) if dashed else '-',
                        shrinkA=1.5,shrinkB=1.5,zorder=1))

def save(fig, stem, title, description):
    # Check that text stays on the figure. Topology and meaning need human review.
    fig.canvas.draw()
    renderer=fig.canvas.get_renderer()
    page=fig.bbox
    for ax in fig.axes:
        for t in ax.texts:
            b=t.get_window_extent(renderer)
            if b.x0<page.x0 or b.x1>page.x1 or b.y0<page.y0 or b.y1>page.y1:
                raise ValueError('Text outside figure: '+t.get_text())
    fig.savefig(OUT/(stem+'.svg'), metadata={'Date':None,'Creator':'Original conceptual figure; Matplotlib',
                    'Title':title,'Description':description})
    fig.savefig(OUT/(stem+'.pdf'), metadata={'CreationDate':None,'ModDate':None,
                    'Creator':'Original conceptual figure; Matplotlib','Title':title,'Subject':description})
    fig.savefig(OUT/(stem+'.png'), dpi=180, metadata={'Title':title,'Description':description,
                    'Software':'Matplotlib'})
    # Add an accessible relationship to Matplotlib's SVG metadata/title.
    p=OUT/(stem+'.svg')
    svg=p.read_text(encoding='utf-8')
    svg=re.sub(r'<svg\b', '<svg role="img" aria-label="'+title+'"',svg,count=1)
    p.write_text(svg,encoding='utf-8')
    plt.close(fig)
    print(stem)

def portability():
    fig,ax=canvas('01  Preserve working knowledge across harnesses',
                  'Content can travel. Loading, tools and execution still need adaptation.')
    items=[('Rules','Cross-task\nessentials'),('Knowledge','Facts, sources\nand conditions'),
           ('Procedures','Reusable methods\nand exceptions'),('Capabilities','Entry points, I/O\nand coverage'),
           ('Project state','Decisions, artifacts\nand next actions')]
    for x,(title,body) in zip([4,26,48,70,92],items):
        box(ax,x,42,20,12,title,body,color=BLUE)
        arrow(ax,[(x+10,42),(x+10,36.5)],color=BLUE)
    box(ax,4,28.5,108,8,'Task-relevant context + reachable evidence',color=BLUE,fill=LIGHT,size=12)
    for x,title in zip([4,32,60,88],['Codex','Claude Code','Antigravity','Other harnesses']):
        arrow(ax,[(x+12,28.5),(x+12,22)],color=INK)
        box(ax,x,14,24,8,title,size=11.3)
    label(ax,58,9.5,'Platform adaptation: loading, invocation, permissions, messaging and recovery',
          size=10.3,ha='center')
    label(ax,58,4.8,'Runtime evidence determines what is available in the current session.',
          size=10.1,ha='center',color=MUTED)
    save(fig,'01-portability','Working knowledge and harness adaptation',
         'Five kinds of working material feed task-relevant context and reachable evidence. Different harnesses adapt loading and execution. Content portability does not establish runtime interoperability.')

def collaboration():
    fig,ax=canvas('02  Coordinate around integration and dependencies',
                  'Keep one main point of contact; share the decisions and evidence others need.')
    box(ax,4,43,23,10,'User','Goal and key choices')
    box(ax,44,43,29,10,'Integration owner','Plan, reconcile, integrate',color=BLUE)
    arrow(ax,[(27,48),(44,48)],both=True,color=BLUE)
    label(ax,35.5,51,'Dialogue',ha='center',size=9.3,color=MUTED)
    box(ax,91,43,21,10,'Usable result','Actual consumer',color=TEAL)
    arrow(ax,[(73,48),(91,48)],color=TEAL)
    label(ax,82,51,'Delivery',ha='center',size=9.3,color=MUTED)
    # Shared assignment/feedback lines do not imply dependencies between tasks.
    arrow(ax,[(58.5,43),(58.5,36.5)],color=BLUE,both=True)
    label(ax,62,39.7,'Tasks + feedback',size=9.3,color=MUTED)
    ax.plot([18,98],[36.5,36.5],color=BLUE,linewidth=1.05)
    for x,title,body in [(4,'Bounded task A','Research / implementation'),
                         (44,'Bounded task B','Research / implementation'),
                         (84,'Targeted review','When risk warrants it')]:
        arrow(ax,[(x+14,36.5),(x+14,31)],color=BLUE,both=True)
        box(ax,x,20,28,11,title,body,size=11)
        arrow(ax,[(x+14,20),(x+14,12)],color=LINE,both=True)
    arrow(ax,[(32,25.5),(44,25.5)],color=MUTED,dashed=True,both=True)
    label(ax,38,28.6,'Dependency',ha='center',size=8.1,color=MUTED)
    box(ax,4,4,108,8,'Shared decisions, artifact pointers and current task state',fill=LIGHT,size=11.6)
    label(ax,58,1.5,'Shared files, applications and runtime resources still require explicit coordination.',
          ha='center',size=9.5,color=MUTED)
    save(fig,'02-collaboration','Integration ownership and bounded collaboration',
         'The user talks primarily to the integration owner. Bidirectional blue connections show task assignment and result feedback. The owner coordinates bounded tasks and targeted review. Workers share current state and artifacts, and communicate directly for a specific dependency. Shared runtime resources require coordination.')

def delivery():
    fig,ax=canvas('03  Trace delivery through the actual consumer',
                  'Find the earliest meaningful divergence; resume from confirmed state.')
    items=[('Real input','Identity and version'),('Processing','Read / transform'),
           ('Handoff','Preserved semantics'),('Consumer','Load and use'),('Result','Observable outcome')]
    for x,(title,body) in zip([4,26,48,70,92],items):
        box(ax,x,39,20,12,title,body,color=TEAL if x==92 else INK,size=11.1)
        if x<92: arrow(ax,[(x+20,45),(x+22,45)],color=INK)
    # Diagnostic branch can return to the relevant boundary, not always the input.
    arrow(ax,[(80,39),(80,31)],color=BLUE)
    box(ax,45,23,67,8,'Inspect evidence at the first relevant divergence',color=BLUE,fill=LIGHT,size=11.1)
    arrow(ax,[(45,27),(36,27),(36,39)],color=BLUE,dashed=True)
    label(ax,4,26,'Revise the affected\nassumption or interface',size=10.5,color=BLUE)
    box(ax,4,5,108,10,'Recover from current decisions + committed artifacts',
        'Check earlier side effects before retrying; continue with the next unfinished action.',color=INK,size=11.5)
    arrow(ax,[(80,23),(80,15)],color=LINE,dashed=True)
    label(ax,82,19,'At interruption',size=9.0,color=MUTED)
    save(fig,'03-delivery','Delivery, diagnosis and recovery',
         'Real input passes through processing and handoff into an actual consumer and result. Diagnose discrepancies at the earliest relevant divergence. Recovery uses current decisions and committed artifacts, checking earlier side effects before retrying.')

if __name__=='__main__':
    with plt.rc_context(STYLE):
        portability()
        collaboration()
        delivery()
